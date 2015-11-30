##Heap Median Maintenance

numfile = open('Median.txt', 'r')
numlist = [int(i.rstrip('\r\n')) for i in numfile.readlines()]

class heap_low:
      def __init__(self, array, length):
            self.array = array
            self.length = length

      def insert(self, newnum):
            self.array.append(newnum)
            if self.length:
                  child_pos = self.length
                  child = self.array[-1]
                  parent_pos = (child_pos -1)/2
                  parent = self.array[parent_pos]
                  while parent < child and parent_pos >=0:
                        self.array[parent_pos], self.array[child_pos] = child, parent
                        child_pos = parent_pos
                        parent_pos = (child_pos -1)/2
                        if parent_pos >= 0:
                              parent = self.array[parent_pos]
            self.length += 1

      def extractmax(self):
            self.array[0] = self.array[-1]
            self.array.pop(-1)
            self.length -= 1
            if self.length > 1:
                  parent_pos, child_pos = 0, 1
                  parent, child1 = self.array[0], self.array[1]
                  if self.length == 2 and parent < child1:  #base case
                        self.array[0], self.array[1] = child1, parent
                  elif self.length > 2:
                        child2 = self.array[2]
                        while (parent < child1 or parent < child2) and child_pos < self.length-1:
                              if child1 > child2:
                                    self.array[parent_pos], self.array[child_pos] = child1, parent  #swap parent and child1
                                    parent_pos = child_pos
                              else:
                                    self.array[parent_pos], self.array[child_pos+1] = child2, parent  #swap parent and child2
                                    parent_pos = child_pos +1
                              parent = self.array[parent_pos]
                              child_pos = parent_pos*2 +1
                              if child_pos == self.length-1:  #only 1 child
                                    child1 = self.array[-1]
                                    if parent < child1:
                                          self.array[parent_pos], self.array[child_pos] = child1, parent  #swap parent and child1
                              elif child_pos < self.length-1:
                                    child1, child2 = self.array[child_pos], self.array[child_pos+1]



class heap_high:
      def __init__(self, array, length):
            self.array = array
            self.length = length

      def insert(self, newnum):
            self.array.append(newnum)
            if self.length:
                  child_pos = self.length
                  child = self.array[-1]
                  parent_pos = (child_pos -1)/2
                  parent = self.array[parent_pos]
                  while parent > child and parent_pos >=0:
                        self.array[parent_pos], self.array[child_pos] = child, parent
                        child_pos = parent_pos
                        parent_pos = (child_pos -1)/2
                        if parent_pos >= 0:
                              parent = self.array[parent_pos]
            self.length += 1

      def extractmin(self):
            self.array[0] = self.array[-1]
            self.array.pop(-1)
            self.length -= 1
            if self.length > 1:
                  parent_pos, child_pos = 0, 1
                  parent, child1 = self.array[0], self.array[1]
                  if self.length == 2 and parent > child1:  #base case
                        self.array[0], self.array[1] = child1, parent
                  elif self.length > 2:
                        child2 = self.array[2]
                        while (parent > child1 or parent > child2) and child_pos < self.length-1:
                              if child1 < child2:
                                    self.array[parent_pos], self.array[child_pos] = child1, parent  #swap parent and child1
                                    parent_pos = child_pos
                              else:
                                    self.array[parent_pos], self.array[child_pos+1] = child2, parent  #swap parent and child2
                                    parent_pos = child_pos +1
                              parent = self.array[parent_pos]
                              child_pos = parent_pos*2 +1
                              if child_pos == self.length-1:  #only 1 child
                                    child1 = self.array[-1]
                                    if parent > child1:
                                          self.array[parent_pos], self.array[child_pos] = child1, parent  #swap parent and child1
                              elif child_pos < self.length-1:
                                    child1, child2 = self.array[child_pos], self.array[child_pos+1]                                    
                        
 ##initialize
lowerhalf = heap_low([],0)
upperhalf = heap_high([],0)
mediansum = 0
counter = 0
for i in numlist:
      if lowerhalf.length==upperhalf.length==0:
            lowerhalf.insert(i)
      elif lowerhalf.length == upperhalf.length:
            if i <= lowerhalf.array[0]:
                  lowerhalf.insert(i)
            else:
                  upperhalf.insert(i)
      elif lowerhalf.length < upperhalf.length:
            if i <= upperhalf.array[0]:
                  lowerhalf.insert(i)
            else:
                  lowerhalf.insert(upperhalf.array[0])
                  upperhalf.extractmin()
                  upperhalf.insert(i)
      else:
            if i >= lowerhalf.array[0]:
                  upperhalf.insert(i)
            else:
                  upperhalf.insert(lowerhalf.array[0])
                  lowerhalf.extractmax()
                  lowerhalf.insert(i)
      counter += 1
      if counter %2 and lowerhalf.length < upperhalf.length:
            mediansum += upperhalf.array[0]
      else:
            mediansum += lowerhalf.array[0]
#      print counter, mediansum, lowerhalf.length, lowerhalf.array, upperhalf.length, upperhalf.array
print mediansum
            
      
