#!c:\python34\python

import webbrowser, sys

if len(sys.argv) < 2:
	print('Usage: mapit address')
	sys.exit()
	
addr = ' '.join(sys.argv[1:])
print(addr)
webbrowser.open('https://www.google.de/maps/place/'+addr)