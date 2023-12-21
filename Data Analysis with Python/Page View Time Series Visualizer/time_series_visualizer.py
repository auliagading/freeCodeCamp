import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[df["value"].between(df["value"].quantile(0.025),
                            df["value"].quantile(.975))]


def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(15, 5))
  ax.plot(df.index, df['value'], c='red')
  ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  ax.set_xlabel('Date')
  ax.set_ylabel('Page Views')

  plt.tight_layout()
  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  
  #df_bar.reset_index(inplace=True)
  #df_bar['year'] = df_bar['date'].dt.year

  df_bar['year'] = df.index.year
  df_bar['month'] = df.index.month
  df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
  df_bar = df_bar.unstack()
  
  Months = [
      'January', 'February', 'March', 'April',
      'May', 'June', 'July', 'August',
      'September', 'October', 'November', 'December'
  ]

  # Draw bar plot
  fig, ax = plt.subplots(figsize=(10,10))
  df_bar.plot.bar(ax=ax, legend=True)
  ax.set_xlabel('Years')
  ax.set_ylabel('Average Page Views')
  ax.legend(Months, title='Months', loc='best')

  plt.tight_layout()
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
  df_box['monthnum'] = df.index.month
  df_box = df_box.sort_values('monthnum')
  fig, ax = plt.subplots(1, 2, figsize=(15, 5))
  sns.boxplot(x='year', y='value', data=df_box, ax=ax[0], palette='tab10', flierprops={'marker': 'd', 'mfc':'black'}, fliersize=3)
  ax[0].set(xlabel="Year",
            ylabel="Page Views",
            title="Year-wise Box Plot (Trend)")
  sns.boxplot(x='month', y='value', data=df_box, ax=ax[1], palette='husl', flierprops={'marker': 'd', 'mfc':'black'}, fliersize=3)
  ax[1].set(xlabel="Month",
            ylabel="Page Views",
            title="Month-wise Box Plot (Seasonality)")
  plt.tight_layout()
  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
