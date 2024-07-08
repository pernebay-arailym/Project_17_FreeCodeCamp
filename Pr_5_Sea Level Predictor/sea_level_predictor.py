import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('Users/pernebayarailym/Documents/Portfolio Projects AP/Python Projects/Project_17_FreeCodeCamp/Pr_5_Sea Level Predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points', color='blue')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_r = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    #Predict sea level trough 2050
    year_extended=pd.Series(range(1880, 2051))
    sea_level_pred=slope*year_extended+intercept



    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()