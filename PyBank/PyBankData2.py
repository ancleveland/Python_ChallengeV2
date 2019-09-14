#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


import csv


# In[3]:


budget_data_csv = os.path.join('Resources', 'budget_data.csv')


# In[4]:


#The total number of months included in the dataset

# Lists to store data
Total_Months = 0
Total_Profits = 0
Months = []
change_list = []
Net_Change = []
Maximum_Increase_In_Profit = []
Maximum_Decrease_In_Loss = []


# with open(budget_data.csv, newline="") as budgetfile:
with open(budget_data_csv, newline="") as budgetfile:
    budgetreader = csv.reader(budgetfile, delimiter=",")
  
    header = next(budgetreader)
    firstrow = next(budgetreader)
    prev_net = int(firstrow[1])
    change_list.append(list(zip(Months, Net_Change)))

    for row in budgetreader:
        
        Total_Months = Total_Months + 1
        Total_Profits = Total_Profits + int(row[1]) 
        Total_Change = float(row[1]) - prev_net 
        prev_net = int(row[1]) 
        Net_Change = Net_Change + [Total_Change]
        Avg_NetChange = sum(Net_Change)/len(Net_Change) 
        MIP = max(Net_Change)
        MDP = min(Net_Change)
        Months.append(row[0])
        
       
        

               
#             # Add total months
#             Total_Months.append(row[0])

#             # Add total profits
#             Total_Profits.append(row[1])

# #             # Add total losses
#             Total_Losses.append(row[1])

#             # Add average change in P&L
#             Average_Change_inPandL.append(row[6])

#              # Add maximum increase in P&L
#             Maximum_Increase_In_Profit.append(row[7])

#             # Add maximum decrese in in P&L
#             Maximum_Decrease_In_Loss.append(row[8])


# In[ ]:





# In[5]:


Total_Months


# In[6]:


Total_Profits


# In[7]:


#PreviousValue


# In[8]:


Total_Change


# In[9]:


Avg_NetChange


# In[10]:


MIP 


# In[11]:


MDP


# In[12]:


Months


# In[13]:


min(change_list)


# In[14]:


for x in change_list:
    print(x)


# In[ ]:





# In[ ]:




