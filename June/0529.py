#!/usr/bin/python

import string
notrans = string.maketrans('','')
def containAny(str, strset):
	"""check str is substring of strset"""
	return len(strset) != len(strset.translate(notrans,str))

def iscapitalized(s):
	return s == s.capitalize() and containAny (s, string.letters)

##print containAny("1234",string.letters)
#map = string.maketrans('123','abc')
#print 'alex123 345 emma'.translate(map,"45")
#print iscapitalized('123')

##PythonChallange
print ( 2**38)
oldstr='abcdefghijklmnopqrstuvwxyz'
newstr='cdefghijklmnopqrstuvwxyzab'
mytrans = string.maketrans(oldstr, newstr)
str = "g fmnc wms bgblr rpylqjyrc grzwfylb. rfyrq ufyr amknsrcpqypc dmp.bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gqpcambcb.lmu ynnjw ml rfc spj."
print str.translate(mytrans)
print "map".translate(mytrans)
