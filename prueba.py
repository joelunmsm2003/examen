import random
import sys
from functools import reduce
import os
import glob
import datetime
from tabulate import tabulate


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


num = int(sys.argv[1])

lista = [random.randint(0, 100) for r in xrange(num)] # v1

print sorted(lista,reverse=True)[0:5]


print sorted(lista,reverse=True)[5:10]


##

print sum(lista)



###
print 'Mult'

product = reduce((lambda x, y: x * y), lista)


print product

print 'Files'


dire = os.listdir(sys.argv[2])

dire_ord = sorted(dire, key=lambda fe: os.path.getsize(sys.argv[2]+fe),reverse=True)

dire_fecha = sorted(dire, key=lambda dat: os.path.getmtime(sys.argv[2]+dat))


result=[]
python prueba.py 9 '/home/andy'

for e in dire_ord:

	#print e, os.path.getsize(sys.argv[2]+e)
	result.append([e,bcolors.OKBLUE+str(os.path.getsize(sys.argv[2]+e))+bcolors.ENDC])

print tabulate(result,headers=['file','size'])


result=[]


for e in dire_fecha:

	result.append([e,bcolors.OKBLUE+str(datetime.datetime.fromtimestamp(os.path.getmtime(sys.argv[2]+e)))+bcolors.ENDC])



print tabulate(result,headers=['file','date'])
