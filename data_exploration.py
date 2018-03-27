# -*- coding: utf-8 -*-
"""
The script presents some information about the input csv file.

Author: Pavel Zhuchkov - 27.03.2018
"""
# Import Pandas library
import pandas as pd

# Read the csv file
data = pd.read_csv('6153237444115dat.csv', na_values=['*', '**', '***', '****', '*****', '******'])

# How many rows is there in the data?
print('The number of rows is',len(data))

# What are the datatypes of the columns?
print('\nThe datatypes of columns:')
print(data.dtypes)

# What is the mean Fahrenheit temperature in the data? (TEMP column)
print('\nThe mean Fahrenheit temperature is',round(data['TEMP'].mean(),3))

# What is the standard deviation of the Maximum temperature? (MAX column)
print('\nThe standard deviation of the Maximum temperatures is',round(data['MAX'].std(),3))

# How many unique stations exists in the data? (USAF column)
print('\nThe amount of the unique stations is',len(data['USAF'].unique()))

# Select columns
selected = data[['USAF','YR--MODAHRMN','TEMP','MAX','MIN']]

# Remove all rows from selected that has NoData in column TEMP
selected = selected.dropna(subset=['TEMP'])

# Convert the Fahrenheit temperatures from TEMP into a new column Celsius
# Round the values in Celsius to have 0 decimals
# Convert the Celsius values into integers
selected['Celsius'] = ((selected['TEMP'] - 32) / 1.8).round(0).astype(int)

# Output result
print(selected)

