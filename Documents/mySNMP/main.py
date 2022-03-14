
import os
import sys

sys.stdout = open('stdout2.txt', 'w')

hostname = "127.0.0.2"
cmd = "ping " + hostname + " -c 4"

# Ping_response = os.system("ping " + hostname)

# if Ping_response == 0:
#     Net_status = "Network Active"

# else:
#     Net_status = "Network Error"

# res = os.system("ifconfig")



res = os.popen(cmd).read().strip().split('\n')

for r in res:
    print(r)
# res = os.popen("ifconfig").read().strip().split()
# print(res)

sys.stdout.close()