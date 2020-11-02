'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
'''

﻿# Use the file name mbox-short.txt as the file name
file_name = input("Enter file name: ")
file_handler = open(file_name)
_sum=0
_count=0
for line in file_handler:
    
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line)
    _count+=1
    _conf_number_as_string = line.find ('0')
    _conf_number_as_string=line[_conf_number_as_string:]
    #convert to number 
    _conf_number_as_number=float(_conf_number_as_string)
    _sum=_sum+_conf_number_as_number
    #print(_conf_number_as_number)
    
    
result=_sum/_count 
#print("Done")
print("Average spam confidence:",result)
