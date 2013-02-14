#!usr/bin/evn python
##Unicode in network sockets

import sys
import SocketServer

class Echo(SocketServer.BaseRequestHandler):

	def handle(self):
		data = self.request.recv(1024)
		self.request.send(data)
		return

class PassThrough(object):

	def __init__(self, other):
		self.other = other

	def write(self, data):
		print 'Writing :', repr(data)
		return self.other.write(data)

	def read(self, size=-1):
		print 'Reading :',
		data = self.other.read(size)
		print repr(data)
		return data

	def flush(self):
		return self.other.flush()

	def close(self):
		return self.other.close()


if __name__ == '__main__':
	import codecs
	import socket
	import threading

	address = ('localhost', 0) #let the kernel give us a port
	server = SocketServer.TCPServer(address,Echo)
	ip, port = server.server_address 

	t = threading.Thread(target=server.serve_forever)
	t.setDaemon(True)
	t.start()

	# Connect to the server
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))

	# Wrap the socket with a reader and writer
	incoming = codecs.getreader('utf-8')(PassThrough(s.makefile('r')))
	outgoing = codecs.getwriter('utf-8')(PassThrough(s.makefile('w')))

	# Send the data
	text = u'pi: n'
	print 'Sending :', repr(text)
	outgoing.write(text)
	outgoing.flush()
	##len_sent = s.send(text)

	#Receive a response
	######response = s.recv(len_sent)
	response = incoming.read()
	print 'Received:',  repr(response)

	# Clean up
	s.close()
	server.socket.close()
