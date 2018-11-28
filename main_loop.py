import os
import sys
import time
import send_cmd
import cmd_handling
import get_hid
import threading

#manual_cmd holds user cmds for execution
manual_cmd = ''
#flasg for manual command execution
cmd_flag = 0

hid = get_hid.get_hid()

def status_thread():
    global cmd_flag
    global manual_cmd
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

        if cmd_flag is 1:
            response = send_cmd.send_cmd(manual_cmd, hid)
            
            manual_cmd = ''
            cmd_flag = 0

#start status_thread as daemon to query inverter every 1 second

def manual_cmd_input():
    global cmd_flag
    global manual_cmd
    while 1:
        if cmd_flag is 0:
            print ('What command would you like to run?')
            manual_cmd = raw_input()
            cmd_flag = 1


main_thread = threading.Thread(target = status_thread)
cmd_thread = threading.Thread(target = manual_cmd_input)
main_thread.start()
print 'Main thread started'
cmd_thread.start()
print 'Secondary thread started'
