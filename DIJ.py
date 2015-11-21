##Dijkstra's Algm

class node:
      def __init__(self, neighbors, lengths):
            self.neighbors = neighbors
            self.lengths = lengths

##Simple Implementation
#inputfile = open("dijkstraData.txt", "r")
inputfile = open('practice3.txt', 'r')
inputlist = inputfile.readlines()

nnode = len(inputlist)
nodes = [node([], []) for i in range(nnode+1)]

for line in inputlist:
      #adjlist = line.rstrip("\t\r\n").split("\t")
      adjlist = line.rstrip("\n").split(" ")
      curnode = int(adjlist[0])
      nghbrs = []
      lgths = []
      for each_edge in adjlist[1:]:
            #print each_edge
            nghbr, length = each_edge.split(",")
            nghbrs.append(int(nghbr))
            lgths.append(int(length))
            nodes[curnode]= node(nghbrs, lgths)
      
##initialize
X = [1]
V = range(2,nnode+1)
A = [0]+[1000000]*(nnode-1)

while len(X) != nnode:
      #print X
      minlength = 1000000
      minindex = None
      v = None
      for each_x in X:
            #print each_x
            curnode = nodes[each_x]
            curngbrs = curnode.neighbors
            curlgths = curnode.lengths
            #print curngbrs
            #print curlgths
            for index in range(len(curngbrs))[::-1]:
                  #print curngbrs[index], curlgths[index]
                  if curngbrs[index] in X:
                        nodes[each_x].neighbors.pop(index)
                        nodes[each_x].lengths.pop(index)
                  else:
                        if A[each_x-1] + curlgths[index] < minlength:
                              minlength = A[each_x-1] + curlgths[index]
                              minindex = curngbrs[index]
                              v = each_x
      X.append(minindex)
      A[minindex-1] = minlength
      #print A[minindex-1], minindex, each_x

print A
      
                        
                        
                        
