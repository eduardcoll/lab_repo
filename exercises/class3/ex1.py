#!/usr/bin/env python

import smtplib, pickle
import os.path
import datetime
from snmp_helper import snmp_get_oid_v3,snmp_extract
from email.mime.text import MIMEText

def save_to_file(data,filename):
    f = open(filename,"wb")
    pickle.dump(data,f)
    f.close()


def main():
    snmp_device = ('50.76.53.27',8061)
    snmp_user = ('pysnmp','galileo1','galileo1')

    oid_name = 'ccmHistoryRunningLastChanged'
    oid = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    snmp_data = snmp_extract(snmp_get_oid_v3(snmp_device, snmp_user, oid))
    
    filename = 'time.pkl'
    

    #if file not exist
    if not os.path.exists(filename):
        #save snmp_data to file
        save_to_file(snmp_data,filename)
    
    #else file exists
    else:
        #read file and compare with snmp_data
        f = open(filename,'rb')
        loaded_data = pickle.load(f)
        f.close()
                      
        #if snmp_data is different than the file's snmp_data
        #loaded_data = '16585065'
        if not loaded_data == snmp_data:
            print 'CONFIG CHANGE DETECTED' 

            #get the hostname
            host =  snmp_extract(snmp_get_oid_v3(snmp_device, snmp_user, '1.3.6.1.2.1.1.5.0'))
                        
            #get the uptime of last change
            change_time_in_seconds = int(int(snmp_data)/100)
            
            #get the system uptime
            uptime_in_seconds = int(snmp_extract(snmp_get_oid_v3(snmp_device, snmp_user, '1.3.6.1.2.1.1.3.0')))/100
            
            #get the current DATE
            now = datetime.datetime.now()
            
            #get the DATE the config changed
            changed = now - datetime.timedelta(0,uptime_in_seconds-change_time_in_seconds)
                                   
            #Prepare message
 
            recipient = 'eduard.coll@ntt.eu'
            sender = 'ktbyers@twb-tech.com'
            subject = 'Config changed'
            message = "HOSTNAME: " + host + " CHANGED CONFIG AT: " + str(changed)
             
            #send email
            message = MIMEText(message)
            message['Subject'] = subject
            message['From'] = sender
            message['To'] = recipient
            
            print message
 
            #Connect to SMTP server and send email
            smtp_conn = smtplib.SMTP('localhost')
            smtp_conn.sendmail(sender,recipient,message.as_string())
            smtp_conn.quit()
            
        
        #else snmp data is equal
        else:
            print 'Config not changed'
        
        save_to_file(snmp_data,filename)
            
    
    
    
        

    

if __name__ == "__main__":
    main()