import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight']/((df['height']/100)**2)).apply(lambda x:1 if x > 25 else 0)

# 3: Normalize the data by making 0 always good and 1 always bad
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4 Create a DataFrame for the cat plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # 5 Group and reformat the data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset.index(name='total')


    # 6 Draw the catplot
    catplot = sns.catplot(x='variable', y='total', hue ='value', col='cardio', kind='bar', data=df_cat)
    fig = catplot.fig

    # 7



    # 8
   # fig = None


    # 9 Return the figure object for the output
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11 Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025))&
        (df['height'] >= df['height'].quantile(0.975))&
        (df['weight'] >= df['weight'].quantile(0.025))&
        (df['weight'] >= df['weight'].quantile(0.975))
    ]

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
