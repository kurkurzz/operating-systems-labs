import java.util.LinkedList;
import java.util.Queue;

public class fifo{
    public static void main(String[] args){
        Queue<Integer> q = new LinkedList<>();
        int[]k = {1,3,0,3,5,6};
        int frame_capacity = 3;
        
        pageFault(k, q,frame_capacity);
    }

    public static void pageFault(int [] arr,Queue<Integer> q,int capacity){
        
        // int[] frame = new int[0];
        int page_fault = 0;
        int len = 0;

        for(int i=0;i<arr.length;i++){
            
            if(!q.contains(arr[i])){
                page_fault++; //bila new page, auto add je
                if(len < capacity){ //bila page capacity penuh, pergi kat else
                    q.add(arr[i]);
                    // System.out.println(len);
                }
                else{ //buang yang first masuk,add yang paling baru kat belakang
                    q.remove();
                    q.add(arr[i]);
                }
                len++;
            }
            

        }
        System.out.println("The total page fault is: "+ page_fault);
        System.out.println("The final page is: "+q);

    }
}