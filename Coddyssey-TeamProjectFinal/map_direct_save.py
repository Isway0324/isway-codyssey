import utils
import pandas as pd
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import os
from collections import OrderedDict


def bfs_shortest_path_list_queue(
        start, end, min_x, max_x, min_y, max_y, block_set):
    # Queue stores tuples of (current_coordinates, path_to_current_coordinates)
    # Using a list to simulate a queue, always process the first element
    # (index 0)
    queue = [(start, [start])]
    visited = set([start])  # Use a set for efficient O(1) lookups

    # Define possible movements (right, left, down, up)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue_index = 0  # To simulate popleft, we'll just increment an index

    while queue_index < len(queue):
        current_coords, path = queue[queue_index]  # Get the current item

        queue_index += 1  # "Pop" it by incrementing the index

        # Check if we've reached the end
        if current_coords == end:
            return path

        (x, y) = list(current_coords)

        # Explore neighbors
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            next_coords = (nx, ny)

            # Check conditions: within bounds, not a block, and not visited
            if (min_x <= nx <= max_x and
                min_y <= ny <= max_y and
                next_coords not in block_set and
                    next_coords not in visited):

                visited.add(next_coords)  # Mark as visited
                # Enqueue the new coordinates and the path to reach them
                queue.append((next_coords, path + [next_coords]))

    return None  # No path found


def patching(ax, xmin, ymin, width, height):
    rect1 = patches.Rectangle(
        (xmin,
         ymin),
        width,
        height,
        facecolor='yellow',
        alpha=0.3,
        zorder=-1,
        label='Area 1')
    ax.add_patch(rect1)
    return ax


def main(save_path, area_map, area_category: pd.DataFrame,
         area_struct: pd.DataFrame):
    end = []
    utils.mkdir("res")
    area_category.columns = area_category.columns.str.strip()
    area_category['struct'] = area_category['struct'].map(str).map(str.strip)
    area_struct.columns = area_struct.columns.str.strip()
    area_struct['type'] = area_struct['category'].map(lambda x: str(
        area_category['struct'][area_category['category'] == x].values[0])).values
    area_struct['ConstructionSite'] = area_map['ConstructionSite']
    fig, ax = plt.subplots()
    area1_x = area_struct[area_struct["area"] == 1]["x"].values
    area1_y = area_struct[area_struct["area"] == 1]["y"].values
    ax = utils.patching(
        ax,
        area1_x.min() -
        0.5,
        area1_y.min() -
        0.5,
        area1_x.max() -
        area1_x.min(),
        area1_y.max() -
        area1_y.min())
    ax.scatter(area1_x, area1_y, marker="")
    block = []
    for i in range(len(area_struct)):
        loc = area_struct.loc[i]
        x = loc["x"]
        y = loc["y"]
        con = loc["ConstructionSite"]
        t = loc["type"]

        if con == 1:
            fig.gca().add_patch(
                plt.Rectangle(
                    (x - 0.5,
                     y - 0.5),
                    1,
                    1,
                    color='gray',
                    zorder=3,
                    alpha=0.8))
            block.append((int(x), int(y)))
        elif t == "None":
            ax.scatter(x, y, marker='')
        elif t == "Apartment":
            ax.scatter(
                x,
                y,
                s=150,
                color='#A0522D',
                marker='o',
                edgecolor='black',
                zorder=2,
                label="Apartment")
            ax.text(x - 0.3, y - 0.5, 'A')
        elif t == "Building":
            ax.scatter(
                x,
                y,
                s=150,
                color='#A0522D',
                marker='o',
                edgecolor='black',
                zorder=2,
                label="Building")
            ax.text(x - 0.3, y - 0.5, 'B')
        elif t == "BandalgomCoffee":
            end.append((int(x), int(y)))
            fig.gca().add_patch(
                plt.Rectangle(
                    (x - 0.4,
                     y - 0.4),
                    0.8,
                    0.8,
                    color='green',
                    zorder=2,
                    alpha=0.8))
            ax.text(x - 0.3, y - 0.5, 'BC')
        elif t == "MyHome":
            start = (int(x), int(y))
            ax.scatter(x, y, c='green', marker='^', label="MyHome")
            ax.text(x - 0.5, y - 0.5, 'MyHome')

    lines1 = bfs_shortest_path_list_queue(start, end[0], 0, 15, 0, 15, block)
    lines2 = bfs_shortest_path_list_queue(start, end[1], 0, 15, 0, 15, block)

    if len(lines1) <= len(lines2):
        ax.plot([x for x, _ in lines1], [y for _, y in lines1], c="red")
        pd.DataFrame({"x": [x for x, _ in lines1], "y": [y for _, y in lines1]}).to_csv(
            "res/home_to_cafe.csv", index=False)
    else:
        ax.plot([x for x, _ in lines2], [y for _, y in lines2], c="red")
        pd.DataFrame({"x": [x for x, _ in lines2], "y": [y for _, y in lines2]}).to_csv(
            "res/home_to_cafe.csv", index=False)

    handles, labels = ax.get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    ax.set_xlim((-0.1, 15))      # if문안에 넣기
    ax.set_xticks(range(1, 16, 1))
    ax.set_yticks(range(15, 0, -1))
    ax.invert_yaxis()
    ax.legend(by_label.values(), by_label.keys(), loc='lower right')
    ax.grid(True, 'both')
    fig.savefig(save_path, dpi=300)
    return ax


if __name__ == "__main__":
    area = utils.load_data()
    area_map = area["map"]
    area_category = area["category"]
    area_struct = area["struct"]
    area_category.loc[4] = {'category': 0, 'struct': 'None'}
    main("res/map_final.png", area_map, area_category, area_struct)
