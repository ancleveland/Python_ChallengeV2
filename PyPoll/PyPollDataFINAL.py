{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "election_data_csv = os.path.join('Resources', 'election_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_votes = 0\n",
    "Candidates =[]\n",
    "uniqueCandidates = []\n",
    "\n",
    "with open(election_data_csv, newline=\"\") as electiondata:\n",
    "    electiondata = csv.reader(electiondata, delimiter=\",\")\n",
    "    header = next(electiondata)\n",
    "    \n",
    "    for row in electiondata:\n",
    "        total_votes = total_votes + 1\n",
    "        Candidates.append(row[2])\n",
    "        \n",
    "        \n",
    "    \n",
    "    \n",
    "# The total number of votes cast\n",
    "# A complete list of candidates who received votes\n",
    "# The percentage of votes each candidate won\n",
    "# The total number of votes each candidate won\n",
    "# The winner of the election based on popular vote.\n",
    "\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_votes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "for x in Candidates:\n",
    "    if x not in uniqueCandidates:\n",
    "        uniqueCandidates.append(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Khan', 'Correy', 'Li', \"O'Tooley\"]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "uniqueCandidates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "PyPoll = os.path.join('PyPoll', 'Resources', 'election_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "_________________\n",
      "Total Votes: 3521001\n",
      "_________________\n",
      "Kahn: 63.000%  (2218231)\n",
      "Correy: 20.000%  (704200)\n",
      "Li: 14.000%  (492940)\n",
      "Otooley: 3.000%  (105630)\n",
      "___________________\n",
      "Winner: Khan\n",
      "____________________\n"
     ]
    }
   ],
   "source": [
    "with open(election_data_csv, newline=\"\") as electiondata:\n",
    "    electiondata = csv.reader(electiondata, delimiter=\",\")\n",
    "    header = next(electiondata)\n",
    "    file_to_output = \"election_analysis.txt\"\n",
    "    \n",
    "    #variables\n",
    "    TotalVotes = 0\n",
    "    KhanVotes = 0\n",
    "    CorreyVotes = 0\n",
    "    LiVotes = 0\n",
    "    OtooleyVotes = 0\n",
    "    for row in electiondata:\n",
    "    #calculate total votes\n",
    "        TotalVotes += 1\n",
    "    #calculate number of votes for each of the candidates\n",
    "        if (row[2] == \"Khan\"):\n",
    "            KhanVotes += 1\n",
    "        elif (row[2] == \"Correy\"):\n",
    "            CorreyVotes += 1\n",
    "        elif (row[2] == \"Li\"):\n",
    "            LiVotes += 1\n",
    "        else:\n",
    "            OtooleyVotes += 1\n",
    "       #calculate the percentage of times each candidate has won\n",
    "        khan_percent = KhanVotes / TotalVotes\n",
    "        correy_percent = CorreyVotes / TotalVotes\n",
    "        li_percent = LiVotes / TotalVotes\n",
    "        otooley_percent = OtooleyVotes / TotalVotes\n",
    "   #calculate the winner based off of popular votes\n",
    "    winner = max(KhanVotes, CorreyVotes, LiVotes, OtooleyVotes)\n",
    "    if winner == KhanVotes:\n",
    "        winner_name = \"Khan\"\n",
    "    elif winner== CorreyVotes:\n",
    "        winner_name = \"Correy\"\n",
    "    elif winner == LiVotes:\n",
    "        winner_name = \"Li\"\n",
    "    else:\n",
    "        winner_name = \"Otooley\"\n",
    "        \n",
    "#Print results\n",
    "print(f\"Election Results\")\n",
    "print(f\"_________________\")\n",
    "print(f\"Total Votes: {TotalVotes}\")\n",
    "print(f\"_________________\")\n",
    "print(f\"Kahn: {khan_percent:.3%}  ({KhanVotes})\")\n",
    "print(f\"Correy: {correy_percent:.3%}  ({CorreyVotes})\")\n",
    "print(f\"Li: {li_percent:.3%}  ({LiVotes})\")\n",
    "print(f\"Otooley: {otooley_percent:.3%}  ({OtooleyVotes})\")\n",
    "print(f\"___________________\")\n",
    "print(f\"Winner: {winner_name}\")\n",
    "print(f\"____________________\")\n",
    "# Open File Using \"Write\" Mode. Specify The Variable To Hold The Contents\n",
    "\n",
    "with open(file_to_output, \"w\") as txt_file:\n",
    "        txt_file.write(f\"Election Results\\n\")\n",
    "        txt_file.write(f\"---------------------------\\n\")\n",
    "        txt_file.write(f\"Total Votes: {TotalVotes}\\n\")\n",
    "        txt_file.write(f\"---------------------------\\n\")\n",
    "        txt_file.write(f\"Kahn: {khan_percent:.3%}({KhanVotes})\\n\")\n",
    "        txt_file.write(f\"Correy: {correy_percent:.3%}({CorreyVotes})\\n\")\n",
    "        txt_file.write(f\"Li: {li_percent:.3%}({LiVotes})\\n\")\n",
    "        txt_file.write(f\"Otooley: {otooley_percent:.3%}({OtooleyVotes})\\n\")\n",
    "        txt_file.write(f\"---------------------------\\n\")\n",
    "        txt_file.write(f\"Winner: {winner_name}\\n\")\n",
    "        txt_file.write(f\"---------------------------\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "_________________\n",
      "Total Votes: 3521001\n",
      "_________________\n",
      "Kahn: 63.000%  (2218231)\n",
      "Correy: 20.000%  (704200)\n",
      "Li: 14.000%  (492940)\n",
      "Otooley: 3.000%  (105630)\n",
      "___________________\n",
      "Winner: Khan\n",
      "____________________\n"
     ]
    }
   ],
   "source": [
    "#Print results\n",
    "print(f\"Election Results\")\n",
    "print(f\"_________________\")\n",
    "print(f\"Total Votes: {TotalVotes}\")\n",
    "print(f\"_________________\")\n",
    "print(f\"Kahn: {khan_percent:.3%}  ({KhanVotes})\")\n",
    "print(f\"Correy: {correy_percent:.3%}  ({CorreyVotes})\")\n",
    "print(f\"Li: {li_percent:.3%}  ({LiVotes})\")\n",
    "print(f\"Otooley: {otooley_percent:.3%}  ({OtooleyVotes})\")\n",
    "print(f\"___________________\")\n",
    "print(f\"Winner: {winner_name}\")\n",
    "print(f\"____________________\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
