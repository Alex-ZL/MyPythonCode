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
	inlist[low]=pivot
	return low

def quick_sort(inlist, low, high):
	idx = 0
	if low<high:
		idx = partition(inlist, low, high)
		quick_sort(inlist, low, idx)
		quick_sort(inlist, idx+1, high)

def Q_sort(inlist):
	high = len(inlist) - 1
	quick_sort(inlist, 0, high)
	return inlist

if __name__ == "__main__":
	t = [ 2, 3, 1, 2, 2, 4, 5, 3, 8 , 7]
	print Q_sort(t)

