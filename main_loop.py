import os
import sys
import time
import send_cmd
import cmd_handling
import get_hid

hid = get_hid.get_hid()
ERASE_LINE = '\x1b[2K'
print ERASE_LINE
#req_status = send_cmd.send_cmd('QPIGS', hid)
fpid = os.fork()
if fpid!=0:
    # Running as daemon now. PID is fpid
    sys.exit(0)
while 1:
    outfile = open('log.txt', 'a')
    response = ''
    array = ''
    os.system('clear')
    sys.stdout.flush()
    response = send_cmd.send_cmd('QPIGS', hid)
    array = cmd_handling.status_parse(response)
    
    #grab date and time and hold it as a string
    timeString = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    
    #write datetime and values to log file
    outfile.write(timeString + '\t' + array[0] + '\t' + array[1] + '\t' + array[2] + '\t' + array[3] + '\t' + array[4] + '\t' + array[5] + '\t' + array[6] + '\t' + array[7] + '\t' + array[8] + '\t' + array[9] + '\t' + array[10] + '\t' + array[11] + '\t' + array[12] + '\t' + array[13] + '\t' + array[14] + '\t' + array[15] + '\t' + array[16] + '\t' + array[17] + '\t' + array[18] + '\t' + array[19] + '\n')
    
    #close file after writing to it
    outfile.close()
    print ERASE_LINE + 'Grid Voltage: ' + array[0] + '\r',
    time.sleep(1)

