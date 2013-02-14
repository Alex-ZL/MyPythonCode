#!/usr/bin/python
import copy
alist = [[1],[2],[3]]
blist = copy.deepcopy(alist)
blist[0].append('what')
print alist
print blist
