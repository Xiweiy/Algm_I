##2-SUM algm w/ hash table
##use python dic

numfile = open('algo1-programming_prob-2sum.txt', 'r')
numlist = [int(i.rstrip('\n')) for i in numfile.readlines()]
numdic = {i:0 for i in numlist}

target = 0
for i in range(-10000, 10001):
      #print i, target
      for item in numdic:
            remains = i - item
            if remains in numdic and item != remains:
                  target += 1
                  break

