
from netmiko import ConnectHandler

# inform = {
#     'device_type': 'cisco_ios',
#     'ip': '10.52.31.241',
#     'username': 'wonhyo.choi',
#     'password': 'Pa$$w0rdLM',
#     'secret': 'tmxkxm@00&',
#     'port': '22',
# }

# net_connect = ConnectHandler(**inform)
# output = net_connect.send_command('show ip int br')
# print(output)



inform = {
    'device_type': 'juniper_junos',
    'ip': '10.52.54.237',
    'username': 'martadmin',
    'password': 'wkatlf@01$',
    # 'secret': 'tmxkxm@00&',
    'port': '22',
}

# mycommand = "show interfaces descriptions"
mycommand = "show configuration" + " | display set"

net_connect = ConnectHandler(**inform)


# net_connect.enable() #접속
# net_connect.exit_enable_mode() #종료
if net_connect.check_enable_mode: #Enable 모드면 True, 아니면 False
    print("Enable!\n")
else:
    print("NO!\n")



# net_connect.config_mode() #접속
# net_connect.exit_config_mode() #종료
if net_connect.check_config_mode: #Config 모드면 True, 아니면 False
    print("Config!\n")
else:
    print("No!\n")

output = net_connect.send_command(mycommand)
print(output)