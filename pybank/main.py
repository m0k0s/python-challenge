# pybank
# Dependencies
import pandas as pd
import numpy as np
# Choose csv file
budget = 'budget_data_2.csv'
text_file = 'pybank.txt'
# Look at data using pandas
budget_df = pd.read_csv(budget, low_memory= True)
budget_df.head()
# Find range of data
print(budget_df.index.unique)
# Change object type of date column to datetime
budget_df.rename(columns={(2): ''}, inplace=True)
budget_df.head()
budget_df.tail()
# Make sure date column object type is changed to datetime
budget_df.dtypes
# Convert object to timestamp for easier math
ts = pd. to_datetime('1/1/2009')
budget_df.head()
#Calculate timedelta
td = budget_df.Date.max() - budget_df.Date.min()
# Gather basic stats on Revenue column
maxrev = budget_df['Revenue'].max()
print(maxrev)
minrev = budget_df['Revenue'].min()
print(minrev)
avgrev = budget_df['Revenue'].mean()
print(avgrev)
sumrev = budget_df['Revenue'].sum()
print(sumrev)
#Create new column for Monthly Revenue Change
budget_df['revdelta'] = revdelta = budget_df['Revenue'].diff().shift(-1)
# Find greatest increase in revenue over 1 month period
incr = budget_df[budget_df.revdelta == (revdelta.max())]
print(incr)
#and decrease in revenue over 1 month period
decr = budget_df[budget_df.revdelta == (revdelta.min())]
print(decr)
#and average
avgrevchange = revdelta.mean()
print(avgrevchange)
#Check out the revdeltas
budget_df.head()
# Textfile with this info 
#(1) total number of months, (2) total amount of revenue, (3) average monthly revenue change, 
#(4) greatest increase in revenue (date and amount), (5) greatest decrease in revenue 


with open("pybank.txt", "w") as text_file:
    print(f"Total Months: {td_mon}", f"Total Revenue: {sumrev}", f"Average Monthly Change in Revenue: {avgrevchange}", 
          f"Greatest Increase in Monthly Revenue: {incr}", 
          f"Greatest Decrease in Monthly Revenue: {decr}", file=text_file)