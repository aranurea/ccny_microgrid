import sys
import os
import time

def get_hid():
    while 1:
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
                hid_pos = line.find('hidraw') + 6
                while line[hid_pos]!= ':':
                    hidnum = hid + line[hid_pos]
                    hid_pos += 1
                break

        if hid is not 'hidraw':
            break

        print 'Device not found. Retry in 60 seconds.'
        time.sleep(60)

    return hidnum
