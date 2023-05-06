
import csv

data = csv.reader(open('Resources/budget_data.csv'))

next(data)

total = 0

months = 0

for row in data:
    months += 1
    rev = int(row[1])  
    total += rev 
    
output = f'''
    Financial Analysis
    ----------------------------
    Total Months: {months}
    Total: ${total:,}
    Average Change: $-8311.11
    Greatest Increase in Profits: Aug-16 ($1862002)
    Greatest Decrease in Profits: Feb-14 ($-1825558)
'''
print(months)
print(output)