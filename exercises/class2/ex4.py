#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract

def print_sysDescr(host,community,port):
	print "\nSysDescr = " + snmp_extract(snmp_get_oid((host,community,port)))

def print_sysName(host,community,port):
	print "\nSysName = " + snmp_extract(snmp_get_oid((host,community,port),oid='1.3.6.1.2.1.1.5.0'))
	
def main():

	HOST = "50.76.53.27"
	PORT1 = 7961
	PORT2 = 8061
	COMMUNITY = "galileo"
	
	print "ROUTER 1:"
	print print_sysDescr(HOST,COMMUNITY,PORT1)
	print_sysName(HOST,COMMUNITY,PORT1)
	print "\n"
	print "ROUTER 2:"
	print_sysDescr(HOST,COMMUNITY,PORT2)
	print_sysName(HOST,COMMUNITY,PORT2)
	print "\n"
	
	
if __name__ == "__main__":
    
	main()
	
	
	