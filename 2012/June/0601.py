#!/usr/bin/python
##improved resolution for level_3
if mport string
def level_3(t1):
	pad = 'x'
	t1 = pad + t1 + pad
	markers = "".join(['1' if c in string.uppercase else '0' for c in t1])
	pattern = "011101110"
	def f(res, t2, markers):
		n = len(markers.partition(pattern)[0])
		end_of_string = lambda res, t2, markers: markers == pattern and res+t2[4] or res
		return f(res+t2[n+4], t2[n+4], markers[n+4:]) if n != len(markers) else end_of_string(res, t2, markers)
	return f('',t1,markers)

