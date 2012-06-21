#!/urs/share/python
#print 'I must act to let you know my love'
import string
table = string.maketrans('cs','kz')
print len(table)
print string.maketrans('','')[97:123]
print 'this is an incredible test'.translate(table)
