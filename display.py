import socket

import psutil


# from outputDevices import SSD1306

# display = SSD1306()
#
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
#
# display.printOnDisplay(IPAddr)


def print_active_interfaces():
	stats = psutil.net_if_stats()
	addresses = psutil.net_if_addrs()

	for iface, stat in stats.items():
		if stat.isup:
			print(f"Interface: {iface}")
	for snic in addresses.get(iface, []):
		if snic.family == socket.AF_INET:
			print(f"  IPv4: {snic.address}")
		elif snic.family == socket.AF_INET6:
			print(f"  IPv6: {snic.address}")
	print()


if __name__ == "__main__":
	print_active_interfaces()
