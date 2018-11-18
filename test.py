import os
import sys
import time
import datetime
import send_cmd
import cmd_handling
import get_hid

outfile = open('log.txt', 'a')
hid = get_hid.get_hid()
response = send_cmd.send_cmd('QPIGS', hid)
array = cmd_handling.status_parse(response)
print array
print datetime.datetime.now()

#time = '[' + decimal.Decimal(time.time()) + ']'

#outfile.write(time)
outfile.write('\t' + array[0] + '\t' + array[1] + '\t' + array[2] + '\t' + array[3] + '\t' + array[4] + '\t' + array[5] + '\t' + array[6] + '\t' + array[7] + '\t' + array[8] + '\t' + array[9] + '\t' + array[10] + '\t' + array[11] + '\t' + array[12] + '\t' + array[13] + '\t' + array[14] + '\t' + array[15] + '\t' + array[16] + '\t' + array[17] + '\t' + array[18] + '\t' + array[19] + '\n')

outfile.close()
