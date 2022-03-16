
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
    #, {
    #     'device_type': 'juniper_junos',
    #     'ip': '',
    #     'username': '',
    #     'password': '',
    #     # 'secret': '',
    #     'port': '22',
    # }
]

mycommand = "show | compare"

# config_commands = [ 
#                     # 'set interfaces ge-0/0/10 description " ## Test 5 ## "',
#                     # 'set interfaces ge-0/0/11 description " ## Test 6 ## "',
#                     'set firewall family inet filter SCAL-IN term TEST from source-address 10.57.'+250+'.0/24',
#                     'set firewall family inet filter SCAL-IN term TEST from destination-address 10.52.31.152',
#                     'set firewall family inet filter SCAL-IN term TEST then accept',
#                     'set firewall family inet filter SCAL-OUT term TEST from source-address 10.52.31.152/32',
#                     'set firewall family inet filter SCAL-OUT term TEST from destination-address 10.57.'+250+'.0/24',
#                     'set firewall family inet filter SCAL-OUT term TEST then accept'
#                 ]

# print(str(informs[0]['ip']))
# print(informs[0]['ip'].split('.')[2])


for inform in informs:

    ## set commands
    cClass = str(inform['ip'].split('.')[2])
    config_commands = [ 
                    # 'set interfaces ge-0/0/10 description " ## Test 5 ## "',
                    # 'set interfaces ge-0/0/11 description " ## Test 6 ## "',
                    'set firewall family inet filter SCAL-IN term TEST from source-address 10.57.'+cClass+'.0/24',
                    'set firewall family inet filter SCAL-IN term TEST from destination-address 10.52.31.152',
                    'set firewall family inet filter SCAL-IN term TEST then accept',
                    'set firewall family inet filter SCAL-OUT term TEST from source-address 10.52.31.152/32',
                    'set firewall family inet filter SCAL-OUT term TEST from destination-address 10.57.'+cClass+'.0/24',
                    'set firewall family inet filter SCAL-OUT term TEST then accept'
    ]


    ## connect to device (Switch, Server, ...)
    net_connect = ConnectHandler(**inform)

    ## enter the command ( set ~~~ )
    edit = net_connect.send_config_set(config_commands, exit_config_mode=False)
    # print(edit)

    ## current prompt status
    output = net_connect.find_prompt()
    # print(output)

    ## enter the command (show | compare)
    compare = net_connect.send_config_set(mycommand, exit_config_mode=False)
    print(compare)

    ## commit
    com_output = net_connect.commit()
    print(com_output)
