def out_priority_parse(response):
    if (response[:2] == 'ACK'):
        return 0
    if (response[:2] == 'NCK'):
        return 1
    if (response[:2] != 'NCK') and (response[:2] != 'ACK'):
        return 2

def enable_disable(response):
    if response is 'a':
        return 'Mute buzzer'
    if response is 'b':
        return 'Overload Bypass function'
    if response is 'j':
        return 'Power Saving'
    if response is 'k':
        return 'LCD display home after 1 minute timeout'
    if response is 'u':
        return 'Overload restart'
    if response is 'v':
        return 'Overheat restart'
    if response is 'x':
        return 'Backlight'
    if response is 'y':
        return 'Alarm on primary source interrupt'
    if response is 'z':
        return 'Fault code record'
    if response is 'l':
        return 'Data log pop-up'

def flag_parse(response):
    response[:12]
    if response[0] is 'E':
        print '\nEnabled:'
        j = 1
        while response[j] != 'D':
            print enable_disable(response[j])
            j += 1
    if response[j] is 'D':
        print '\nDisabled:'
        j += 1
        while response[j].isalpha():
            print enable_disable(response[j])
            j += 1
        exit

def mode_parse(response):
    print 'Current Mode:',
    if response[0] is 'P':
        print 'Power On'
    if response[0] is 'S':
        print 'Standby'
    if response[0] is 'L':
        print 'Line/Bypass'
    if response[0] is 'B':
        print 'Battery'
    if response[0] is 'F':
        print 'Fault'
    if response[0] is 'H':
        print 'Power Saving'
