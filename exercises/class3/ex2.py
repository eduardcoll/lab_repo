#!/usr/bin/env python

import smtplib,pygal,time
from snmp_helper import snmp_get_oid_v3,snmp_extract

def get_int_value(oid):

    snmp_device = ('50.76.53.27',7961)
    snmp_user = ('pysnmp','galileo1','galileo1')
    
    value = int(snmp_extract(snmp_get_oid_v3(snmp_device, snmp_user, oid)))
    
    return value

def main():

    oid = {
    'ifDescr' : '1.3.6.1.2.1.2.2.1.2.5',
    'ifInOctets' : '1.3.6.1.2.1.2.2.1.10.5',
    'ifInUcastPkts': '1.3.6.1.2.1.2.2.1.11.5',
    'ifOutOctets': '1.3.6.1.2.1.2.2.1.16.5',
    'ifOutUcastPkts': '1.3.6.1.2.1.2.2.1.17.5'  
    }
    
    fa4_in_octets = []
    fa4_out_octets = []
    fa4_in_pkts = []
    fa4_out_pkts = []
    
    print "GATHERING INITIAL INFO"
	
    last_in_bytes = get_int_value(oid['ifInOctets'])
    last_out_bytes = get_int_value(oid['ifOutOctets'])
    last_in_pkts = get_int_value(oid['ifInUcastPkts'])
    last_out_pkts = get_int_value(oid['ifOutUcastPkts'])
	
    time.sleep(5)
    
    for tick in range(0,65,5):
    
        print str(tick) + " minutes"
    
        in_bytes = get_int_value(oid['ifInOctets'])
        out_bytes = get_int_value(oid['ifOutOctets'])
        in_pkts = get_int_value(oid['ifInUcastPkts'])
        out_pkts = get_int_value(oid['ifOutUcastPkts'])
                                    
        fa4_in_octets.append(int(in_bytes)-last_in_bytes)
        fa4_out_octets.append(int(out_bytes)-last_out_bytes)
        fa4_in_pkts.append(int(in_pkts)-last_in_pkts)
        fa4_out_pkts.append(int(out_pkts)-last_out_pkts)
        
        print fa4_in_octets
        print fa4_out_octets
        print fa4_in_pkts
        print fa4_out_pkts
        
        last_in_bytes = in_bytes
        last_out_bytes = out_bytes
        last_in_pkts = in_pkts
        last_out_pkts = out_pkts
        
        time.sleep(5*60)
             
        print
        
    print "GENERETING GRAPHS"
    
    # Create a Chart of type Line
    line_chart_bytes = pygal.Line()
    line_chart_pkts = pygal.Line()
    # Title
    line_chart_bytes.title = 'Input/Output Bytes'
    line_chart_pkts.title = 'Input/Output Packets'
    # X-axis labels
    line_chart_bytes.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
    line_chart_pkts.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
    # Add each one of the above lists into the graph as a line with corresponding label
    line_chart_pkts.add('InPackets', fa4_in_pkts)
    line_chart_pkts.add('OutPackets',  fa4_out_pkts)
    line_chart_bytes.add('InBytes', fa4_in_octets)
    line_chart_bytes.add('OutBytes', fa4_out_octets)
    # Create an output image file from this
    line_chart_bytes.render_to_file('bytes.svg')
    line_chart_pkts.render_to_file('packets.svg')
    
    print "FINISHED"

if __name__ == "__main__":
    main()