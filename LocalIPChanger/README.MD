Created by William 'Vulcan' McDonald.

# # # # # # # # # #
# Why it was made #
# # # # # # # # # #

  I created this program because I wanted to find a way to mess with my school's IT department. We know that they watch our class, so I thought a great way to mess with them would to be dropping IPs and picking another one up every 10 seconds. I don't know if they have noticed, because I'm not really there to see their faces, but while working on it, I found out it is a great program to run on a raspberry pi or some other infiltration device to change the IP a less common rate to lower suspicion, but the changing IP address keeps them from being able to watch the device intently.

# # # # # #
# Updates #
# # # # # #


# # # # # # # #
# Binary Run  #
# # # # # # # #

Go to Dist folder to find binary file created with pyinstaller program. Copy or move binary file to /bin folder to run via command.

If you update the python file to fit what you need (as I reccomend, for this one is set up for my personal use), update the binary file with pyinstaller via 'pyinstaller -F changer.py'. If you do not have pyinstaller, install it with 'apt-get install libc-bin binutils python-dev python-pip' to get the prerequisites (might already have them, as I did), and install the actual program with 'pip install PyInstaller'.

