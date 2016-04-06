import os
import pexpect

def reboot_testmachine():
    reboot = pexpect.spawn('ssh root@192.168.32.46')
    reboot.expect(':')
    reboot.sendline('abc123')
    reboot.sendline('reboot')
    reboot.interact()

#reboot_testmachine()
