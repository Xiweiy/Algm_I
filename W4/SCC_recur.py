##This recursive Kosaraju Algm works all right on small datasets
##But exceed maximum recursive call depth

import datetime
import pandas
import sys
sys.setrecursionlimit(70000)  ##allocate more space for recursive depth, not work for our dataset
print datetime.datetime.now().time()

DF = pandas.read_csv("practice4.txt", sep = " ", names = ["to", "from", 'blank'])
nnode = int(max(DF.max()))

class node:
      def __init__(self, adj):
            self.adj = adj

infile = open("practice4.txt", "r")
infilelist = infile.readlines()
nedge = len(infilelist)

Graphfor = [node([]) for i in range(nnode+1)]
Graphbac = [node([]) for i in range(nnode+1)]
print datetime.datetime.now().time()

for i in infilelist:
      node1, node2 = i.rstrip("\n").split(" ")[:2]
      Graphfor[int(node1)].adj.append(node2)
      Graphbac[int(node2)].adj.append(node1)
print datetime.datetime.now().time()


def DFS(Graph, stnode):
      global t,s
      print stnode
      explored[stnode] = 1
      leader[stnode] = s
      for outnode in Graph[stnode].adj:
            if not explored[int(outnode)]:
                  DFS(Graph, int(outnode))
      t += 1
      finishing[stnode] = t


def DFS_LOOP(Graph):
      global t,s  ##create a global variable
      t = 0
      s = None
      for nodeindex in range(nnode,1,-1):
            #print nodeindex
            vertex = nodelabel[nodeindex]
            if not explored[vertex]:
                  s = vertex
                  DFS(Graph, vertex)



explored = [0]*(nnode+1)
leader = [-1]*(nnode+1)
finishing = [-1]*(nnode+1)
nodelabel = range(nnode+1)  ##the nodelabel keep track of the position of each node, especailly useful in the 2nd pass of DFS

DFS_LOOP(Graphbac)
print datetime.datetime.now().time()


for i in range(1,nnode+1):
      newid = finishing[i]
      nodelabel[newid] = i  ##Create the new nodelabel list based on their finishing time
      
explored = [0]*(nnode+1)
leader = [-1]*(nnode+1)
DFS_LOOP(Graphfor)

print datetime.datetime.now().time()

s1 = pandas.Series(leader[1:])
print s1.value_counts()
