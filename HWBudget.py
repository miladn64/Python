import os
import csv


budget=open("budget_data.csv",'r')
data=budget.read()
rows=data.split('\n')
file=[]
first_col=[]
second_col=[]
file_output = "Budget_results.txt"

for row in rows:
	test=row.split(",")
	file.append(test)

file.pop()	

for row in file:
	first_col.append(row[0])
	second_col.append(row[1])
	
first_col=first_col[1:len(first_col)]
second_col=second_col[1:len(second_col)]


month_count=0
total=0
changes=0
change=[]
counter=0

for i in first_col:
     month_count+=1
for i in second_col:
	total=total+int(i)
	
for i in range(len(second_col)):
		counter+=1
		prev=second_col[i-1]
		curr=second_col[i]
		changes=int(curr)-int(prev)
		change.append(changes)

change=change[1:]
a=sum(change)  /len(change)
m=max(change)
mi=min(change)
locationmin=change.index(mi)
dates=first_col[locationmin+1]
l=change.index(m)
dateg=first_col[l+1]
avgchange=format(round(a,2))

print("Financial Analysis")
print("------------------------------")
print(f'Total months: {month_count}.')
print(f'Total : ${total}')
print (f'Average Change: ${avgchange}')
print(f'Greatest Increase in profits:{dateg} (${m}).')
print(f'Greatest decrease in profits:{dates} (${mi}).')

with open(file_output, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total : $" + str(total) + "\n")
    file.write("Total Months: " + str(month_count) + "\n")
    file.write("Average Change: $" + str(avgchange) + "\n")
    file.write("Greatest Increase in profits: $ " + str(dateg) +" "+ str(m)+"\n")
    file.write("Greatest decrease in profits: $ " + str(dates) +" "+str(mi)+ "\n")
	
	
	


  


	