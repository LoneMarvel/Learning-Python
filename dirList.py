#!c:\Python34\python

import os

dirFlag = 1
#sDir = "c:\\Users\\kterzopoulos"
sDir = os.getcwd()
print(sDir)
lDir = os.listdir(sDir)

while ( dirFlag == 0 ):
	
		for d in lDir:	
			if os.path.isdir(d):
				print('Is Directory --> ', d)