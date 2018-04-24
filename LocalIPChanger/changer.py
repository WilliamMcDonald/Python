# CHANGER.PY ZWEI NULL - 4/24

import subprocess
from subprocess import call

import time
from time import sleep

 # Change to your desired interface; DEFAULT is eth0.
interface = 'wlo1'

while True:
	print('# # # # # # #')
	print('# CHANGING  #')
	print('# # # # # # #')
	print("")

	# Changes MAC Address
	call(['ifconfig', interface, 'down'])
	call(['macchanger', '-r', interface])
	call(['ifconfig', interface, 'up'])
	print("")

	# Renews IP address
	call(['dhclient', '-r', interface])
	call(['dhclient', interface])
	print("")

	# Shows new IPV4 Addresses
	call(['ip', '-4', 'address'])
	print("")

	sleep(10)
