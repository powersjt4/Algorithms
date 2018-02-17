"""
This is an implementation of an activity scheduler 
"""
import itertools
from sys import argv
from collections import deque
script, inFilename = argv
#inFile = open(inFilename, "r")
G = {}
wArr = []
eArr = []

with open(inFilename, "r") as inFile:
	numW = int(inFile.readline())
	for i in range(0,numW):
		wArr.append(inFile.readline())
	wArr = [x.rstrip() for x in wArr]
	G = dict((x,[]) for x in wArr)
	numE = int(inFile.readline())
	for line in range(0, numE):
		edge = inFile.readline().split()
		print edge[0]
		G[edge[0]].append(edge[1])
		G[edge[1]].append(edge[0])
#print wArr
#for key in G:
#    G[key].append([0,2])
G = dict((x,white) for x in wArr)
babs = []
heels = []
Q = deque([])
Q.append(wArr[0])
print Q
while len(Q) != 0:
    u = Q.popleft()
        for x in G[u]  
"""
GoodBadGuys(list of wrestlers, pairs of rivalries)
Build an adjacency list representation for G = (V, E) such that each wrestler
corresponds to a vertex in V and each edge in E = (V1, V2) represents a rivalry between
the wrestlers associated with V1 and V2
 for each vertex u is in V [G]
    do color [u] == WHITE
 for each vertex u in in V [G]
    do if color [u] = WHITE
        then guy==BFS-GOOD-BAD(G, u, guy)
 return guy
BFS-GOOD-BAD(G, s, guy)
 color[s] == Gray
 guy[s] == GOOD
 Q == nil 
 ENQUEUE(Q, s)
 while Q not empty 
    do u == DEQUEUE(Q)
        for each v is in Adj[u]
            do if color[v] = GRAY and guy[v] = guy[u]
                then return FAIL
            if color[v] = WHITE
                then color[v] == GRAY
                if guy[u] = GOOD
                    then guy[v] == BAD
                    else guy[v] == GOOD
                ENQUEUE(Q, v)
        color[u] == BLACK
 return guy
"""