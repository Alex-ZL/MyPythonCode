#!/usr/bin/python
##get file names from folder "search_files" by INV_Num in INV_num.txt and store the table in result file.
import os
search_files = os.listdir("search_files")

#Get INV_num from the file "INV_num.txt"
INV_file = open("INV_num.txt","r")

table = []  #table to store the inv num and corresponding filename

for num in INV_file.readlines():
	table.append([num[:-1]])

INV_file.close()

#search files by INV_num, append corresponding file name to table.
for file in search_files:
	search_file = open("search_files/"+file,"r")
	search_string = search_file.read()
	search_file.close()
	for num in table:
		if num[0] in search_string:
			num.append(file)

#output table into result file
result = open("result.txt","a")

for num in table:
	result.write('    '.join(num)+'\n')

result.close()
