import numpy as np
from string import rstrip
import argparse
import sys

def main(argv):
    loadData(argv)
    dxreader_z()

def loadData(argv):
	global inLfile
	global inPfile
	global inWfile
	global outfile
	parser = argparse.ArgumentParser(description='takes a protein water and lipid dx file and gives average along z')
	parser.add_argument('-il','--inputLipidfile',help='input lipid file name (a dx file)', required=True)
	parser.add_argument('-ip','--inputProteinfile',help='input protein file name (a dx file)', required=True)
	parser.add_argument('-iw','--inputWaterfile',help='input water file name (a dx file)', required=True)
	parser.add_argument('-o','--outputfile',help='output file name (a txt file, no need to include extension', required=True)

	args = vars(parser.parse_args())
	inLfile=args['inputLipidfile']
	inPfile=args['inputProteinfile']
	inWfile=args['inputWaterfile']
	outfile=args['outputfile']

def dxreader_z():
	global inLfile
	global inPfile
	global inWfile
	global outfile
	with open(inLfile, "r") as ins:
		dxLfile = []
		for line in ins:
			if line.startswith("object 1"):
				line=rstrip(line)
				line=line.split()
				xLnum=int(line[-3])
				yLnum=int(line[-2])
				zLnum=int(line[-1])
			elif line.startswith("origin"):
				line=rstrip(line)
				line=line.split()
				xLstart=int(round(float(line[-3])))
				yLstart=int(round(float(line[-2])))
				zLstart=int(round(float(line[-1])))

			elif line[0].isdigit()==True:
				line=rstrip(line)
				line=line.split()
				for y in line:
					dxLfile.append(y)

	with open(inPfile, "r") as ins:
		dxPfile = []
		for line in ins:
			if line.startswith("object 1"):
				line=rstrip(line)
				line=line.split()
				xPnum=int(line[-3])
				yPnum=int(line[-2])
				zPnum=int(line[-1])
			elif line.startswith("origin"):
				line=rstrip(line)
				line=line.split()
				xPstart=int(round(float(line[-3])))
				yPstart=int(round(float(line[-2])))
				zPstart=int(round(float(line[-1])))

			elif line[0].isdigit()==True:
				line=rstrip(line)
				line=line.split()
				for y in line:
					dxPfile.append(y)

	with open(inWfile, "r") as ins:
		dxWfile = []
		for line in ins:
			if line.startswith("object 1"):
				line=rstrip(line)
				line=line.split()
				xWnum=int(line[-3])
				yWnum=int(line[-2])
				zWnum=int(line[-1])
			elif line.startswith("origin"):
				line=rstrip(line)
				line=line.split()
				xWstart=int(round(float(line[-3])))
				yWstart=int(round(float(line[-2])))
				zWstart=int(round(float(line[-1])))
			elif line[0].isdigit()==True:
				line=rstrip(line)
				line=line.split()
				for y in line:
					dxWfile.append(y)



	#make origins positive to not screw up arrays
	movex=min(xLstart,xPstart,xWstart)
	movey=min(yLstart,yPstart,yWstart)
	movez=min(zLstart,zPstart,zWstart)

	xLstart=xLstart+abs(movex)
	xPstart=xPstart+abs(movex)
	xWstart=xWstart+abs(movex)

	yLstart=yLstart+abs(movey)
	yPstart=yPstart+abs(movey)
	yWstart=yWstart+abs(movey)

	zLstart=zLstart+abs(movez)
	zPstart=zPstart+abs(movez)
	zWstart=zWstart+abs(movez)

	xLend=xLstart+xLnum
	yLend=yLstart+yLnum
	zLend=zLstart+zLnum

	xPend=xPstart+xPnum
	yPend=yPstart+yPnum
	zPend=zPstart+zPnum

	xWend=xWstart+xWnum
	yWend=yWstart+yWnum
	zWend=zWstart+zWnum




	xdim=max(xLstart+xLnum,xPstart+xPnum,xWstart+xWnum)
	ydim=max(yLstart+yLnum,yPstart+yPnum,yWstart+yWnum)
	zdim=max(zLstart+zLnum,zPstart+zPnum,zWstart+zWnum)



	denL=np.zeros((xdim,ydim,zdim))
	denP=np.zeros((xdim,ydim,zdim))
	denW=np.zeros((xdim,ydim,zdim))



	i=0
	for x in range(xLstart,xLend):
		for y in range(yLstart,yLend):
			for z in range(zLstart,zLend):
				denL[x,y,z]=dxLfile[i]
				i=i+1


	i=0
	for x in range(xPstart,xPend):
		for y in range(yPstart,yPend):
			for z in range(zPstart,zPend):
				denP[x,y,z]=dxPfile[i]
				i=i+1


	i=0
	for x in range(xWstart,xWend):
		for y in range(yWstart,yWend):
			for z in range(zWstart,zWend):
				denW[x,y,z]=dxWfile[i]
				i=i+1

	denWadj=np.zeros((xWend-xWstart,yWend-yWstart,zWend-zWstart))


	#mean zero values for all, protein and lipid values nan
	for i in range(xWstart,xWend):
		for j in range(yWstart,yWend):
			for k in range(zWstart,zWend):
				denWadj[i-xWstart,j-yWstart,k-zWstart]=denW[i,j,k]
				if denL[i,j,k] > 0.0:
					denWadj[i-xWstart,j-yWstart,k-zWstart]=np.NaN				
				elif denP[i,j,k] > 0.0:
					denWadj[i-xWstart,j-yWstart,k-zWstart]=np.NaN


	zden=np.nanmean(denWadj,axis=(0,1))

	np.savetxt(outfile+'.txt',zden)

if __name__ == "__main__":
    main(sys.argv[1:])
