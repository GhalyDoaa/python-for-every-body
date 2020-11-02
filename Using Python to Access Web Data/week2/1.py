"""
Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
"""
import re as regular_exp

#Extracting Data With Regular Expressions
hand = open("regex_sum_55.txt")
numbers_list = []

for line in hand:
    line = line.rstrip()
    extract = regular_exp.findall("([0-9]+)", line)

    if len(extract) < 1 : continue

    for i in range(len(extract)):
        number = float(extract[i])
        numbers_list.append(number)

print(sum(numbers_list))
