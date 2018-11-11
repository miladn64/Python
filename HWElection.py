import os
import csv


election=open("election_data.csv",'r')
data=election.read()
rows=data.split('\n')
file=[]
votes_col=[]
names_col=[]
total=0
votecount=0
candidates=[ ]
file_output = "Poll_results.txt"

for row in rows:
	test=row.split(",")
	file.append(test)
file.pop()	
	
for row in file:
	votes_col.append(row[2])
	names_col.append(row[1])
	
votes_col=votes_col[1:len(votes_col)]
names_col=names_col[1:len(names_col)]

for i in votes_col:
	votecount+=1
	if i not in candidates: 
		candidates.append(i) 
		
#my_dict = {i:votes_col.count(i) for i in votes_col}

from collections import Counter
res = Counter(votes_col)

maximum = max(res, key=res.get)

print("Election Results")
print("------------------------------")
print("Total Votes:" ) 
print( votecount)
print("------------------------------")
for key,value in res.items():
	
	
	print(key,value,(round((value/votecount),2))*100)

print("------------------------------")


	
print ("Winner:" + maximum,res[maximum])


with open(file_output, 'w') as file:
	file.write("Election Results \n")
	file.write("------------------------------------- \n")
	file.write("Total : $" + str(votecount) + "\n")
	file.write("------------------------------------- \n")
	
	for key,value in res.items():
		file.write(key+" "+str(value)+" "+str((round((value/votecount),2))*100)+"\n")
	file.write("------------------------------------- \n")
	file.write("Winner:" +" "+ str(maximum)+str(res[maximum]))



