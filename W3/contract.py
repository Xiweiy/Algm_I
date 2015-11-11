import numpy as np
from copy import deepcopy
contractFile = open("kargerMinCut.txt", "r")
contractList = contractFile.readlines()
contractList = [i.rstrip("\t\r\n").split("\t") for i in contractList]
#contractList = [i.rstrip("\n").split(" ") for i in contractList]
contractDic = {i[0]:i[1:] for i in contractList}

edgelist = [[i[0],j] for i in contractList for j in i[1:]]

def ContractAlgm(vertexdic, edges):

#vertexdic = contractDic
#edges = edgelist

      while len(vertexdic) >2 :
            nedges = len(edges)
      #      print nedges
            Rind = np.random.randint(0, nedges)
      #      print Rind
            end1, end2 = edges[Rind]
      #      print end1, end2
            edges.pop(Rind)
            vertexdic[end1] = list(set(vertexdic[end1]+vertexdic[end2]))

            for i in vertexdic[end2]:
                  vertexdic[i] = [j for j in vertexdic[i] if j!= end2] + [end1]
            del vertexdic[end2]

            to_remove=[]
            for i in range(nedges-1):
                  edge = edges[i]
                  if edge[0] == end2:
                        edge[0] = end1
                  elif edge[1] == end2:
                        edge[1] = end1
                  if edge[0] == edge[1]:
                        to_remove.append(i)

            for i in to_remove[::-1]:
                  edges.pop(i)
      #      print edges, vertexdic
      return len(edges)*1.0/2  #, edges, vertexdic           

mincut = []
for i in range(1000):
      vert = deepcopy(contractDic)
      edges = deepcopy(edgelist)
      #print ContractAlgm(vert, edges)
      mincut.append(ContractAlgm(vert, edges))
print min(mincut)
