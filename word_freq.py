#!/usr/bin/python3
import sys	

filename=sys.argv[1]
number=int(sys.argv[2])

D = {}

with open(filename, 'r') as fr:
	for line in fr:
		line = line.replace('.',' ').replace(',',' ').replace('!',' ').replace('?',' ').replace('@',' ').replace('#',' ').replace('$',' ').replace('%',' ').replace('^',' ').replace('&',' ').replace('*',' ').replace('(',' ').replace(')',' ').replace('-',' ').replace('_',' ').replace('+',' ').replace('=',' ').replace('{',' ').replace('}',' ').replace('[',' ').replace(']',' ').replace(':',' ').replace(';',' ').replace("'",' ').replace('"',' ').replace('<',' ').replace('>',' ').replace('/',' ')
		for word in line.lower().split():	
			if word in D:
				D[word] += 1
			else:
				D[word] = 1	
			 
D_list = sorted(D.items(), key=lambda x: x[1], reverse=True)

for i in D_list[:number]:
	print("%-5s%8d" % (i[0],i[1]))
