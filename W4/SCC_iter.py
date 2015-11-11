##Implement Kosaraju Algm iteratively

import datetime
import pandas
print datetime.datetime.now().time()

DF = pandas.read_csv("SCC1.txt", sep = " ", names = ["to", "from"])
nnode = max(DF.max())
nedge = DF.shape[0]

class node:
      def __init__(self, adj, index, nnbr):
            self.adj = adj
            self.index = index
            self.nnbr = nnbr

Graphfor = [node([],0,0) for i in range(nnode+1)]
Graphbac = [node([],0,0) for i in range(nnode+1)]
print datetime.datetime.now().time()


for (index, row) in DF.iterrows():
      node1, node2 = row
      Graphfor[node1].adj.append(node2)
      Graphfor[node1].nnbr += 1
      Graphbac[node2].adj.append(node1)
      Graphbac[node2].nnbr += 1

print datetime.datetime.now().time()

def DFS_LOOP(Graph):
      global t,s  ##create a global variable
      t = 0
      s = None
      for nodeindex in range(nnode,1,-1):
            vertex = nodelabel[nodeindex]
            if not explored[vertex]:
                  s = vertex
                  explored[vertex] = 1
                  nodestack = [vertex]
                  while len(nodestack):
                        lastnode = nodestack[-1]
                        if Graph[lastnode].index == Graph[lastnode].nnbr:
                              del nodestack[-1]
                              t += 1
                              finishing[lastnode] = t
                              leader[lastnode] = s
                        else:
                              newnode = Graph[lastnode].adj[Graph[lastnode].index]
                              Graph[lastnode].index += 1
                              if not explored[newnode]:
                                    explored[newnode] = 1
                                    nodestack.append(newnode)

explored = [0]*(nnode+1)
leader = [-1]*(nnode+1)
finishing = [0]*(nnode+1)
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
