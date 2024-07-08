import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('/Users/pernebayarailym/Documents/Portfolio Projects AP/Python Projects/Project_17_FreeCodeCamp/Pr_5_Sea Level Predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points', color='orange')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    #Predict sea level trough 2050
    year_extended=pd.Series(range(1880, 2051))
    sea_level_pred=slope*year_extended+intercept

    #Plot the first line of the best fit
    plt.plot(year_extended, sea_level_pred, label='Best Fit Line 1880-2050', color='red')


    # Create second line of best fit
    recent_df=df[df['Year']>=2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent=linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])

    #Predict sea level trough 2050 using the recent trend
    year_extended_recent = pd.Series(range(2000, 2051)) 
    sea_level_pred_recent=slope_recent*year_extended_recent+intercept_recent

    #Plot the second line of the best fit
    plt.plot(year_extended_recent, sea_level_pred_recent, label='Best Fit Line 2000-2050', color='green')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()