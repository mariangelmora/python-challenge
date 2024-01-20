import csv

#read csv file
csvpath = os.path.join(r"C:\Users\maria\Desktop\Bootcamp\python\Python challenge\Starter_Code\PyBank\Resources\budget_data.csv")

#open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #store header
    csv_header = next(csvreader)
    #print header
    print(f'CSV Header: {csv_header}')

    # Initialize variables
    #keep track of the values
    total_months = 0
    net_total = 0
    profit_loss_info = 0
    
    #empty lists to add values
    changes = []
    dates = []

    #Iterate through each row
    for i in csvreader:
        
        # Extract date and profit/loss information
        date = i[0]
        profit_losses = int(i[1])

        # Update total months and net total
        total_months += 1
        net_total += profit_losses
        
        # Calculate and store the change in profit/loss
        if total_months > 1:
            change = profit_losses - profit_loss_info
            changes.append(change)
            dates.append(date)
        
        # Update profit/loss for the next iteration
        profit_loss_info = profit_losses

print("Financial Analysis")
print("------------------")      
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")

# Calculate the average change
average_change = sum(changes) / len(changes)
print(f"Average Change: ${average_change:.2f}")

#calculate the greatest increase 
max_increase = max(changes)
max_increase_date = dates[changes.index(max_increase)]
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")

#calculate the greatest decrease
max_decrease = min(changes)
max_decrease_date = dates[changes.index(max_decrease)]
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")
