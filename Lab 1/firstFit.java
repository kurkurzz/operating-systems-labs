public class firstFit_riel{
    public static void main(String[] args){
        System.out.println("First Fit Algorithm");
        int blockSize[] = {100, 500, 200, 300, 600}; 
        int processSize[] = {212, 417, 112, 426};
        int bs = blockSize.length;
        int ps = processSize.length;

        first_fit(blockSize, bs, processSize, ps);
    }

    public static void first_fit(int blockSize[],int numOfBlock,int processSize[],int numOfProcess){
        // intialize block as free
        int block[] = new int[numOfProcess];

        //set takde block assigned kat each task lagi
        for(int i=0;i<block.length;i++){
            block[i] = -1; 
        }

        //traverse the block untuk cari saiz yang sesuai untuk each process
        for(int i=0;i<numOfProcess;i++){
            for(int j=0;j<numOfBlock;j++){
                if(blockSize[j] >= processSize[i]){
                    //allocate the block according to first fit
                    block[i] = j;
    
                    //reduce the memory left
                    blockSize[j] -= processSize[i];
                    break;
                }
            }
        }

        System.out.println("\nProcess No.\tProcess Size\tBlock No.");
        for(int i=0;i<numOfProcess;i++){
            System.out.print(""+(i+1)+"\t\t"+processSize[i]+"\t\t");
            if(block[i] != -1){
                System.out.print(block[i]+1);
            }
            else{
                System.out.print("It cannot be allocated");
            }
            System.out.println();
        }
    }
}