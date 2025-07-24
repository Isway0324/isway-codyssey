import pandas as pd
import matplotlib.pyplot as plt
import utils
from collections import OrderedDict


def main(save_path, area_map, area_category: pd.DataFrame,
         area_struct: pd.DataFrame):
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
            ax.scatter(x, y, c='green', marker='^', label="MyHome")
            ax.text(x - 0.5, y - 0.5, 'MyHome')

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


if __name__ == '__main__':
    area = utils.load_data()
    area_map = area["map"]
    area_category = area["category"]
    area_struct = area["struct"]
    area_category.loc[4] = {'category': 0, 'struct': 'None'}
    main('res/map.png', area_map, area_category, area_struct)
