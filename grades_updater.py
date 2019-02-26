#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import os
import csv
import pandas
import re
import pprint

###select exact one tab file
while True:
    count=0
    for filename in os.listdir():
        
        if filename.endswith(".tab"):
            tab_name=filename
            count+=1
    if count!=1:
        print("too much or no tab files in the current directory,add exaxt one tab file and input anything to continue")
        x=input()
    else:
        break
    #print(1)
        
#print(tab_name)

with open(tab_name,"r") as file:
    record_list = list(csv.reader(file, dialect='excel', delimiter='\t'))
    
for i in record_list:
    if i[2]=='':
        i[2]='0'
    if len(i)<4:
        i.append('')
#print(record_list)

while True:

    #get input
    print("Input part of UID or part of name to search the records. \n Enter save to save, check or exit. CHECK WILL NOT SAVE ANY DATA")
    #print(record_list[0])

    #some treatment for input to make sure it is valid.
    pattern=input().upper()
    ###### some if stament need to wriiten
    #print(pattern)
    if(pattern=='SAVE'):
        print('Modification has been updated')
        try:
            output = open(tab_name,'w')
        except IOError:
            print('IOError')
        else:
            with output:
                N=len(record_list)
                temp=list(range(N))
                for i in range(N):
                    temp[i]='\t'.join(record_list[i])
                #print(record_list)
                content='\n'.join(temp)
                #print (content)
                output.write(content)       
        continue
    
    if(pattern=='CHECK'):
        N=len(record_list)
        temp=list(range(N))
        for i in range(N):
            temp[i]='\t'.join(record_list[i])
        #print(record_list)
        content='\n'.join(temp)
        print(content)
        continue
    
    if(pattern=='EXIT'):
        break

    #funtion is used to filter valid records in recorinput
    def l_match(record):
        assert len(record)==3 or len(record)==4, "Record is wrong"
        prog = re.compile(pattern)
        for i in record:
            if prog.search(i):
                return True

        return False
    #print(l_match(record_list[0]))

    result=list(filter(l_match,record_list))
    for i in result:
        print(i)

    # make sure finally there is exactly one record match
    if len(result)>1:
        print('Too many records. Please narrow down the seach.')
        continue
    if len(result)==0:
        print('No records are found')
        continue
    assert len(result)==1

    print('Input grades between 0-100')
    grade=input()

    # make sure the input is of correct format
    if not(grade.isdigit() and (len(grade)<3) or grade=='100'):
        print('Wrong input')
        continue

    idx=record_list.index(result[0])
    record_list[idx][2]=grade
    if len(record_list[idx])==3:
        record_list[idx].append("")
    print(record_list[idx])

