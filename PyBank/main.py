import os
import csv

pybankCSV = os.path.join('Resources', 'budget_data.csv')

with open(pybankCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header
    csv_header = next(csvfile)

    #define variables
    totalmonth = 0
    totalnet = 0
    greatest_profits = 0
    greatest_loss = 0
    cal_change = []
    avg_change = []

    for row in csvreader:

        totalmonth += 1
        totalnet += float(row[1])
        cal_change.append(row[1])

        if float(row[1]) > greatest_profits:
            greatest_profits = float(row[1])
            profit_month = row[0]
        
        if float(row[1]) < greatest_loss:
            greatest_loss = float(row[1])
            loss_month = row[0]
    
    for a, b in zip(cal_change[::1],cal_change[1::1]):
        avg_change.append(float(b) - float(a))

    final_avg_change = sum(avg_change) / len(avg_change)


print("Financial Analysis")
print("-------------------------------------------")
print(f'Total Months: '+ str(totalmonth))
print(f'Total: $' + str(int(totalnet)))
print(f'Average Change: $' + str(round(final_avg_change,2)))
print(f'Greatest Increase in Profits: ' + profit_month + ' ($' + str(int(greatest_profits)) + ')')
print(f'Greatest Decrease in Profits: ' + loss_month + ' ($' + str(int(greatest_loss)) + ')')

output_file = os.path.join("output.txt")

with open(output_file, "w", newline = "") as datafile:

    datafile.write("Financial Analysis\n")
    datafile.write("-------------------------------------------\n")
    datafile.write(f'Total Months: '+ str(totalmonth) + '\n')
    datafile.write(f'Total: $' + str(int(totalnet)) + '\n')
    datafile.write(f'Average Change: $' + str(round(final_avg_change,2)) + '\n')
    datafile.write(f'Greatest Increase in Profits: ' + profit_month + ' ($' + str(int(greatest_profits)) + ')\n')
    datafile.write(f'Greatest Decrease in Profits: ' + loss_month + ' ($' + str(int(greatest_loss)) + ')\n')
 