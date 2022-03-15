
# -*- coding: utf-8 -*-

import os
import sys
import datetime

sys.stdout = open('stdout2.txt', 'w')

hosts = ["10.52.31.252", "10.52.31.253", "10.52.16.163"]

for host in hosts:
    cmd = "ping " + host + " -n 4"

    # res = os.popen(cmd).read().strip().split('\n')
    res = os.system("ping " + host + " -n 1")

    if res == 0:
        print(host, "ping ok in ", datetime.datetime.now())
    
    else:
        print(host, "ping not ok in ", datetime.datetime.now())


# Ping_response = os.system("ping " + hostname)

# if Ping_response == 0:
#     Net_status = "Network Active"

# else:
#     Net_status = "Network Error"

# res = os.system("ifconfig")



    # res = os.popen(cmd).read().strip().split('\n')
    # for r in res:
    #     print(r)
# res = os.popen("ifconfig").read().strip().split()
# print(res)

sys.stdout.close()