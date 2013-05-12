#!/usr/bin/python

def partition(inlist, low, high):
	pivote = inlist[low]
	while(high > low):
		while(pivote<=inlist[high] and high > low): high-=1;
		inlist[low] = inlist[high]
		while(pivote>=inlist[low] and high > low): low+=1;
		inlist[high] = inlist[low]
	inlist[low] = pivote
	return low
	
def quick_sort(inlist, low, high):
	if (low<high):
		index = partition(inlist, low, high)
		quick_sort(inlist, low, index-1)
		quick_sort(inlist, index+1, high)

def Qsort(inlist):
	quick_sort(inlist, 0, len(inlist)-1)
	return inlist

if __name__=="__main__":
	t = [4, 3, 2, 6, 5, 1, 5, 7]
	print Qsort(t)
