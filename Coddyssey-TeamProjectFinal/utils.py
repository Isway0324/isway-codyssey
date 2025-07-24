import argparse as parse
import pandas as pd
import os
import matplotlib.patches as patches


def argparsing():
    parser = parse.ArgumentParser()

    parser.add_argument(
        "--data-dir",
        type=str,
        help="data directory path",
        default="")
    args = parser.parse_args()
    return args


def load_data():
    args = argparsing()
    area_map = pd.read_csv(os.path.join(args.data_dir, 'area_map.csv'))
    area_category = pd.read_csv(
        os.path.join(
            args.data_dir,
            'area_category.csv'))
    area_struct = pd.read_csv(os.path.join(args.data_dir, 'area_struct.csv'))
    return {"map": area_map, "category": area_category, "struct": area_struct}


def mkdir(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as e:
            print(f"폴더 '{path}' 생성 중 오류가 발생했습니다: {e}")
    else:
        pass


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
