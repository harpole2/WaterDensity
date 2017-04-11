import numpy as np
from string import rstrip
import argparse
import sys

def main(argv):
    loadData(argv)
    dxreader_z()

def loadData(argv):
	global infile
	global outfile
	parser = argparse.ArgumentParser(description='takes a dx file and gives average along z')
	parser.add_argument('-i','--inputfile',help='input file name (a dx file)', required=True)
	parser.add_argument('-o','--outputfile',help='output file name (a txt file, no need to include extension', required=True)

	args = vars(parser.parse_args())
	infile=args['inputfile']
	outfile=args['outputfile']

def dxreader_z():
	global infile
	global outfile
	with open(infile, "r") as ins:
		dxfile = []
		for line in ins:
			if line.startswith("object 1"):
				line=rstrip(line)
				line=line.split()
#				print line
				xnum=line[-3]
				ynum=line[-2]
				znum=line[-1]

			if line[0].isdigit()==True:
				line=rstrip(line)
				line=line.split()
				for y in line:
					dxfile.append(y)

	xnum=int(xnum)
	ynum=int(ynum)
	znum=int(znum)

	den=np.zeros((xnum,ynum,znum))
	i=0
	for x in range(0,xnum):
		for y in range(0,ynum):
			for z in range(0,znum):
				den[x,y,z]=dxfile[i]
				i=i+1

	zden=np.mean(den,axis=(0,1))

	np.savetxt(outfile+'.txt',zden)

if __name__ == "__main__":
    main(sys.argv[1:])
