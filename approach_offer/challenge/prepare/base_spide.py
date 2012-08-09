#!usr/bin/evn python
# -*- coding:utf-8 -*-
import urllib2
import re
from HTMLParser import HTMLParser
from subprocess import Popen, PIPE

content = urllib2.urlopen('http://bbs.nju.edu.cn/board?board=girls').read()
content2 =unicode(urllib2.urlopen('http://bbs.nju.edu.cn/bbstcon?board=Pictures&file=M.1343140887.A').read(),'gb2312')

#HTMLParser.attrfind = re.compile(
#		r'\s*([a-zA-Z_][-.:a-zA-Z_0-9]*)(\s*=\s*'
#		r'(\'[^\']*\'|"[^"]*"|[^\s>^\[\]{}\|\'\"]*))?')
##print content

global outlist 
outlist =[]
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print "Encountered a start tag: ", tag
	def handle_endtag(self,tag):
		print "Encountered an end tag: ", tag
	def handle_data(self, data):
		if data:
			outlist.append(data)

#text = open('board_list').read()
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)

tidy.stdin.write(content)
tidy.stdin.close()
pretty_content = tidy.stdout.read()
x_file = open('pretty_html','w')
x_file.write(pretty_content)
x_file.close()

myparser = MyHTMLParser()
#myparser.feed("<title><a href=bbsqry?userid='1573'> Hold on</a></title>")
#myparser.feed(pretty_content)
myparser.feed("<tr><td>6853<td>   <td><a href=bbsqry?userid='1573'>1573</a><td><td><nobr>Jul 25 08:57<td><a href=bbscon?board=Girls&file=M.1343177841.A&num=6852>Re: 问一个有点变态的问题。 </a>(<font style='font-size:12px; color:#008080'>22字节</font>)<td><font color=black>3</font>")
print outlist
