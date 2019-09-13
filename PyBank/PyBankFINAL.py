{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "budget_data_csv = os.path.join('Resources','budget_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months: 85\n",
      "Total: $37514694\n",
      "Average Change: $3732.809523809524\n",
      "Greatest Increase in Profits: Jan-2012 ($1926159)\n",
      "Greatest Decrease in Profits: Aug-2013 ($-2196167)\n",
      "----------------------------\n"
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
    "\n",
    "with open(budget_data_csv, newline=\"\") as budgetfile:\n",
    "    budgetfile = csv.reader(budgetfile, delimiter=\",\")\n",
    "    header = next(budgetfile)\n",
    "    firstrow = next(budgetfile)\n",
    "    file_to_output = \"budget_analysis.txt\"\n",
    "    \n",
    "    for row in budgetfile:\n",
    "        #total months\n",
    "        TotalMonths = TotalMonths + 1\n",
    "        #total rev\n",
    "        TotalRev = TotalRev + int(row[1])\n",
    "        #rev list\n",
    "        Revenue.append(row[1])\n",
    "        #date list\n",
    "        Date.append(row[0])\n",
    "        \n",
    "#change in Revenue for average, max, and min\n",
    "\n",
    "    for i in range(len(Revenue)-1):\n",
    "        change = int(Revenue[i+1]) - int(Revenue[i])\n",
    "        RevenueChange.append(change)\n",
    "\n",
    "        #Average change in rev b/t months\n",
    "        AvgRevChange = abs(sum(RevenueChange)/len(RevenueChange))\n",
    "        #Max rev change\n",
    "        MaxRevChange = max(RevenueChange)\n",
    "        #Min rev change\n",
    "        MinRevChange = min(RevenueChange)\n",
    "        MaxRevChangeDate = str(Date[RevenueChange.index(max(RevenueChange))])\n",
    "        MinRevChangeDate = str(Date[RevenueChange.index(min(RevenueChange))])\n",
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
    "            txt_file.write(\"Greatest Decrease: \" + str(MinRevChangeDate)+ \" ($\" + str(MinRevChange)+\")\")"
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
