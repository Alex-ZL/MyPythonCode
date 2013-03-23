#/usr/bin/env python

def insert_sort(inlist):
	for j in range(1,len(inlist)):
		key = inlist[j]
		i = j
		while i > 0 and inlist[i-1] > key:
			inlist[i] = inlist[i-1]
			i -= 1
			inlist[i] = key
	return inlist

if __name__=="__main__":
	t = [2, 3, 4, 3, 1, 5, 5, 6]
	print insert_sort(t)
