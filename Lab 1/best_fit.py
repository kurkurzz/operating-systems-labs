block_size = [100, 500, 200, 300, 600]
process_size = [212, 417, 112, 426]

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

def find_min(size):
    block_place_holder = 1000
    location_place_holder = -1
    for i in range(len(block_size)):
        if (block_size[i] < size): 
            continue
        if (block_size[i] - size < block_place_holder):
            block_place_holder = block_size[i] - size
            location_place_holder = i
    
    block_size[location_place_holder] = block_size[location_place_holder] - size
    return(location_place_holder)

def best_fit():
    print("Process No.\tProcess Size\tBlock no.")
    for n in range(len(process_size)):
        block_number = find_min(process_size[n])
        print ("%d\t\t%d\t\t%d" % (n+1, process_size[n], block_number+1))

print("Best Fit:")
best_fit()