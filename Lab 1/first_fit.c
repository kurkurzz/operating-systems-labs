#include <stdio.h>
int blockSize[] = {100, 500, 200, 300, 600};
int processSize[] = {212, 417, 112, 426};

// Implementation
// 1 - Input memory blocks and processes with sizes.
// 2 - Initialize all memory blocks as free.
// 3 - Start by picking each process and check if it can be assigned to current block.
// 4 - If size-of-process <= size-of-block if yes then assign and check for next process.
// 5 - If not then keep checking the further blocks.

int findFirstFit(int processSize);
void firstFit();

int main()
{
    printf("First Fit:\n");
    firstFit();

    return 0;
}

int findFirstFit(int processSize)
{
    int blockSizeLength = 5;

    for (int i = 0; i < blockSizeLength; i++)
    {
        if (processSize < blockSize[i])
        {
            blockSize[i] -= processSize;
            return i;
        }
    }

    return -1;
}

void firstFit()
{
    int processSizeLength = 4;
    printf("Process No.\tProcess Size\tBlock No.\n");

    for (int i = 0; i < processSizeLength; i++)
    {
        int blockNumber = findFirstFit(processSize[i]);
        if (blockNumber != -1)
        {
            printf("%d\t\t\t%d\t\t\t\t%d\n", i + 1, processSize[i], blockNumber + 1);
        }
        else
        {
            printf("%d\t\t\t%d\t\t\t\t%s\n", i + 1, processSize[i], "Not Allocated");
        }
    }
}