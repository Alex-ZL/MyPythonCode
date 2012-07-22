import os
from os.path import join, getsize
for root, dirs, files in os.walk('Rename'):
	print '##root', root
	print '##dirs', dirs
	print '##files', files
	print root, "consumes"
	print sum([getsize(join(root, name)) for name in files])
	print "bytes in", len(files), "non-directory files"
	if 'HP_sNZ' in dirs:
		print "HP_NZ directory removed"
		dirs.remove('HP_NZ')
