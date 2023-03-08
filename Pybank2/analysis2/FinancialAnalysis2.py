import csv

# Open the CSV file and initialize variables
with open('budget_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader) # skip header row
    months = 0
    net_total = 0
    profit_losses = []
    changes = []
    greatest_increase = ['', 0]
    greatest_decrease = ['', 0]

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Count the number of months in the dataset
        months += 1

        # Calculate the net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1])

        # Add the "Profit/Losses" to the list of all "Profit/Losses"
        profit_losses.append(int(row[1]))

        # Calculate the changes in "Profit/Losses" over the entire period
        if months > 1:
            change = int(row[1]) - profit_losses[months - 2]
            changes.append(change)

            # Determine the greatest increase in profits (date and amount) over the entire period
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change

            # Determine the greatest decrease in profits (date and amount) over the entire period
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change

    # Calculate the average of changes in "Profit/Losses" over the entire period
    average_change = sum(changes) / len(changes)

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
