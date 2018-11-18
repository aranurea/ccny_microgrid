import sys
import os
import send_cmd

def get_hid():
    os.system('dmesg > hidnum.txt')
    infile = open('hidnum.txt', 'r')
    inlines = infile.readlines()
    infile.close()
    os.system('rm hidnum.txt')
    inlines.reverse()
    vid = '0665'
    pid = '5161'
    hid = 'hidraw'

    for line in inlines:
        if (vid in line) and (pid in line) and (hid in line):
            #print line
            hid_pos = line.find('hidraw') + 6
            #line[hid_pos]
            while line[hid_pos]!= ':':
                hidnum = hid + line[hid_pos]
                hid_pos += 1
            break

    
    #print hidnum
    #print send_cmd.send_cmd('QPIGS', hidnum)     #first response will be NAK/ACK
    return hidnum

get_hid();
