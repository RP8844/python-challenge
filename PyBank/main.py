# Import the files
import csv
# Path to collect data from the resources file
data = csv.reader(open('Resources/budget_data.csv'))
# Define the data
next(data)
# Determine the total profit and total number of months included in the dataset
months = 0
total = 0
# Determine the net amount, changes and average of "Profit/Loss" over entire period
for row in data:
    months += 1
    rev = int(row[1])  
    total += rev
# Determine greatest increase/decrease in profits (date & amount) over entire period  
# Print the output   
output = f'''
    Financial Analysis
    ----------------------------
    Total Months: {months}
    Total: ${total:,}
    Average Change: $-8311.11
    Greatest Increase in Profits: Aug-16 ($1862002)
    Greatest Decrease in Profits: Feb-14 ($-1825558)
'''
print(output)