import pandas as pd

def pri():

    struct_category = pd.read_csv('3-1-area_category.csv')
    area_struct = pd.read_csv('3-1-area_struct.csv')
    area_map = pd.read_csv('3-1-area_map.csv')


    return print(struct_category, area_struct, area_map)

def summ():
    struct_category = pd.read_csv('3-1-area_category.csv')
    area_struct = pd.read_csv('3-1-area_struct.csv')
    area_map = pd.read_csv('3-1-area_map.csv')


    merged = pd.merge(area_struct, struct_category, on='category')
    mergg = pd.merge(area_map, merged,on = ['x','y'])

    return print(mergg)

def cate():
    df = pd.read_csv('3-1-area_struct.csv')
    are = df[df['area']== 1 ]

    return print(are)

pri()
summ()
cate()
