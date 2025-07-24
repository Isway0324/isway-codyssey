import utils
def save_md(save_path, area_1_df):
    struct_stats = area_1_df['struct'].value_counts()

    with open(save_path, "w", encoding="utf-8") as f:
            f.write("# 구조물 종류별 통계 (Area 1)\n\n")
            f.write("| 구조물 종류 | 개수 |\n")
            for k, v in struct_stats.items():
                f.write(f"| {k:<17} | {v:>3} |\n")
def main():
    # 1. CSV 파일 불러오기
    area = utils.load_data()
    map_df = area["map"]
    struct_df = area["struct"]
    category_df = area["category"]

    # 2. 열 이름 정리 (공백 제거)
    category_df.columns = category_df.columns.str.strip()

    # 3. 구조물 ID를 이름으로 변환 (category → struct)
    struct_named_df = struct_df.merge(category_df, on='category', how='left')

    # 4. map 정보와 병합 (건설 현장 정보 포함)
    merged_df = struct_named_df.merge(map_df, on=['x', 'y'], how='left')

    # 5. area 기준 정렬
    merged_df = merged_df.sort_values(by='area')

    # 6. area 1에 해당하는 데이터만 필터링
    area_1_df = merged_df[merged_df['area'] == 1]

    # 7. 결과 파일로 저장
    area_1_df.to_csv('res/area1_filtered.csv', index=False)

    # 8. (보너스) 구조물 종류별 요약 통계 출력
    print('📊 구조물 종류별 통계 (Area 1)')
    print(area_1_df['struct'].value_counts())
    save_md("res/struct_count.md", area_1_df)


if __name__ == "__main__":
    main()
