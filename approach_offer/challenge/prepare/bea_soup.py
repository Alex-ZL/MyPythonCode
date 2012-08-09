#!usr/bin/evn python
# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
import time, datetime

content0 = urllib2.urlopen('http://bbs.nju.edu.cn/board?board=NoteBook').read()
content = urllib2.urlopen('http://bbs.nju.edu.cn/board?board=pictures').read()
content1 = urllib2.urlopen('http://bbs.nju.edu.cn/board?board=girls').read()
content2 = urllib2.urlopen('http://bbs.nju.edu.cn/bbstcon?board=Pictures&file=M.1343140887.A').read()
soup = BeautifulSoup(content)

#xfile = open('soup_pretty','w')
#xfile.write(soup.prettify().encode('gb2312','ignore'))
#xfile.close()

# convert date format from 'Jul 25 16:20' to '2012-07-25T16:20:00'
def date_format_convert(s_date):
	temp = time.strptime(s_date, "%b %d %H:%M")
	return  str(datetime.datetime.now().year) + time.strftime("-%m-%dT%H:%M:%S", temp)

postlist = []

#def get_postlist_pictures(postlist):
for item in soup.findAll('a', href=re.compile('^bbsqry.*')):

	##only fetch the item with 4 or 5 digits PostID.
	if len(item.parent.parent.contents[0].contents[0]) in (4,5):
		record = item.parent.parent.contents
		dict_record = {}
		if len(record) == 6:
			print record[0].contents[0]
			dict_record['num'] = record[0].contents[0]
			#print record[2].contents[0].contents[0]
			dict_record['author'] = record[2].contents[0].contents[0]
			#print date_format_convert(record[3].contents[0])
			dict_record['date'] = date_format_convert(record[3].contents[0])
			#print record[4].contents[0].contents[0]
			dict_record['title'] = record[4].contents[0].contents[0]
			#print record[5].contents[0].contents[0]
			dict_record['replyCount'] = record[5].contents[0].contents[0]
			#print record[5].contents[2].contents[0]
			dict_record['viewCount'] = record[5].contents[2].contents[0]
		else:
			print record
			#print record[0].contents[0]
			dict_record['num'] = record[0].contents[0]
			#print record[2].contents[0].contents[0]
			dict_record['author'] = record[2].contents[0].contents[0]
			print record[4].contents[0].contents
			dict_record['date'] = date_format_convert(record[4].contents[0].contents[0])
			dict_record['title'] = record[4].contents[0].contents[1].contents[0].contents[0]
			dict_record['replyCount'] = record[4].contents[0].contents[2].contents[0].contents[0]

		postlist.append(dict_record)

print postlist 
