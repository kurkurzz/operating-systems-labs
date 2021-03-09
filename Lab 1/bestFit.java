public class bestFit{
    public static void main(String[] args){
        System.out.println("Best Fit Algorithm");
        int blockSize[] = {100, 500, 200, 300, 600}; 
        int processSize[] = {212, 417, 112, 426};
        int bs = blockSize.length;
        int ps = processSize.length;

        best_fit(blockSize, bs, processSize, ps);
    }

    // method to allocate block using best fit approach
    public static void best_fit(int blockSize[],int numOfBlock,int processSize[],int numOfProcess){
        // to store allocated block id
        int block[] = new int[numOfProcess];

        //to ensure no block is assigned to any process initially
        for(int i=0;i<block.length;i++){
            block[i] = -1;
        }

        //iterate each process to find suitable block
        for(int i=0;i<numOfProcess;i++){
            //find best fit block for each process
            int bestFitBlock = -1;
            for(int j=0;j<numOfBlock;j++){
                if(blockSize[j] >= processSize[i]){
                    // if(bestFitBlock == -1 || (blockSize[bestFitBlock] > blockSize[j])){
                    //     bestFitBlock = j;
                    // }

                    if(bestFitBlock == -1){
                        bestFitBlock = j;
                    }
                    else if(blockSize[bestFitBlock] > blockSize[j]){
                        bestFitBlock = j;
                    }
                }
            }

            //if block is suitable
            if(bestFitBlock != -1){
                //assign current block to process
                block[i] = bestFitBlock;
                //decrease the memory left
                blockSize[bestFitBlock] -= processSize[i];
            }
        }

        //print the output
        System.out.println("\nProcess Num.\tProcess Size\tBlock Size");
        for(int i=0;i<numOfProcess;i++){
            System.out.print(""+(i+1)+"\t\t"+processSize[i]+"\t\t");
            if(block[i] != -1){
                System.out.print(block[i]+1);
            }
            else{
                System.out.print("Cannot be allocated");
            }

            System.out.println();
        }
    }

}