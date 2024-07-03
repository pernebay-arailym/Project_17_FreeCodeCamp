import pandas as pd
import os

def calculate_demographic_data(print_data=True):
    script_dir = os.path.dirname(__file__)
    
    # Construct the full path to the CSV file
    file_path = os.path.join(script_dir, 'adult.data.csv')

    # Read data from file
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ]
    df = pd.read_csv(file_path, header=None, names=column_names)

        # Ensure relevant columns are numeric
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['hours-per-week'] = pd.to_numeric(df['hours-per-week'], errors='coerce')

    # Strip spaces from 'salary' and other string columns for consistent comparison
    df['salary'] = df['salary'].str.strip()
    df['native-country'] = df['native-country'].str.strip()
    df['education'] = df['education'].str.strip()
    df['sex'] = df['sex'].str.strip()

    # Clean any row where 'race' column contains non-race data
    if 'race' in df['race'].unique():
        df = df[df['race'] != 'race']

    # Debug: Print unique values in the race column to ensure correctness
    print("Unique races:", df['race'].unique())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean()*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education
    print(df)
    # percentage with salary >50K
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean()*100, 1)
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean()*100, 1)

    # Debug: Print to verify higher and lower education rich percentages
    print("Percentage with higher education earning >50K:", higher_education_rich)
    print("Percentage without higher education earning >50K:", lower_education_rich)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    # Debug: Print to verify min_work_hours calculation
    print("Minimum work hours:", min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round((num_min_workers['salary'] == '>50K').mean()*100, 1)

    # What country has the highest percentage of people that earn >50K?
    countries = df['native-country'].value_counts()
    rich_countries = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country_percentage = round((rich_countries/countries*100).max(), 1)
    highest_earning_country = (rich_countries/countries*100).idxmax()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }