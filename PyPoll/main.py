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
