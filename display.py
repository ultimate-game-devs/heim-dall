import socket

import psutil

from helper.outputDevices import SSD1306

display = SSD1306()

text = ''

stats = psutil.net_if_stats()
addresses = psutil.net_if_addrs()

for iface, stat in stats.items():
	if stat.isup:
		for snic in addresses.get(iface, []):
			if snic.family == socket.AF_INET:
				text = snic.address

display.print_on_display(text)
