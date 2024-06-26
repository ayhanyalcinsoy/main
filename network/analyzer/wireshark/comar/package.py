#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # Set capabilities in order to prevent wireshark from being executed as root
    os.system("/bin/chgrp 207 /usr/bin/dumpcap")
    os.system("/bin/chmod 754 /usr/bin/dumpcap")
    os.system("/bin/chown root:wireshark /usr/bin/dumpcap")
    os.system("/sbin/setcap cap_net_raw,cap_net_admin,cap_dac_override+eip /usr/bin/dumpcap")