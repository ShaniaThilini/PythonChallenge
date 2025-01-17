# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

import csv
import os

# Define file paths
file_to_load = "C:\Users\Unagi\OneDrive\Documents\GitHub\PythonChallenge\pybank\Resources\budget_data.csv"
file_to_output = "C:\Users\Unagi\OneDrive\Documents\GitHub\PythonChallenge\pybank\Analysis"

# Initialize variables
total_months = 0
total_net = 0
net_change_list = []
month_list = []

# Read the CSV file
with open(file_to_load, mode='r') as financial_data:
    reader = csv.reader(financial_data)
    
    # Skip the header row
    header = next(reader)
    
    # Extract the first row to initialize tracking variables
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Process each row of data
    for row in reader:
        # Update totals and track changes
        total_months += 1
        total_net += int(row[1])

        # Calculate change and add to list
        net_change = int(row[1]) - previous_net
        net_change_list.append(net_change)
        month_list.append(row[0])

        # Update previous_net
        previous_net = int(row[1])

# Calculate average change
average_change = sum(net_change_list) / len(net_change_list)

# Determine greatest increase and decrease in profits
greatest_increase = max(net_change_list)
greatest_increase_month = month_list[net_change_list.index(greatest_increase)]

greatest_decrease = min(net_change_list)
greatest_decrease_month = month_list[net_change_list.index(greatest_decrease)]

# Generate output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the output to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)




