import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
overweight_condition = df['weight'] / ((df['height'] / 100) ** 2) > 25
df['overweight'] = np.select([overweight_condition], [1], default=0)

# 3
def good_condtion(num):
    return 1 if num > 1 else 0

df['cholesterol'] = df['cholesterol'].apply(good_condtion)
df['gluc'] = df['gluc'].apply(good_condtion)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6
    df_cat = df_cat.groupby(['variable', 'value', 'cardio'], as_index=False).size().rename(columns={'size': 'total'})
    print(df_cat)
    

    # 7
    sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio')


    # 8
    fig = plt.gcf()


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)


    # 14
    fig, ax = plt.subplots(figsize=(15, 12))

    # 15
    sns.heatmap(corr, annot=True, fmt='.1f', annot_kws={'fontsize': 14}, linewidths=1, mask=mask, square=True, cbar_kws={'shrink': 0.5}, ax=ax, vmin=-0.1, vmax=0.30)


    # 16
    fig.savefig('heatmap.png')
    return fig
