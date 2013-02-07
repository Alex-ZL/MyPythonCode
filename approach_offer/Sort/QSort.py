#!/usr/bin/python

def partition(inlist, low, high):
	pivot = inlist[low]
	while(low<high):
		while(low<high and inlist[high]>=pivot):
			high -= 1
		inlist[low] = inlist[high]
		while(low<high and inlist[low]<=pivot):
			low += 1
		inlist[high] = inlist[low]
	inlist[low] = pivot
	return low

def quick_sort(inlist, low, high):
	idex = partition(inlist, low, high)
	if(low<high):
		quick_sort(inlist, low, idex-1)
		quick_sort(inlist, idex+1, high)

def QSort(inlist):
	high = len(inlist)-1
	quick_sort(inlist, 0, high)

if __name__=="__main__":
	import datetime
	tlist = [2, 3, 1, 2, 4, 5, 3, 6, 7, 8, 9, 3]
	print datetime.datetime.now()
	QSort(tlist)
	print datetime.datetime.now()
	print tlist
