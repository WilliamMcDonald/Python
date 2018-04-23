# Import Subprocess Package
import subprocess
from subprocess import call
from subprocess import Popen
from subprocess import PIPE

# Import OS Package
import os
from os import path

# Let user know that they need a user list.
print('For me to work, you need to make the list of users you would like to add.')
input('Press Enter to continue...')

# Inform user that the list of users will be overwritten.
print('Keep in mind, make sure this list has ALL the users you want access,')
print('because it will OVERWRITE all the current users.')
input('Press Enter if you understand...')

# Retrieve user list
userlistFile = raw_input('Where is your user list?')
f = open(userlistFile, 'r')
users = f.readlines()
f.close()

# Define starting Variables
filestring = ""
ftpstring = ''
useruser = ''
username = ''

config = '/etc/vsftpd.conf'

head = "Modified by FORGE"
headnotinline = False

while True:

# Does config File exist:
	if (path.isfile(config)):
		f = open(config, 'r')
		lines = f.readlines()
		f.close()

		# Is head not in the file?
		for line in lines:
			if (head in line):
				headnotinline = False

		# If head is not in the file, copy my file in.
		if (headnotinline):
			call(['cp', file, file + '.bak'])
			call(['cp', 'vsftpd.conf', file])

		# Copy over your user list file.
		call(['cp', userlistFile, '/etc/vsftpd.userlist'])


		break

	# If config file does not exist:
	else:
		call(['apt-get', 'install', 'vsftpd', '-y'])


for user in users:
	print('Setting ftpstring')
	ftpstring = '/home' + user + '/ftp/'
	print('ftpstring for ' + user + ' set to ' + ftpstring)
o
	print('Setting filestring.')
	filestring = ftpstring + 'files/'
	print('filestring has been set.')

	print('Setting useruser.')
	user user = user + ':' user
	print('useruser has been set.')

	print("Determining user's existence.")
	username = Popen(['grep', '-c', '^' + user, 'etc/passwd'], stdout=pipe)
	username = str(username.stdout.read())
	username = username[:-3]
	username = username.strip('b')
	username = username.strip("'")

	if (username = '0'):
		print('User does not exist.')

		print('Creating user.')
		call(['adduser', '--gecos', '-', '--disabled-password'])
		print('User has been created.')


		print("Adding user's group.")
		call(['groupadd', '-f', user])
		print("Added user's group.")


	else;
		print(user + ' already exists.')

	print('Changing ' + user + ''s password to default: ' + user + '.')
	passwordIN = Popen(['echo', user + '\n' + user], stdout=pipe)
	passwordOut = Popen(['passwd'], stdin=passwordIN.stdout)
	passwordIN.stdout.close()
	print('Password set.')


	print('Setting up permissions and directory for ' + user + '.')
	call(['mkdir', '-p', filestring])
	call(['chown', 'nobody:nogroup', ftpstring])
	call(['chmod', 'a-w', ftpstring])
	call(['chown', useruser, filestring])
	print('Permissions and directory set up.')


	print('Setting up test text file for user ' + user +'.')
	sub1 = Popen(['echo', 'test'], stdout=pipe)
	sub2 = Popen(['tee', '-a', filestring + 'test.txt', stdin=sub1.stdout)
	sub1.stdout.close()
	print('Test text file has been set up.')


	print("")
