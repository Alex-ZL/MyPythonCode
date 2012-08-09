#!usr/bin/evn python
# -*- coding:utf-8 -*-
## a example to get used to json
import json
indata = [
			{
				'num':2896,
				'author':'what',
				'title':u'置顶贴',
				'date': '2012-07-24T18:27:00',
				'replyCount':4,
				'viewCount':1539
			},
			{
				'num':1,
				'author':'nothing',
				'title':u'能做，就做好来.',
				'date':'2012-07-23T18:12:00',
				'replyCount':3,
				'viewCount':122
			}
		]

outdata = json.dumps(indata, ensure_ascii=False)
print type(outdata)
print outdata
