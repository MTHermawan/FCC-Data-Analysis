import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope_1, y_intercept_1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])[:2]
    year_1 = pd.Series([i for i in range(1880, 2051)])
    plt.plot(year_1, slope_1 * year_1 + y_intercept_1, 'red') 

    # Create second line of best fit
    df_2 = df.loc[df['Year'] >= 2000]
    slope_2, y_intercept_2 = linregress(df_2['Year'], df_2['CSIRO Adjusted Sea Level'])[:2]
    year_2 = pd.Series([i for i in range(2000, 2051)])
    plt.plot(year_2, slope_2 * year_2 + y_intercept_2, 'blue')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()