#!/usr/bin/env python

# take a remote host name as a parameter to get its corresponding IP address
import socket

def get_remote_machine_info(r_host_name):
	try:
		print "IP address: %s" % socket.gethostbyname(r_host_name)
	except socket.error, err_msg:
		print "%s: %s" % (r_host_name,err_msg)

if __name__ == '__main__':
	remote_hostname=raw_input("Please input remote host name:")
	get_remote_machine_info(remote_hostname)