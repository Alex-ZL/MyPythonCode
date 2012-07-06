#!/usr/bin/python
## rename files by appending INV_Num to the file name
import os
import shutil

#Get all source file names
#source_files = os.listdir("HP_NZ")

#Get INV_num from the file "INV_Num"
INV_file = open("INV_Num", "r")
table = []
INV_list = []
x_list = []

for num in INV_file.readlines():
	INV_list.append(num)

INV_excluded_list = INV_list[:]

print len(INV_list)
for num in INV_list:
	for file in os.listdir("HP_NZ"):
		source_file = open("HP_NZ/"+file,"r")
		str = source_file.read()
		x_list.append(str[86:92])
		if num[:-1] == str[86:92]:
			shutil.copy2('HP_NZ/'+file,'rename_files/'+file+'.NZ'+num)
			os.remove('HP_NZ/'+file)
			table.append('HP_NZ/' + file + "###############" + 'rename_files/' + file + '.NZ' + num)
			print num
			if INV_excluded_list.count(num):
				INV_excluded_list.remove(num)
		source_file.close()

INV_file.close()
print len(INV_excluded_list)
print len(table)

list_file = open('list','w')
for item in table:
	list_file.write(item)

INV_excluded = open('excluded_INV','w')
for item in INV_excluded_list:
	INV_excluded.write(item)

INV_excluded.close()

list_file.close()
