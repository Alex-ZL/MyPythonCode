#!/usr/bin/python
import time

dictcache = {}
def cache(func):
	def __decorator(user):
		now = time.time()
		if (user in dictcache):
			result,cache_time = dictcache[user]
			if (now - cache_time) > 30:
				result = func(user)
				dictcache[user] = (result, now)
			else:
				print('cache hits')
		else:
			result = func(user)
			dictcache[user] = (result, now)
		return result
	return __decorator


def login(user):
	print("in login:" + user)
	msg = validate(user)
	return msg

@cache
def validate(user):
	time.sleep(5)
	msg = "success" if user == "ivy" else "fail"
	return msg

result1 = login("emma"); print result1
result2 = login("ivy"); print result2
result2 = login("ivy"); print result2
result3 = login("who"); print result3
