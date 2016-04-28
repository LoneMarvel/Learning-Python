#!c:\python34\python

tstList = []
inVar = 'y'
while(inVar == 'y'):
     print('Type Value For List --> ')
     listVar = input()
     tstList += [listVar]
     print('Continue (0 to Exit) --> ')
     inVar = input()

for i in range(len(tstList)):
	print('List Item --> ' + str(i) + ' Value --> ' + tstList[i])