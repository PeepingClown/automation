import os
import sys

saved_profiles = os.popen('netsh wlan show profiles').read()

# print(saved_profiles)

preferred_ssid = input('Enter the preferred wifi for your connection:')

response = os.popen('netsh wlan disconnect').read()

# print(response)

if preferred_ssid not in saved_profiles:
	print('Profile for '+preferred_ssid+' not saved in the system')
	print('Sorry, can not establish connection')
	sys.exit()

else:
	print('Profile for '+preferred_ssid+' is saved in system')

while True:
	avail = os.popen('netsh wlan show networks').read()
	if preferred_ssid in avail:
		print('Found Network')
		break

print('----------Connecting----------')
resp = os.popen('netsh wlan connect name="'+preferred_ssid+'"').read()



