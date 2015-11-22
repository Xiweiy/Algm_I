##Dijkstra's Algm

class node:
      def __init__(self, neighbors, arclengths, key, heappos):
            self.neighbors = neighbors
            self.arclengths = arclengths
            self.key = key
            self.heappos = heappos
            

class heap:
      def __init__(self, indexlist, length):
            self.indexlist = indexlist
            self.length = length
            
      def bubbleup(self,child_pos):
            child = self.indexlist[child_pos]
            parent_pos = (child_pos -1)/2
            #print 'parent', parent_pos
            if parent_pos >= 0:
                  parent = self.indexlist[parent_pos]
            else:
                  return
            while nodes[child].key < nodes[parent].key and parent_pos >=0:
                  self.indexlist[parent_pos], self.indexlist[child_pos] = child, parent  #swap child and parent position
                  nodes[child].heappos, nodes[parent].heappos = parent_pos, child_pos
                  child_pos = parent_pos
                  child = self.indexlist[child_pos]
                  parent_pos = (child_pos -1)/2
                  if parent_pos >= 0:
                        parent = self.indexlist[parent_pos]
            
      def insert(self, new_index):
            self.indexlist.append(new_index)
            nodes[new_index].heappos = self.length+1
            #print self.indexlist, self.length
            if self.length:
                  child_pos = self.length
                  child = self.indexlist[-1]
                  #print 'child', child_pos, child
                  self.bubbleup(child_pos)
            self.length += 1

      def bubbledown(self, parent_pos):
            parent = self.indexlist[parent_pos]
            child_pos = parent_pos*2 +1
            if child_pos >= self.length:
                  return
            elif child_pos + 1 >= self.length:
                  child = self.indexlist[child_pos]
                  if nodes[child].key < nodes[parent].key:
                        self.indexlist[parent_pos], self.indexlist[child_pos] = child, parent  #swap child and parent position
                        nodes[child].heappos, nodes[parent].heappos = parent_pos, child_pos
            else:
                  child1, child2 = self.indexlist[child_pos:(child_pos+2)]
                  minchildkey = min(nodes[child1].key, nodes[child2].key)
                  if minchildkey < nodes[parent].key:
                        if minchildkey == nodes[child1].key:
                              self.indexlist[parent_pos], self.indexlist[child_pos] = child1, parent
                              nodes[child1].heappos, nodes[parent].heappos = parent_pos, child_pos
                              parent_pos = child_pos
                        else:
                              self.indexlist[parent_pos], self.indexlist[child_pos+1] = child2, parent
                              nodes[child2].heappos, nodes[parent].heappos = parent_pos, child_pos+1
                              parent_pos = child_pos + 1
                        self.bubbledown(parent_pos)
                  
      def deletemin(self):
            self.indexlist[0] = self.indexlist[-1]
            nodes[self.indexlist[0]].heappos = 0
            self.indexlist.pop(-1)
            self.length -= 1
            if self.length >1:
                  parent_pos = 0
                  self.bubbledown(parent_pos)

      def changed_values(self, pos):
            newnode = self.indexlist[pos]
            parent_pos = (pos -1)/2
            if parent_pos >=0:
                  parent = self.indexlist[parent_pos]
                  if nodes[newnode].key < nodes[parent].key: 
                        self.bubbleup(pos)
                  else:
                        self.bubbledown(pos)

            
            


##implement with heap
inputfile = open("dijkstraData.txt", "r")
#inputfile = open('practice.txt', 'r')
inputlist = inputfile.readlines()

nnode = len(inputlist)
nodes = [node([], [], 100000, 0) for i in range(nnode+1)]

for line in inputlist:
      adjlist = line.rstrip("\t\r\n").split("\t")
      #adjlist = line.rstrip("\n").split(" ")
      curnode = int(adjlist[0])
      nghbrs = []
      lgths = []
      for each_edge in adjlist[1:]:
            #print each_edge
            nghbr, length = each_edge.split(",")
            nghbrs.append(int(nghbr))
            lgths.append(int(length))
      nodes[curnode].neighbors = nghbrs
      nodes[curnode].arclengths = lgths
      
      
      
##initialize
X = [1]
V_X = heap([2],1)
A = [0]+[1000000]*(nnode-1)

##Construct the initial heap
for i in range(3,nnode+1):
      cur_node = nodes[i]
      key = 1000000
      for j in range(len(cur_node.neighbors)):
            if cur_node.neighbors[j] in X and cur_node.arclengths[j] < key:
                  key = cur_node.arclengths[j]
      nodes[i].key = key
      #print key
      V_X.insert(i)


while len(X) != nnode:
      minindex = V_X.indexlist[0]
      minlength = nodes[minindex].key
      V_X.deletemin()
      X.append(minindex)
      A[minindex-1] = minlength

      #update key
      nodes_to_change = nodes[minindex].neighbors
      nodes_lengths = nodes[minindex].arclengths
      for each_node,each_length in zip(nodes_to_change, nodes_lengths):
            if each_node in V_X.indexlist:
                  nodes[each_node].key = min(nodes[each_node].key, A[minindex-1]+each_length)
                  V_X.changed_values(nodes[each_node].heappos)

toprint = [7,37,59,82,99,115,133,165,188,197]
for i in toprint:
      print str(A[i-1])+',',
