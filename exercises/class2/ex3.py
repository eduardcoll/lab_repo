#!/usr/bin/env python
'''
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import telnetlib
import time
import socket
import sys
import getpass

class Connection:

    TELNET_PORT = 23
    TELNET_TIMEOUT = 6
    
    remote_conn = None

    def send_command(self, cmd):
        '''
        Send a command down the telnet channel

        Return the response
        '''
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(1)
        return self.remote_conn.read_very_eager()

    def login(self, username, password):
        '''
        Login to network device
        '''
        output = self.remote_conn.read_until("sername:", self.TELNET_TIMEOUT)
        self.remote_conn.write(username + '\n')
        output += self.remote_conn.read_until("ssword:", self.TELNET_TIMEOUT)
        self.remote_conn.write(password + '\n')
        return output

    def disable_paging(self, paging_cmd='terminal length 0'):
        '''
        Disable the paging of output (i.e. --More--)
        '''
        return self.send_command(paging_cmd)

    def telnet_connect(self,ip_addr):
        '''
        Establish telnet connection
        '''
        try:
            self.remote_conn = telnetlib.Telnet(ip_addr, self.TELNET_PORT, self.TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")


def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()
    con = Connection()
    con.telnet_connect(ip_addr)
    output = con.login(username, password)

    time.sleep(1)
    con.remote_conn.read_very_eager()
    con.disable_paging()

    output = con.send_command('show ip int brief')

    print "\n\n"
    print output
    print "\n\n"

    con.remote_conn.close()

if __name__ == "__main__":
    main()
