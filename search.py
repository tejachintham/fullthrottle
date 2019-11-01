import csv
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--value","-q")
args = parser.parse_args()
#input number you want to search
number = args.value

#read csv, and split on "," the line
csv_file = csv.reader(open('C:\\Users\\tejac\\search\\rankingtool\\word.csv'), delimiter=",")

q=[]
#loop through csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if number in  row[0]:
         q.append(row)
orrded=[]
for qq in q:
    temp1=qq[0]
    temp2=qq[1]
    qq[0]=temp2
    qq[1]=temp1
    orrded.append(qq)
orrded.sort()
orrd=[]
for orr in orrded:
    o=len(orr[1])
    orr.append(o)
    orrd.append(orr)
orrd.sort()
orrde=[]
for orr in orrd:
    result = str(orr[1]).find(number)
    l=list(orr)
    l.append(result)
    l.reverse()
    orrde.append(l)
orrde.sort()
ordde=orrde[:25]
la=[]
for orr in orrde: 
    la.append(orr[2])
j={
    "suggestions":la,
}    
print(j)
