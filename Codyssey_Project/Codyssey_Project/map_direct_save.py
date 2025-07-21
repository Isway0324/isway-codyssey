import pandas as pd
import matplotlib.pyplot as plt
from collections import deque

def bfs(start, goal, obstacles, width, height):
    # BFS로 최단 경로
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (1 <= nx <= width and 1 <= ny <= height and
                (nx, ny) not in visited and (nx, ny) not in obstacles):     # 이미 방문 & 장애물 탐지
                visited.add((nx, ny))                                       # 방문 추가
                queue.append(((nx, ny), path + [(nx, ny)]))                 # 큐에 추가
    return []

def main():
    area_map = pd.read_csv('area_map.csv')
    struct_df = pd.read_csv('area_struct.csv')
    category_df = pd.read_csv('area_category.csv')

    # struct 컬럼 생성 (카테고리 → 이름)
    struct_df = struct_df.merge(category_df, on='category', how='left')
    struct_df['struct'] = struct_df['struct'].fillna('').str.strip()

    # 지도 크기
    width = area_map['x'].max()
    height = area_map['y'].max()
    max_y = height

    # 장애물: ConstructionSite == 1
    obstacles = set(area_map[area_map['ConstructionSite'] == 1][['x', 'y']].apply(tuple, axis=1))

    # MyHome & BandalgomCoffee 좌표
    home = struct_df[struct_df['struct'] == 'MyHome']
    cafe = struct_df[struct_df['struct'] == 'BandalgomCoffee']

    if home.empty or cafe.empty:
        raise ValueError('❌ MyHome 또는 BandalgomCoffee 데이터 없음')

    start = tuple(home[['x', 'y']].values[0])
    end = tuple(cafe[['x', 'y']].values[0])

    print(f'✅ Start(MyHome): {start}, Goal(BandalgomCoffee): {end}')
    print(f'✅ 지도 크기: {width} x {height}, 장애물 수: {len(obstacles)}')

    # 2. BFS로 최단 경로 탐색
    path = bfs(start, end, obstacles, width, height)
    if not path:
        raise ValueError('❌ 최단 경로 없음 (장애물이 막고 있음)')

    # 경로 저장
    pd.DataFrame(path, columns=['x', 'y']).to_csv('home_to_cafe.csv', index=False)

    # 3. 시각화
    plt.figure(figsize=(6, 6))
    plt.grid(True)

    # 건설 현장
    plt.scatter(area_map[area_map['ConstructionSite'] == 1]['x'],
                max_y - area_map[area_map['ConstructionSite'] == 1]['y'],
                c='gray', marker='s', label='ConstructionSite')

    # MyHome
    plt.scatter(start[0], max_y - start[1], c='green', marker='^', s=100, label='MyHome')

    # BandalgomCoffee
    plt.scatter(end[0], max_y - end[1], c='green', marker='s', s=100, label='BandalgomCoffee')


    # Building
    building_df = struct_df[struct_df['struct'] == 'Building']
    plt.scatter(building_df['x'], max_y - building_df['y'], c='brown', marker='o', label='Building')
    for x, y in zip(building_df['x'], building_df['y']):
        plt.text(x - 0.3, max_y - y + 0.3, 'B', fontsize=8)

    # Apartment
    apartment_df = struct_df[struct_df['struct'] == 'Apartment']
    plt.scatter(apartment_df['x'], max_y - apartment_df['y'], c='purple', marker='v', label='Apartment')
    for x, y in zip(apartment_df['x'], apartment_df['y']):
        plt.text(x - 0.3, max_y - y + 0.3, 'A', fontsize=8)


    # 경로
    for x, y in path:
        plt.plot(x, max_y - y, 'r.')

    plt.title('Shortest Path: MyHome → BandalgomCoffee')
    plt.legend(fontsize=7, loc='lower right')
    plt.savefig('map_final.png', dpi=300)
    print('✅ map_final.png 생성 완료')

if __name__ == '__main__':
    main()

