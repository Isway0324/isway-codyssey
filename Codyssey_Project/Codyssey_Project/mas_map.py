"""
import pandas as pd

# 1. CSV 파일 불러오기
map_df = pd.read_csv('area_map.csv')
struct_df = pd.read_csv('area_struct.csv')
category_df = pd.read_csv('area_category.csv')

# 2. 열 이름 정리 (공백 제거)
category_df.columns = category_df.columns.str.strip()

# 3. 구조물 ID를 이름으로 변환 (category → struct)
struct_named_df = struct_df.merge(category_df, on='category', how='left')

# 4. map 정보와 병합 (건설 현장 정보 포함)
## merged_df = struct_named_df.merge(map_df, on=['x', 'y'], how='left')
merged_df = map_df.merge(struct_named_df, on=['x', 'y'], how='left')


# 5. area 기준 정렬
merged_df = merged_df.sort_values(by='area')

# 6. area 1에 해당하는 데이터만 필터링
area_1_df = merged_df[merged_df['area'] == 1].reset_index(drop=True)

# 7. 결과 파일로 저장
area_1_df.to_csv('area1_filtered.csv', index=False)

# 8. (보너스) 구조물 종류별 요약 통계 출력
print('📊 구조물 종류별 통계 (Area 1)')
print(area_1_df['struct'].value_counts())

"""


import pandas as pd

# 1. CSV 파일 불러오기
map_df = pd.read_csv('area_map.csv')
struct_df = pd.read_csv('area_struct.csv')
category_df = pd.read_csv('area_category.csv')

# 2. 열 이름 정리 (공백 제거)
category_df.columns = category_df.columns.str.strip()

# 3. MyHome 존재 여부 확인
if 'MyHome' not in category_df['struct'].values:
    # category 5번이 없다면 추가
    category_df.loc[len(category_df)] = {'category': 5, 'struct': 'MyHome'}

# 4. MyHome이 struct_df에 존재하지 않으면 자동 추가
has_myhome = struct_df.merge(category_df, on='category', how='left')
if 'MyHome' not in has_myhome['struct'].values:
    # area 1, x=3, y=6, category=5으로 추가
    new_row = {'area': 1, 'x': 3, 'y': 6, 'category': 5}
    struct_df.loc[len(struct_df)] = new_row
    print('✅ MyHome이 없어서 자동으로 추가했습니다: (area=1, x=3, y=6, category=5)')

# 5. 구조물 ID를 이름으로 변환 (category → struct)
struct_named_df = struct_df.merge(category_df, on='category', how='left')

# 6. map 정보와 병합 (건설 현장 정보 포함)
merged_df = struct_named_df.merge(map_df, on=['x', 'y'], how='left')

# 7. area 기준 정렬
merged_df = merged_df.sort_values(by='area')

# 8. area 1에 해당하는 데이터만 필터링
area_1_df = merged_df[merged_df['area'] == 1].reset_index(drop=True)

# 9. 결과 파일로 저장
area_1_df.to_csv('area1_filtered.csv', index=False)

# 10. (보너스) 구조물 종류별 요약 통계 출력
print('📊 구조물 종류별 통계 (Area 1)')
print(area_1_df['struct'].value_counts())
