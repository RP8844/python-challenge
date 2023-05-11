# Import the files
#Rebeca 05/10/23
import csv
import os

# Path to collect data from the resources file
my_report = open('./analysis/budget_report', 'w')
data = os.path.join('Resources','budget_data.csv')
with open(data) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)
    # Assign the variables
    months = 0
    total = 0
    total_ch = 0
    previous_profit_losses = 0
    greatest_increase_month = ''
    greatest_increase_amount = 0
    greatest_decrease_month = ''
    greatest_decrease_amount = 0

    # Determine the complete number of months and profit/losses
    for row in reader:
        
        # months = months + 1
        months += 1

        profit_losses = int(row[1])  
        total += profit_losses

        # profit losses changes
        change = (profit_losses - previous_profit_losses)
        
        if previous_profit_losses == 0:
            change = 0

        total_ch += change
        previous_profit_losses = profit_losses

        # Greatest increase
        if(change > greatest_increase_amount):
            greatest_increase_amount = change
            greatest_increase_month = row[0]
        
        # Greatest decrease
        if(change < greatest_decrease_amount):
            greatest_decrease_amount = change
            greatest_decrease_month = row [0]
        

    # Determine greatest increase/decrease in profits (date & amount) over entire period  
    # Print the output   
    output = f'''
        Financial Analysis
        ----------------------------
        Total Months: {months}
        Total: ${total:,}
        Average Change: ${total_ch/(months-1):,.2f}
        Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount:,})
        Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount:,})
    '''
    print(output)
    my_report.write(output)