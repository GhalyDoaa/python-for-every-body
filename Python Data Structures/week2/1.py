"""
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.

"""
﻿# use words.txt as the file name
fname = input("Enter file name: ")
file_handler = open(fname)
line = file_handler.read()
print(line.upper().rstrip())
