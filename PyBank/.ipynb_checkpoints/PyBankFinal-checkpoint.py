{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "budget_data_csv = os.path.join('Resources','budget_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(budget_data_csv, newline=\"\") as budgetfile:\n",
    "    budgetreader = csv.reader(budgetfile, delimiter=\",\")\n",
    "    header = next(budgetreader)\n",
    "    firstrow = next(budgetreader)\n",
    "    file_to_output = \"budget_analysis.txt\"\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-67-ef51acb2497a>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0mDate\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 15\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mbudgetreader\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     16\u001b[0m     \u001b[0;31m#total months\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     17\u001b[0m     \u001b[0mTotalMonths\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mTotalMonths\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "#setting values\n",
    "\n",
    "TotalRev = 0\n",
    "TotalMonths = 0\n",
    "LengthRev = 0\n",
    "AvgRevChange = 0\n",
    "MaxRevChange = 0\n",
    "MinRevChange = 0\n",
    "MaxRevChangeDate = None\n",
    "MinRevChangeDate = None\n",
    "Revenue = []\n",
    "RevenueChange = []\n",
    "Date = []\n",
    "   \n",
    "for row in budgetreader:\n",
    "    #total months\n",
    "    TotalMonths = TotalMonths + 1\n",
    "    #total rev\n",
    "    TotalRev = TotalRev + int(row[1])\n",
    "    #rev list\n",
    "    Revenue.append(row[1])\n",
    "    #date list\n",
    "    Date.append(row[0])\n",
    "        \n",
    "#change in Revenue for average, max, and min\n",
    "\n",
    "for i in range(len(Revenue)-1):\n",
    "    change = int(Revenue[i+1]) - int(Revenue[i])\n",
    "    RevenueChange.append(change)\n",
    "        \n",
    "    #Average change in rev b/t months\n",
    "    AvgRevChange = abs(sum(RevenueChange)/len(RevenueChange))\n",
    "    #Max rev change\n",
    "    MaxRevChange = max(RevenueChange)\n",
    "    #Min rev change\n",
    "    MinRevChange = min(RevenueChange)\n",
    "    MaxRevChangeDate = str(Date[RevenueChange.index(max(RevenueChange))])\n",
    "    MinRevChangeDate = str(Date[RevenueChange.index(min(RevenueChange))])\n",
    "\n",
    "    \n",
    "#print outputs\n",
    "print(\"Financial Analysis\")\n",
    "print(\"----------------------------\")\n",
    "    \n",
    "print(\"Total Months: \" + str(TotalMonths))\n",
    "print(\"Total: \" + \"$\" + str(TotalRev))\n",
    "print(\"Average Change: \" + \"$\" + str(AvgRevChange))\n",
    "print(\"Greatest Increase in Profits: \" + str(MaxRevChangeDate)+ \" ($\" + str(MaxRevChange) +\")\")\n",
    "print(\"Greatest Decrease in Profits: \" + str(MinRevChangeDate)+ \" ($\" + str(MinRevChange) +\")\")\n",
    "    \n",
    "print(\"----------------------------\")\n",
    "\n",
    "with open(file_to_output, \"w\") as txt_file:\n",
    "            txt_file.write(\"Total Months: \" + str(TotalMonths))\n",
    "            txt_file.write(\"Total Revenue: \" + \"$\" + str(TotalRev))\n",
    "            txt_file.write(\"Average Change: \" + \"$\" + str(AvgRevChange))\n",
    "            txt_file.write(\"Greatest Increase: \" + str(MaxRevChangeDate)+ \" ($\" + str(MaxRevChange) +\")\")\n",
    "            txt_file.write(\"Greatest Decrease: \" + str(MinRevChangeDate)+ \" ($\" + str(MinRevChange)+\")\")\n",
    "\n"
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
