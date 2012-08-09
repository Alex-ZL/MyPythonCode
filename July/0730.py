#!/usr/bin/env python
# -*- coding: utf-8 -*-

#print chr(65)
#print unichr(12340)
#print ord(u'\ua000')

import binascii
import codecs

def to_hex(t, nbytes):
	"format text t as a sequence of nbyte long values separated by space."
	chars_per_item = nbytes * 2
	hex_version = binascii.hexlify(t)
	num_chunks = len(hex_version) / chars_per_item
	def chunkify():
		for start in xrange(0, len(hex_version), chars_per_item):
			yield hex_version[start:start + chars_per_item]
	return ' '.join(chunkify())

if __name__ == '__main__':
	print to_hex('abcdef', 1)
	print to_hex('abcedf', 2)

	text = u'pi: n'
	print 'Raw    :', repr(text)
	print 'UTF-8  :', to_hex(text.encode('utf-8'),1)
	print 'UTF-16 :', to_hex(text.encode('utf-16'),2)

	encoded = text.encode('utf-8')
	decoded = encoded.decode('utf-8')
	print 'Original :', repr(text)
	print 'Encoded  :', to_hex(encoded, 1), type(encoded)
	print 'Decoded  :', repr(decoded), type(decoded)

	encoding = 'utf-8'
	filename = encoding + '.txt'

	print 'Writing to', filename
	with codecs.open(filename, mode='wt', encoding=encoding) as f:
		f.write(u'pi: \u03c0')

	nbytes = { 'utf-8':1,
			   'utf-16':2,
			   'utf-32':4,
			   }.get(encoding, 1)
	print "File contents:"
	with open(filename, mode='rt') as f:
		print to_hex(f.read(), nbytes)
	
	for name in ['BOM', 'BOM_BE', 'BOM_LE', 
			     'BOM_UTF8',
				 'BOM_UTF16', 'BOM_UTF16_BE', 'BOM_UTF16_LE',
				 'BOM_UTF32', 'BOM_UTF32_BE', 'BOM_UTF32_LE',
				 ]:
		print '{:12} : {}'.format(name, to_hex(getattr(codecs, name), 2))
		
	

