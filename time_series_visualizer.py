import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r"fcc-forum-pageviews.csv", index_col="date")
print(df.head())
# Clean data
df = df[(df["value"] > df["value"].quantile(0.025))
        & (df["value"] < df["value"].quantile(0.975))]
print(df.head())

def draw_line_plot():
    # Draw line plot
    xlabels = [df.index[i][:8] for i in range(10, len(df.index)-10, 150)]
    fig = plt.figure(figsize=(20, 7))
    plt.plot(df.index, df["value"], color="red", figure=fig)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", figure=fig)
    plt.xlabel("Date", labelpad=10, figure=fig)
    plt.xticks(np.arange(10, len(df.index)-10, 150), xlabels)
    plt.ylabel("Page Views", figure=fig)




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
