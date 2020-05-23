# Import to enable interaction for operating system and file type
import os
import csv
from pathlib import Path

# Add csv path
csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Rescources', 'budget_data.csv')

# Set starting variables
g_inc = 0
g_inc_month = 0
g_dec = 0
g_dec_month = 0

# Open csv
with open(csvpath, newline='') as csvfile:

    # Read csv
    csvreader = csv.reader(csvfile, delimiter=',')

    # Don't include header in counts
    header = next(csvreader)

    # Create empty lists to store values
    tot_months = []
    monthly_chg = []
    net_gain = []

    # DETERMINE TOTAL NUMBER MONTHS IN DATASET AND TOTAL PROFIT/LOSS
    for row in csvreader:
        tot_months.append(row[0])
        net_gain.append(int(row[1]))

    # DETERMINE MONTHLY CHANGES
    for i in range(len(net_gain)-1):
        # Use current cell and append to take current and subtract previous
        monthly_chg.append(net_gain[i+1]-net_gain[i])

    # Average monthly change
    avg_chg = sum(monthly_chg)/ len(monthly_chg)

# DETERMINE GREATEST INCREASE AND DECREASE OF MONTHLY PROFIT/LOSS
g_inc = max(monthly_chg)
g_dec = min(monthly_chg)

# Tie g_inc and g_dec to corresponding month of occurence
g_inc_month = monthly_chg.index(max(monthly_chg)) + 1
g_idec_month = monthly_chg.index(min(monthly_chg)) + 1

# PRINT ANALYSIS
print("Financial Analysis")
print("------------------------------------------------------------------------------")
print(f"Total Months: {len(tot_months)}")
print(f"Total: ${sum(net_gain)}")
print(f"Average Change: {str(avg_chg)}")
print(f"Greatest Increase in Profits: {tot_months[g_inc_month]} (${(str(g_inc))})")
print(f"Greatest Decrease in Profits: {tot_months[g_dec_month]} (${(str(g_dec))})")

# EXPORT TEXT 

# Create file path
output = os.path.join(".", 'output.txt')
with open(output,"w") as PyBank:

    # Write txt
    PyBank.write(f"Financial Analysis\n")
    PyBank.write(f"------------------------------------------------------------------------------")
    PyBank.write(f"Total Months: {len(tot_months)}\n")
    PyBank.write(f"Total: ${sum(net_gain)}\n")
    PyBank.write(f"Average Change: {str(avg_chg)}\n")
    PyBank.write(f"Greatest Increase in Profits: {tot_months[g_inc_month]} (${(str(g_inc))})\n")
    PyBank.write(f"Greatest Decrease in Profits: {tot_months[g_dec_month]} (${(str(g_dec))})\n")
