#!/usr/bin/evn python
## a example of sort a list by nested tuple value
alist = [(3,2), (3,1), (3,3), (1,2), (1,1), (2,1), (2,3), (2,2)]
#alist.sort(key = lambda x:(x[0], x[1]))
#print alist
print sorted(alist, key = lambda x:(x[0], x[1]))
