
from netmiko import ConnectHandler

informs = [{
        'device_type': 'juniper_junos',
        'ip': '',
        'username': '',
        'password': '',
        # 'secret': '',
        'port': '22',
    }, {
        'device_type': 'juniper_junos',
        'ip': '',
        'username': '',
        'password': '',
        # 'secret': '',
        'port': '22',
    }
]
mycommand = "show | compare"

config_commands = [ 'set interfaces ge-0/0/10 description " ## Test 5 ## "',
                    'set interfaces ge-0/0/11 description " ## Test 6 ## "']


for inform in informs:
    net_connect = ConnectHandler(**inform)

    edit = net_connect.send_config_set(config_commands, exit_config_mode=False)

    # print(edit)

    output = net_connect.find_prompt()

    # print(output)

    compare = net_connect.send_config_set(mycommand, exit_config_mode=False)

    print(compare)
