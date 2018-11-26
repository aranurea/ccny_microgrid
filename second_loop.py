import main_loop

main_loop.start_main()

print 'What command would you like to send?'
raw_input(command)

if command == 'mode':
    manual_cmd = send_cmd.send_cmd('QMOD', hid)
    cmd_handling.mode_parse(manual_cmd)
