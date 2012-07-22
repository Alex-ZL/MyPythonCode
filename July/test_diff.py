#!/usr/bin/env python
#coding = utf-8
a = {'a1':'b1','a2':{'b2':'c2'},'a3':'b3'}
b = {'a1':'b1','a2':{'b2':'c3'}}

def p(x, root=None):
	for k, v in x.items():
		if isinstance(v,dict):
			for t in p(v,k):
				yield t
		else:
			if root:
				yield((root,k),v)
			else:
				yield(k,v)

a1 = set([x for x in p(a)])
b1 = set([x for x in p(b)])

print a1
print b1
print a1|b1
print a1&b1
print a1^b1
