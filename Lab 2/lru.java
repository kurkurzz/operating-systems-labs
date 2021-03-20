import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Collections;

public class lru {
    public static void main(String[] args){
        LinkedList<Integer> l = new LinkedList<>();
        int[] k = {7,0,1,2,0,3,0,4,2,3,0,3,2};
        int frame_capacity = 4;

        lru(k, l, frame_capacity);
    }

    public static void lru(int[] arr,LinkedList<Integer> link,int capacity){
        
        // int[] frame = new int[0];
        int page_fault = 0;
        int len = 0;
        ArrayList<Integer> index = new ArrayList<>();
        int lru_index = 0;

        for(int i=0;i<arr.length;i++){
            if(len < capacity){
                link.add(arr[i]);
                page_fault++;
                index.add(i);
                // System.out.println("masuk");
            }
            else{
                // System.out.println("Penuh");
                if(link.contains(arr[i])){
                    index.set(link.indexOf(arr[i]),i);
                    // System.out.println(index.get(arr[i]));
                    // System.out.println("yang ada");
                }
                else{
                    link.set(index.indexOf(lru_index),arr[i]);
                    index.set(index.indexOf(lru_index),i);
                    page_fault++;
                    // System.out.println("yang takde");
                }
                lru_index = Collections.min(index);
                // System.out.println("lru "+lru_index);
            }
            len++;
            // System.out.println();

            
        }

        System.out.println("The total page fault is: "+ page_fault);
        System.out.println("The final page is: "+link);
        // System.out.println(index);
    }
}
