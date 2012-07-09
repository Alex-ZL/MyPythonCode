#!/usr/bin/python
## A file handling script, including functions that could search file by key
## and rename file by appending key value to the file names.

import os
import shutil
import copy

def get_INV_list(key_file):
	""" read key_file and get key values into list"""
	INV_file = open(key_file, 'r')
	key_list = []
	
	for num in INV_file.readlines():
		key_list.append([num[:-1]])
	
	INV_file.close()
	return key_list

def write_result_list(key_list,out_file):
	"""write updated key_list with reference into a file"""
	result = open(out_file,'w')

	for key in key_list:
		result.write('########'.join(key)+'\n')
	
	result.close()

def search(key_list,search_dir):
	"""search key value in all files in search directory,
	   return a list with key reflect file name"""
	
	##my original workaround
    #result_list = []
	#for item in key_list:
	#	result_list.append(item[:])
	##A simpler code
	#result_list = [item[:] for item in key_list]
	## or 
	#result_list = [list(item) for item in key_list]
	#best solution is copy.deepcopy()
	result_list = copy.deepcopy(key_list)
	
	for file in os.listdir(search_dir):
		search_file = open(search_dir+'/'+file,'r')
		search_str = search_file.read()
		search_file.close()
		for key in result_list:
			if key[0] == search_str[86:92]:    ##only check INV#
			#if key[0] in search_str:
				key.append(file)
	
	return result_list

def rename(result_list,input_dir,output_dir):
	""" rename files in input directory and move to output directory,
	    return a list of file names those not moved."""
	for item in result_list:
		if len(item) > 1:
			for filename in item[1:]:
				# move files to another folder and rename them
				# name format could be modified if necessary
				shutil.move(input_dir+'/'+filename,
						output_dir+'/'+filename+'.NZ'+item[0])

	return os.listdir(input_dir)

xlist = get_INV_list('INV_Num')
ylist = search(xlist,'InputFiles')
rest_list = rename(ylist,'InputFiles','OutputFiles')
write_result_list(ylist,'resultList')
