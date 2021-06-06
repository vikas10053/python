import netmiko
x = {"host":"192.168.137.40",
"username":"vikas",
"password":"vikas",
"device_type":"cisco_ios"}

y = netmiko.ConnectHandler(**x)

c = y.find_prompt()
commands = ("int gi0/2","ip address 10.0.0.1 255.255.255.0","no shut")
y.send_config_set(commands)
i = y.send_command("sh ip int brief")
print(i)