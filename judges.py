# -*- coding: utf-8 -*-
"""judges.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AHBsMOpDI7S5v5YXj1rFsem6sFSKntA0
"""

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager
import matplotlib.lines as mlines
 
 
plt.rcParams["font.family"] = "serif"
matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)
 
# figure = plt.figure()
# ax = figure.add_axes([0,0,1,1])
 
from google.colab import files
 
uploaded = files.upload()
 
for fn in uploaded.keys():
 print('User uploaded file "{name}" with length {length} bytes'.format(
     name=fn, length=len(uploaded[fn])))
 
data = pd.read_csv("beatbobbyflay.csv")
column = data.loc[:,"guest1"]
counts = column.value_counts()
 
fig, ax = plt.subplots()
fig.set_size_inches(20,10)
all_judges = counts.index
all_frequency = counts.values
 
judges = []
for i in range(10):
 judges.append(all_judges[i])
frequency = []
for i in range(10):
 frequency.append(all_frequency[i])
 print (frequency[i])
 
ax.bar(judges, frequency, color = "#113a86")
 
ax.set_title("Celebrity Judge Appearances", fontsize = 30)
ax.set_xlabel("Judges", fontsize = 20)
ax.set_ylabel("Frequency", fontsize = 20)
 
fig2, ax2 = plt.subplots()
fig2.set_size_inches(20,10)
 
winner = data.loc[:,"winner"]
success_rate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(10):
 for i in range(306):
   if (column[i]==judges[x] and winner[i]=="Bobby Flay"):
     success_rate[x] += 1
 
for i in range(10):
 success_rate[i] = (success_rate[i] / frequency[i]) * 100;
 print (success_rate[i])
 
ax2.bar(judges, success_rate, color = "#113a86")
ax2.set_title("Celebrity Judge vs Bobby Flay Success Rate", fontsize = 30)
ax2.set_xlabel("Judges", fontsize = 20)
ax2.set_ylabel("Success Rate (%)", fontsize = 20)
 
count = 0.0
for x in winner:
 if (x=="Bobby Flay"):
   count = count + 1
 
plt.axhline(y = (count/306.0)*100, color = '#b82329')
 
y = []
for i in range(10):
 y.append((count/306.0)*100)
 
plt.plot(judges, y, "#b82329", label="overall success rate")
plt.legend(loc="upper left")
 
plt.show()