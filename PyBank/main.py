import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

import os
import csv
filepath = os.path.join("..", "PyBank","budget_data.csv")
with open("budget_data.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csv_reader)
    file_to_output = "budget_analysis.txt"
#setting values
    TotalRev = 0
    TotalMonths = 0
    LengthRev = 0
    AvgRevChange = 0
    MaxRevChange = 0
    MinRevChange = 0
    MaxRevChangeDate = None
    MinRevChangeDate = None
    Revenue = []
    RevenueChange = []
    Date = []
    for row in csv_reader:
        #total months
        TotalMonths = TotalMonths + 1
        #total rev
        TotalRev = TotalRev + int(row[1])
        #rev list
        Revenue.append(row[1])
        #date list
        Date.append(row[0])
#change in Revenue for average, max, and min
    for i in range(len(Revenue)-1):
        change = int(Revenue[i+1]) - int(Revenue[i])
        RevenueChange.append(change)
        
    #Average change in rev b/t months
    AvgRevChange = abs(sum(RevenueChange)/len(RevenueChange))
    #Max rev change
    MaxRevChange = max(RevenueChange)
    #Min rev change
    MinRevChange = min(RevenueChange)
    MaxRevChangeDate = str(Date[RevenueChange.index(max(RevenueChange))])
    MinRevChangeDate = str(Date[RevenueChange.index(min(RevenueChange))])
    #print outputs
    print("Financial Analysis")
    print("----------------------------")
    
    print("Total Months: " + str(TotalMonths))
    print("Total: " + "$" + str(TotalRev))
    print("Average Change: " + "$" + str(AvgRevChange))
    print("Greatest Increase in Profits: " + str(MaxRevChangeDate)+ " ($" + str(MaxRevChange) +")")
    print("Greatest Decrease in Profits: " + str(MinRevChangeDate)+ " ($" + str(MinRevChange) +")")
    
    print("----------------------------")
with open(file_to_output, "w") as txt_file:
   txt_file.write("Total Months: " + str(TotalMonths))
   txt_file.write("Total Revenue: " + "$" + str(TotalRev))
   txt_file.write("Average Change: " + "$" + str(AvgRevChange))
   txt_file.write("Greatest Increase: " + str(MaxRevChangeDate)+ " ($" + str(MaxRevChange) +")")
   txt_file.write("Greatest Decrease: " + str(MinRevChangeDate)+ " ($" + str(MinRevChange)+")")
