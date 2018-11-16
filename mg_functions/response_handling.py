def status_parse(response):
    values = list(response.split())
    values[0][0] = ""

    return values

def out_priority_parse(response):
    if (response[1:3] != "ACK"):
        return 0
    else:
        return 1

def flag_parse(response):
    response[:12]
    if response[0] is "E":
        print "\nEnabled:"
        j = 1
        while response[j] != "D":
            if response[j] is "a":
                print "Mute buzzer"
            if response[j] is "b":
                print "Overload Bypass function"
            if response[j] is "j":
                print "Power Saving"
            if response[j] is "k":
                print "LCD display home after 1 minute timeout"
            if response[j] is "u":
                print "Overload restart"
            if response[j] is "v":
                print "Overheat restart"
            if response[j] is "x":
                print "Backlight"
            if response[j] is "y":
                print "Alarm on primary source interrupt"
            if response[j] is "z":
                print "Fault code record"
            if response[j] is "l":
                print "Data log pop-up"
            j += 1
    if response[j] is "D":
        print "\nDisabled:"
        while response[j] != "/":
            if response[j] is "a":
                print "Mute buzzer"
            if response[j] is "b":
                print "Overload Bypass function"
            if response[j] is "j":
                print "Power Saving"
            if response[j] is "k":
                print "LCD display home after 1 minute timeout"
            if response[j] is "u":
                print "Overload restart"
            if response[j] is "v":
                print "Overheat restart"
            if response[j] is "x":
                print "Backlight"
            if response[j] is "y":
                print "Alarm on primary source interrupt"
            if response[j] is "z":
                print "Fault code record"
            if response[j] is "l":
                print "Data log pop-up"
            j += 1
        exit
