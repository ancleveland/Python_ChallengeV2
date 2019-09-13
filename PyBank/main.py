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
#PYPOLL!!!!!
import os
import csv
PyPoll = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
#open csv file
with open("election_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    file_to_output = "election_analysis.txt"
    
    #variables
    TotalVotes = 0
    KhanVotes = 0
    CorreyVotes = 0
    LiVotes = 0
    OtooleyVotes = 0
    for row in csvreader:
    #calculate total votes
        TotalVotes += 1
    #calculate number of votes for each of the candidates
        if (row[2] == "Khan"):
            KhanVotes += 1
        elif (row[2] == "Correy"):
            CorreyVotes += 1
        elif (row[2] == "Li"):
            LiVotes += 1
        else:
            OtooleyVotes += 1
       #calculate the percentage of times each candidate has won
        khan_percent = KhanVotes / TotalVotes
        correy_percent = CorreyVotes / TotalVotes
        li_percent = LiVotes / TotalVotes
        otooley_percent = OtooleyVotes / TotalVotes
   #calculate the winner based off of popular votes
    winner = max(KhanVotes, CorreyVotes, LiVotes, OtooleyVotes)
    if winner == KhanVotes:
        winner_name = "Khan"
    elif winner== CorreyVotes:
        winner_name = "Correy"
    elif winner == LiVotes:
        winner_name = "Li"
    else:
        winner_name = "Otooley"
#Print results
print(f"Election Results")
print(f"_________________")
print(f"Total Votes: {TotalVotes}")
print(f"_________________")
print(f"Kahn: {khan_percent:.3%}  ({KhanVotes})")
print(f"Correy: {correy_percent:.3%}  ({CorreyVotes})")
print(f"Li: {li_percent:.3%}  ({LiVotes})")
print(f"Otooley: {otooley_percent:.3%}  ({OtooleyVotes})")
print(f"___________________")
print(f"Winner: {winner_name}")
print(f"____________________")
# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write(f"---------------------------\n")
    txt_file.write(f"Total Votes: {TotalVotes}\n")
    txt_file.write(f"---------------------------\n")
    txt_file.write(f"Kahn: {khan_percent:.3%}({KhanVotes})\n")
    txt_file.write(f"Correy: {correy_percent:.3%}({CorreyVotes})\n")
    txt_file.write(f"Li: {li_percent:.3%}({LiVotes})\n")
    txt_file.write(f"Otooley: {otooley_percent:.3%}({OtooleyVotes})\n")
    txt_file.write(f"---------------------------\n")
    txt_file.write(f"Winner: {winner_name}\n")
    txt_file.write(f"---------------------------\n")
