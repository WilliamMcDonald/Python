import subprocess
from subprocess import call

import time
from time import time

 # Change to your desired interface; DEFAULT is eth0.
interface = 'wlo1'

 # Starts timer.
start = time()

 # Initialises elapsed time to run off the bat.
elapsed = 10


while True:
	if elapsed >= 10:
		# Resets timer
		start = time()

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

	# Checks time
	stop = time()
	elapsed = stop - start
