#!/usr/bin/env python
import socket

def find_service_name(protocolname,ports):
	for port in ports:
		try:
			print "Port:%s => service name: %s" % (port,socket.getservbyport(port,protocolname))
		except socket.error, err_msg:
			print err_msg

if __name__ == '__main__':
	protocolname=raw_input("Please input protocol name:")
	ports=[]
	port=int(raw_input("Please input ports:"))
	ports.append(port)
	while port!=-1:
		port=int(raw_input("Please input ports:"))
		ports.append(port)
	ports.pop()
	find_service_name(protocolname,ports)
