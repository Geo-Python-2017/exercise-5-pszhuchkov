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