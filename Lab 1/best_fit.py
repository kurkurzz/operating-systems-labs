blockSize = [100, 500, 200, 300, 600]
processSize = [212, 417, 112, 426]

'''
BEST FIT 

Implementation:
1- Input memory blocks and processes with sizes.
2- Initialize all memory blocks as free.
3- Start by picking each process and find the
   minimum block size that can be assigned to
   current process i.e., find min(bockSize[1], 
   blockSize[2],.....blockSize[n]) > 
   processSize[current], if found then assign 
   it to the current process.
5- If not then leave that process and keep checking
   the further processes.
   '''

def findMin(size):
   blockPlaceHolder = 1000
   locationPlaceHolder = -1
   for i in range(len(blockSize)):
      if (blockSize[i] < size): 
         continue
      if (blockSize[i] - size < blockPlaceHolder):
          blockPlaceHolder = blockSize[i] - size
          locationPlaceHolder = i
   
   blockSize[locationPlaceHolder] = blockSize[locationPlaceHolder] - size
   return(locationPlaceHolder)

def bestFit():
   print("Process No.\tProcess Size\tBlock no.")
   for n in range(len(processSize)):
      blockNumber = findMin(processSize[n])
      print ("%d\t\t%d\t\t%d" % (n+1, processSize[n], blockNumber+1))

print("Best Fit:")
bestFit()