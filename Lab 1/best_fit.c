#include <stdio.h>
int blockSize[] = {100, 500, 200, 300, 600};
int processSize[] = {212, 417, 112, 426};

// Implementation
// 1 - Input memory blocks and processes with sizes.
// 2 - Initialize all memory blocks as free.
// 3 - Start by picking each process and find the minimum block size that can be assigned to current process
//     i.e., find min(blockSize[1], blockSize[2], ..., blockSize[n]) > processSize[current],
//     if found then assign it to the current process.
// 4 - If not then leave that process and keep checking the further processes.

int findMin(int processSize);
void bestFit();

int main()
{
    printf("Best Fit:\n");
    bestFit();

    return 0;
}

int findMin(int processSize)
{
    int allocator = -1, min = 9999, blockSizeLength = 5;
    // int blockSizeLength = (int) sizeof(blockSize) / sizeof(blockSize[0]);

    for (int i = 0; i < blockSizeLength; i++)
    {
        if (processSize < blockSize[i])
        {
            if (min > blockSize[i])
            {
                min = blockSize[i];
                allocator = i;
            }
        }
    }

    blockSize[allocator] -= processSize;
    return allocator + 1;
}

void bestFit()
{
    // int processSizeLength = (int) sizeof(processSize) / sizeof(processSize[0]);
    int processSizeLength = 4;
    printf("Process No.\tProcess Size\tBlock No.\n");

    for (int i = 0; i < processSizeLength; i++)
    {
        int blockNumber = findMin(processSize[i]);
        printf("%d\t\t\t%d\t\t\t\t%d\n", i + 1, processSize[i], blockNumber);
    }
}