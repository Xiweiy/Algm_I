##count comparisons
readfile = open('QuickSort.txt','r')
numbers = readfile.readlines()
numbers = [int(i.rstrip("\r\n")) for i in numbers]
numbers1 = numbers[:]  ##make a deep copy every time before a different sorting algm is implemented.

########################################################################
### QSort1 and partition1 use the first element as pivot, a is array####
########################################################################

## sorting only, w/0 counting comparison 
def QSort1(a):
      if len(a) <1:
            return a
      else:
            pivot = a[0]
            left, right = partition1(a, len(a))
            return QSort1(left) + [pivot] + QSort1(right)

     
def partition1(a, n):
      pivot = a[0]
      j = 1
      for i in range(1,n):
            if a[i] < pivot:
                  a[i], a[j] = a[j], a[i]
                  j += 1
      a[0], a[j-1] = a[j-1], a[0]
      return a[:j-1], a[j:]
                  
#sortarray = QSort1(numbers)
#print sortarray


##QSort12 will include comparison, still use partition1()
def QSort12(a):
      ncPartition = len(a) - 1   #number of count during partition 
      if len(a) <1:
            return a, 0
      else:
            pivot = a[0]
            left, right = partition1(a, len(a))
            left, leftcount = QSort12(left)
            right, rightcount = QSort12(right)
            return left + [pivot] + right, ncPartition + leftcount + rightcount
print QSort12(numbers1)[1]


numbers1 = numbers[:]
##########################################################################
############QSort2 use the final element as pivot element##################
##########################################################################
def QSort2(a):
      n = len(a)
      ncPartition = len(a) - 1   #number of count during partition 
      if len(a) <1:
            return a, 0
      else:
            pivot = a[n-1]
            left, right = partition2(a, n)
            left, leftcount = QSort2(left)
            right, rightcount = QSort2(right)
            return left + [pivot] + right, ncPartition + leftcount + rightcount

def partition2(a, n):
      a[0],a[n-1] = a[n-1],a[0]
      pivot = a[0]
      j = 1
      for i in range(1,n):
            if a[i] < pivot:
                  a[i], a[j] = a[j], a[i]
                  j += 1
      a[0], a[j-1] = a[j-1], a[0]
      return a[:j-1], a[j:]
print QSort2(numbers1)[1]

numbers1 = numbers[:]
##########################################################################
#####QSort3 use the median of first, last, and middle element as pivot####
##########################################################################

from numpy import median
def QSort3(a):
      n = len(a)
      middle = (n-1)/2
      ncPartition = len(a) - 1   #number of count during partition 
      if len(a) <1:
            return a, 0
      else:
            pivot = median([a[0],a[n-1],a[middle]])
            left, right = partition3(a, n)
            left, leftcount = QSort3(left)
            right, rightcount = QSort3(right)
            return left + [pivot] + right, ncPartition + leftcount + rightcount

def partition3(a, n):
      middle = (n-1)/2
      pivot = median([a[0],a[n-1],a[middle]])   
      if pivot == a[n-1]:
            a[0],a[n-1] = a[n-1],a[0]
      elif pivot == a[middle]:
            a[0],a[middle] = a[middle],a[0]
      j = 1
      for i in range(1,n):
            if a[i] < pivot:
                  a[i], a[j] = a[j], a[i]
                  j += 1
      a[0], a[j-1] = a[j-1], a[0]
      return a[:j-1], a[j:]
print QSort3(numbers1)[1]
