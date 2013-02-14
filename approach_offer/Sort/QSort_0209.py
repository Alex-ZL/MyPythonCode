#!/usr/bin/python

def partition(inlist, low, high):
	pivot = inlist[low]
	while(low < high):
		while(low < high and pivot<=inlist[high]):
			high -= 1
		inlist[low] = inlist[high]
		while(low < high and pivot>=inlist[low]):
			low += 1
		inlist[high] = inlist[low]
	inlist[low]=pivot
	return low

def quick_sort(inlist, low, high):
	if low<high:
		indx = partition(inlist, low, high)
		quick_sort(inlist, low, indx-1)
		quick_sort(inlist, indx+1, high)

def QSort(inlist):
	high = len(inlist)-1
	quick_sort(inlist, 0, high)
	return inlist

if __name__=="__main__":
	tlist=[12, 1, 2, 2, 4, 5, 3, 9, 5, 6, 4, 32]
	QSort(tlist)
	print tlist
