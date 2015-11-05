#!/usr/bin/env python

import telnetlib

def show_int():
	
    IP = "50.76.53.27"
    TELNET_PORT = 23
    USER = "pyclass"
    PASSWORD = "88newclass"
    TELNET_TIMEOUT = 5
	
    try:
        remote_conn = telnetlib.Telnet(IP,TELNET_PORT,TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed out")

    remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(USER + "\n")
    remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(PASSWORD + "\n")
    remote_conn.read_until("#", TELNET_TIMEOUT)	
    remote_conn.write("term len 0\n")
    remote_conn.read_until("#", TELNET_TIMEOUT)	
    remote_conn.write("show ip interface brief\n")
    output = remote_conn.read_until("#")
    print "OUTPUT:"
    print output
    remote_conn.close()
	
if __name__== "__main__":
    show_int()

