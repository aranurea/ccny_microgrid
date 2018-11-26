import os
import sys
import time

from crc16 import crc16xmodem
from struct import pack
from traceback import format_exc

def send_cmd(encoded_cmd, hidnum):

    checksum = crc16xmodem(encoded_cmd)
    request = encoded_cmd + pack('>H', checksum) + '\r'


    try:
        fd = os.open('/dev/'+ hidnum,  os.O_RDWR|os.O_NONBLOCK)
    except:
        response = 'NAK Device not connected'
        print response[4:]
        return response
    
    try:
        #time.sleep(.125)

        os.write(fd, request[:8])
        if len(request) > 8:
            os.write(fd, request[8:])

        #print('Write done')
        time.sleep(.5)

        response = ''
        try:
            while True:
                chunk = os.read(fd, 8).encode('string-escape')
                if not chunk:
                    break
                response += chunk
        except:
            pass
    except Exception as e:
        print(format_exc(e))
    finally:
        os.close(fd)
        
    try:
        response = response[1:]
    except:
        response = 'NAK Response not assigned'
        print response[4:]
        return response
    finally:
        return response

#encoded_cmd = 'POP00'
#print send_cmd(encoded_cmd, "hidraw6")

