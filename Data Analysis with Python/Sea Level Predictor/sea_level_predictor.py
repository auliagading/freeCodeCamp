import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, _,_,_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series(range(min(df['Year']), 2051))
    y = intercept + slope * x
    ax.plot(x, y, c='r', label='First Line of Best Fit')
    
    # Create second line of best fit
    df1 = df.loc[df['Year'] >= 2000]
    slope, intercept, _,_,_ = linregress(df1['Year'], df1['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(min(df1['Year']), 2051))
    y1 = intercept + slope * x1
    ax.plot(x1, y1, c='b', label='Second Line of Best Fit')
    
    # Add labels and title
    ax.set(xlabel='Year', ylabel='Sea Level (inches)', title='Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()