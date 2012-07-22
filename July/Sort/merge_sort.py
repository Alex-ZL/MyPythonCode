#usr/bin/evn python
## merge sort

def merge(l1,l2):
	final = []
	while l1 and l2:
		final.append(l1[0] <= l2[0] and l1.pop(0) or l2.pop(0))
	return final + l1 + l2


def mergesort(List):
	mid = int(len(List)/2)
	if len(List) <= 1: return List
	return merge(mergesort(List[:mid]), mergesort(List[mid:]))


def iter_mergesort(List):
	Q=[]

	for i in List:
		Q.append([i])

	while len(Q) > 1:
		Q.append(merge(Q.pop(0),Q.pop(0)))

	return Q.pop()


l1 = [1,3,5,7,9,2,4,5,6,7,8,10]
l2 = [2,4,6,8,10,11]
print mergesort(l1)
print iter_mergesort(l1)
