import os
import sys
import time
import send_cmd
import cmd_handling
import get_hid
import threading

hid = get_hid.get_hid()

thread_id = ''

def status_thread():
    #req_status = send_cmd.send_cmd('QPIGS', hid)
    while 1:
        outfile = open('log.txt', 'a')
        response = ''
        array = ''
        ###os.system('clear')
        ###sys.stdout.flush()
        response = send_cmd.send_cmd('QPIGS', hid)
        
        if (response is not None) and (response[:3] is not 'NAK'):
            array = list(response.split())

            #grab date and time and hold it as a string
            timeString = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

            #write datetime and values to log file
            try:
                outfile.write(timeString + '\t' + array[0] + '\t' + array[1] + '\t' + array[2] + '\t' + array[3] + '\t' + array[4] + '\t' + array[5] + '\t' + array[6] + '\t' + array[7] + '\t' + array[8] + '\t' + array[9] + '\t' + array[10] + '\t' + array[11] + '\t' + array[12] + '\t' + array[13] + '\t' + array[14] + '\t' + array[15] + '\t' + array[16] + '\t' + array[17] + '\t' + array[18] + '\t' + array[19] + '\n')
                
            except:
                pass

        #close file after writing to it, sleep for 1 second
        outfile.close()
        time.sleep(.5)

#start status_thread as daemon to query inverter every 1 second
def start_main():
    main_thread = threading.Thread(target = status_thread(), args = None)
    main_thread.start
