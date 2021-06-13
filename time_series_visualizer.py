import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r"fcc-forum-pageviews.csv", index_col="date")

# Clean data
df = df[(df["value"] > df["value"].quantile(0.025))
        & (df["value"] < df["value"].quantile(0.975))]

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
    df_bar = df.copy()
    months = {"01":"January", "02":"February", "03":"March", "04":"April", "05":"May", "06":"June", "07":"July", "08":"August", "09":"September", "10":"October", "11":"November", "12":"December"}

    df_bar = df_bar.reset_index()
    df_bar["Months"] = df_bar["date"].apply(lambda row: months[row[5:7]])
    df_bar["Months"] = pd.Categorical(df_bar["Months"], categories=months.values())

    df_bar["year"] = df_bar["date"].apply(lambda row: row[:4])
    df_pivot = pd.pivot_table(df_bar, values="value", index="year", columns="Months", aggfunc=np.mean)

    # Draw bar plot
    ax = df_pivot.plot(kind="bar")
    fig = ax.get_figure()
    fig.set_size_inches(7, 6)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)

    months = {"01":"Jan", "02":"Feb", "03":"Mar", "04":"Apr", "05":"May", "06":"Jun", "07":"Jul", "08":"Aug", "09":"Sep", "10":"Oct", "11":"Nov", "12":"Dec"}

    df_box = df_box.rename(columns={"value":"Page Views"})

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(ncols=2)
 
    sns.set(rc={'figure.figsize':(30,17)})
    sns.set_style("whitegrid")
    fig.tight_layout()
    df_box["Year"] = df_box["date"].apply(lambda row: row[:4])
    df_box = df_box.sort_values(by=["Year"])

    sns.boxplot(x="Year", y="Page Views", data=df_box, ax=ax1).set_title("Year-wise Box Plot (Trend)")



    df_box["Month"] = df_box["date"].apply(lambda row: row[5:7])
    df_box = df_box.sort_values(by=["Month"])
    df_box["Month"] = df_box["Month"].apply(lambda row: months.get(row))

    sns.boxplot(x="Month", y="Page Views", data=df_box, ax=ax2).set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig