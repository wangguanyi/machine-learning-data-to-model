import sys
import numpy
import random
import matplotlib.pyplot as plt
from pylab import *

covariancematrix=numpy.eye(4,4)
umean=numpy.ones(4).T	

class priorWeight(object):
	"""docstring for priorWeight"""
	u=umean
	cov=covariancematrix
	step=0
	length=0
	def __init__(self, step):
		super(priorWeight, self).__init__()
		self.step = step


class posteriorWeight(object):
	"""docstring for posteriorWeight"""
	u=umean
	cov=covariancematrix
	step=0
	length=0
	def __init__(self, step):
		super(posteriorWeight, self).__init__()
		self.step = step

class Yt(object):
	"""docstring for Yt"""
	u=0
	var=0
	step=0
	length=0
	def __init__(self, step):
		super(Yt, self).__init__()
		self.step = step


class Xt(object):
	"""docstring for Xt"""
	def __init__(self, value, step):
		super(Xt, self).__init__()
		self.step = step
		self.value=value

		

def initial(datamatrix):
	covariancematrix=numpy.eye(4,4)
	umean=numpy.ones(4).T
	priorweight=[]
	posteriorweight=[]
	yt=[]	
	xt=[]
	for i in range(0,10000):
		priorweight.append(priorWeight(i))
		#print priorweight[i].cov
		posteriorweight.append(posteriorWeight(i))
		yt.append(Yt(i))
		xt.append(Xt(datamatrix[i,1:4],datamatrix[i,0]))
	priorweight=numpy.array(priorweight)
	posteriorweight=numpy.array(posteriorweight)
	yt=numpy.array(yt)
	xt=numpy.array(xt)
	return priorweight,posteriorweight,xt,yt


def readFile():
	data = open("stocks.txt","r")
	datalist = data.readlines()
	linecount=0
	#print len(datalist)
	infodata=[] #1000*5 matrix, the 1st column is the index of each data, the 2nd column is the data of A, 3rd B, 4th C, 5th D
	for line in datalist:
		linecount=linecount+1
		line=line.replace("\n","").split(",")
		if linecount>=3 and linecount<=10002:
			infodata.append([int(line[0])-1,float(line[1]),float(line[2]),float(line[3]),float(line[4]),float(line[5])])
	#print len(infodata)
	#print infodata[9999]
	datamatrix=numpy.array(infodata)
	return datamatrix

#w is 4*1, x^T is 1*4

# the model for question 1
#def calculate1():




def main(argv):
	
	datamatrix=readFile()
	priorweight,posteriorweight,xt,yt=initial(datamatrix)


	figure(1)
	plt.plot(datamatrix[:,0],datamatrix[:,1:5])
	#plt.plot(datamatrix[:,0],datamatrix[:,1:4],'.')
	figure(2)
	plt.plot(datamatrix[:,0],datamatrix[:,5])
	#plt.show()
	a=numpy.array([[1,1,1],[0,1,0],[0,0,1]])
	b=numpy.array([2,3,8])
	x=numpy.linalg.solve(a,b)
	print x

if __name__ == "__main__":
     main(sys.argv)