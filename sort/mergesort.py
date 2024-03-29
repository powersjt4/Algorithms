"""
This is an implementation of merge sort
from introduction to algorithms, CLRS
Other resources:
http://love-python.blogspot.com/2013/10/merge-sort-implementation-in-python.html
//www.geeksforgeeks.org/merge-sort/rint(array)
"""
           #p q r
def merge(A,l,m,r):
#    n1 = m-l+1 
#    n2 = r-m
    inf = 99999999
    L = [] 
    R = []
    L.extend(A[l : m+1])
    R.extend(A[m+1 : r+1])
    L.append(inf) # sentinal card
    R.append(inf) # = infinity
    i = 0 
    j = 0 
   # k = l 
    for k in range(l,r+1):
        if(L[i]<= R[j]):
            A[k] = L[i]
            i +=1
        else:
            A[k] = R[j]
            j+=1
 
def mergeSort(A,l,r):
    if l<r:
	m = (l+(r-1))/2
	mergeSort(A,l,m)
	mergeSort(A,m+1,r)
	merge(A,l,m,r)

#main 
input = "data.txt"
output = "merge.out"
inFile = open(input, "r")
outFile = open(output, "w")

for line in inFile:
        array = [] 
        for val in line.split():
            array.append(int(val))
	length = array.pop(0) 
        print length
        mergeSort(array,0,length-1)
        print(array)
        for item in array:
            outFile.write("%d "% item)
        outFile.write("\n")
inFile.close()
outFile.close()
