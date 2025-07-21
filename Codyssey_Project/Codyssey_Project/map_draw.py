import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def main(save_path, area_category: pd.DataFrame, area_struct: pd.DataFrame, cmaps =list(mcolors.CSS4_COLORS.keys())):
    area_struct['type'] = area_struct['category'].map(lambda x: str(area_category['struct'][area_category['category']==x].values[0])).values
    
    plt.figure(figsize = (6, 4))
    area = area_map[area_map['ConstructionSite']==1]
    plt.scatter(area['x'].values, 15-area['y'].values, c='grey', marker='s', label = 'ConstructionSite')
    for i in range(len(area_category)):
        c = area_category['struct'][i].strip()
        if c == 'None':
            area = area_struct[area_struct['type'].map(lambda x: x in 'None')]
            plt.scatter(area['x'].values, 15-area['y'].values, marker='')
        elif c == 'Apartment':
            area = area_struct[area_struct['type'].map(lambda x: x in ' Apartment ')]
            plt.scatter(area['x'].values, 15-area['y'].values, c='brown', marker='o', label =area_category['struct'][i])
            for x,y in zip(area['x'].values, area['y'].values):
                plt.text(x-0.3, 15-y+0.4, 'A')
        elif c == 'Building':
            area = area_struct[area_struct['type'].map(lambda x: x in ' Building ')]
            plt.scatter(area['x'].values, 15-area['y'].values, c='brown', marker='o', label =area_category['struct'][i])
            for x,y in zip(area['x'].values, area['y'].values):
                plt.text(x-0.3, 15-y+0.4, 'B')
        elif c == 'BandalgomCoffee':
            area = area_struct[area_struct['type'].map(lambda x: x in ' BandalgomCoffee ')]
            plt.scatter(area['x'].values, 15-area['y'].values, c='green', marker='s', label =area_category['struct'][i])
            for x,y in zip(area['x'].values, area['y'].values):
                plt.text(x-0.3, 15-y+0.4, 'BC')
        elif c =='MyHome':
            area = area_struct[area_struct['type'].map(lambda x: x in ' MyHome ')]
            plt.scatter(area['x'].values, 15-area['y'].values, c='green', marker='^', label =area_category['struct'][i])
            for x,y in zip(area['x'].values, area['y'].values):
                plt.text(x-0.5, 15-y+0.4, 'MyHome')

    plt.legend(fontsize=7, loc='lower right')
    plt.grid(True, 'both')
    plt.savefig(save_path, dpi=300)

if __name__=='__main__':
    area_map = pd.read_csv('area_map.csv')
    area_category = pd.read_csv('area_category.csv')
    area_struct = pd.read_csv('area_struct.csv')
    # input 0 category
    area_category.loc[4] = {'category': 0 , 'struct': 'None'}
    main('res/map.png', area_category, area_struct)

