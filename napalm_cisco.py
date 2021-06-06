
from napalm import get_network_driver
import napalm
import json

x = napalm.get_network_driver("ios")

z = x(hostname="192.168.137.40",username="vikas",password="vikas")

z.open()

print(z.compare_config())