#!/usr/bin/python
def quick_sort(inlist, low, high):
	pivot = inlist[low]
	org_low = low
	org_high = high
	while(low<high):
		while(low<high and pivot<=inlist[high]):
			high -= 1
		inlist[low] = inlist[high]
		while(low<high and pivot>=inlist[low]):
			low += 1
		inlist[high] = inlist[low]
		inlist[low] = pivot
	indx = low
	if(org_low<org_high):
		quick_sort(inlist, org_low, indx-1)
		quick_sort(inlist, indx+1, org_high)
	return inlist

if __name__=="__main__":
	t = [5, 3, 4, 12, 2, 12, 22, 11]
	d = quick_sort(t, 0, len(t)-1)
	print d
