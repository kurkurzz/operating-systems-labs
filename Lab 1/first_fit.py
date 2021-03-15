block_size = [100, 500, 200, 300, 600]
process_size = [212, 417, 112, 426]

'''
FIRST FIT

Implementation:
1- Input memory blocks with size and processes with size.
2- Initialize all memory blocks as free.
3- Start by picking each process and check if it can
    be assigned to current block. 
    4- If size-of-process <= size-of-block if yes then 
    assign and check for next process.
    5- If not then keep checking the further blocks.
    '''

def find_first_fit(size):
    for x in range(len(block_size)):
        if (block_size[x] > size): 
            block_size[x] -= size
            return x
    # return value -1 if processSize can't be allocated
    return -1

def first_fit():
    print("Process No.\tProcess Size\tBlock no.")
    for a in range(len(process_size)):
        block_number = find_first_fit(process_size[a])
        if block_number != -1:
            print ("%d\t\t%d\t\t%d" % (a+1, process_size[a], block_number+1))
        else:
            print ("%d\t\t%d\t\t%s" % (a+1, process_size[a], "Not Allocated"))


print("First Fit:")
first_fit()
