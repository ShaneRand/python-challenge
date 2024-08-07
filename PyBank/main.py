# Import modules os and csv
import os
import csv
 
# Define variables
months = []
month_count = 0
pnl_change = []
net_pnl = 0
prev_month_pnl = 0
curr_month_pnl = 0
 
# Path for file from resource folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")
 
# Open and read csv file
with open(budget_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # First row
    csv_header = next(csv_reader)
    # print(f"Header: {csv_header}")
 
    # Read through rows
    for row in csv_reader:
        # Count the months
        month_count += 1
        # PnL over period
        curr_month_pnl = int(row[1])
        net_pnl += curr_month_pnl
        if (month_count == 1):
            # make the prev month equal to current month
            prev_month_pnl = curr_month_pnl
            continue
        else:
            # PnL change
            pnl = curr_month_pnl - prev_month_pnl
            # add each month to the months variable
            months.append(row[0])
            # add each PnL to the PnL change
            pnl_change.append(pnl)
            # Next loop for current pnl equal to prev pnl
            prev_month_pnl = curr_month_pnl
 
# Add and find avg for PnL changes
sum_pnl = sum(pnl_change)
avg_pnl = round(sum_pnl/(month_count - 1), 2)
 
# largest and smallest MoM change
max_change = max(pnl_change)
min_change = min(pnl_change)
 
# find largest and smallest MoM change
max_month = pnl_change.index(max_change)
min_month = pnl_change.index(min_change)
 
# Match max and min months
best_month = months[max_month]
worst_month = months[min_month]
 
# Print Analysis
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_pnl}")
print(f"Average Change: ${avg_pnl}")
print(f"Greatest Increase in Profits: {best_month} (${max_change})")
print(f"Greatest Decrease in Profits: {worst_month} (${min_change})")

# Write Analysis to text file
output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("--------------------\n")
    txtfile.write(f"Total Months: {month_count}\n")
    txtfile.write(f"Total: ${net_pnl}\n")
    txtfile.write(f"Average Change: ${avg_pnl}\n")
    txtfile.write(f"Greatest Increase in Profits: {best_month} (${max_change})\n")
    txtfile.write(f"Greatest Decrease in Profits: {worst_month} (${min_change})\n")
print(f"\nResults have been written to {output_path}")



