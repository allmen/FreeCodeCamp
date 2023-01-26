import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates = ['date'],index_col= "date")

# Clean data
d1 = df["value"] <= df['value'].quantile(0.025)
d2 = df["value"] >= df['value'].quantile(0.975)
f = (d1 | d2)
df = df.drop(index = df[f].index)


def draw_line_plot():
    # Draw line plot
    fig, axs = plt.subplots(figsize=(20, 10))

    fig.set_figwidth(15)
    fig.set_figheight(5)

    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.plot(df.index, df['value'], color='r', linewidth = 1)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df["month"] = df.index.month
    df["year"] = df.index.year
    df_bar = df.groupby(["year", "month"])["value"].mean()
    df_bar = df_bar.unstack()
    # Draw bar plot
    fig = df_bar.plot(kind ="bar", legend = True, figsize = (15,10)).figure
    plt.xlabel("Years", fontsize= 10)
    plt.ylabel("Average Page Views", fontsize= 10)
    #plt.xticks(rotation=30)
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    plt.legend(fontsize = 10, title="Months", labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
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
    
    df_box['smonth'] = [d.strftime('%m')for d in df_box.date]
    
    df_box = df_box.sort_values(by='smonth')
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_figwidth(20)
    fig.set_figheight(10)

    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    ax1 = sns.boxplot(x=df_box.year, y=df_box.value, ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    ax2 = sns.boxplot(x="month", y="value", data=df_box, ax=ax2)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

