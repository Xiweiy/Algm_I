##count inversions
readfile = open('IntegerArray.txt','r')
numbers = readfile.readlines()
numbers = [int(i.rstrip("\r\n")) for i in numbers]

totallength = len(numbers)
print totallength
def CountInversion(inputlist, inputlength):
      if inputlength==1:
            return inputlist, 0
      elif inputlength==2:
            if inputlist[0] < inputlist[1]:
                  return inputlist, 0
            else:
                  return inputlist[::-1], 1
      else:
            middle = inputlength/2
            left_half = inputlist[:middle]
            right_half = inputlist[middle:]
            sortedleft, x = CountInversion(left_half, middle)
            sortedright, y = CountInversion(right_half, (inputlength - middle))
            sortedarray, z = MergeInversion(sortedleft, sortedright, inputlength)
            print x+y+z
            return sortedarray, x+y+z

def MergeInversion(left, right, length):
      print left, right, length
      m = 0
      n = 0
      leftsize = length/2
      rightsize = length - leftsize
      sortedarray = []
      countInv = 0
      for i in range(length):
            if m == leftsize:
                  sortedarray = sortedarray + right[n:rightsize]
                  return sortedarray, countInv
            elif n == rightsize:
                  sortedarray = sortedarray + left[m:leftsize]
                  return sortedarray, countInv
            elif left[m] < right[n]:
                  sortedarray.append(left[m])
                  m += 1
            else:
                  sortedarray.append(right[n])
                  countInv = countInv + (leftsize - m)
                  n += 1
      
CountInversion(numbers, totallength)
