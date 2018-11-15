import sys
import os

def get_hid():
    os.system("dmesg > hidnum.txt")
    infile = open('hidnum.txt', 'r')
    vid = "413C"
    pid = "2107"
    hid = "hidraw"

    for line in infile:
        if (vid in line) and (pid in line) and (hid in line):
            print line
            hid_pos = line.find('hidraw') + 6
            line[hid_pos]
            while line[hid_pos]!= ':':
                hid = hid + line[hid_pos]
                hid_pos = hid_pos + 1
    infile.close()
    os.system('rm hidnum.txt')
    print hid
    return hid
