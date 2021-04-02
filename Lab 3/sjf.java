import java.util.*;

public class sjf {
    public static void main(String[] args){
        // HashMap<Integer,Integer> map = new HashMap<>();
        // map.put(2,3);
        // map.put(0,4);
        // map.put(4,2);
        // map.put(5,4);
        // int length = map.size();
        // System.out.println(length);

        // Process p[] = {{2,3},{0,4},{4,2},{5,4}};
        Process p[] = new Process[4];
        p[0] = new Process("1", 3);
        p[1] = new Process("2", 4);
        p[2] = new Process("3", 2);
        p[3] = new Process("4", 4);
        // for(int i=0;i<p.length-1;i++){
        //     for(int j=0;j<p.length-i-1;j++){
        //         if(p[j].burstTime > p[j+1].burstTime){
        //             swap(p[j], p[j+1]);
        //         }
        //     }
        // }
        // for(int i=0;i<p.length;i++){
        //     System.out.println(p[i].burstTime+" "+p[i].processID);
        // }

        Arrays.sort(p);
        System.out.println(Arrays.toString(p));
        System.out.println("Assume the arrival time for all process is 0");
        // for(int i=0;i<p.length;i++){
        //     System.out.println(p[i].burstTime+" "+p[i].processID);
        // }
        findAverageTime(p, p.length);
    }

    // public static void swap(Process a,Process b){
    //     Process temp = a;
    //     a = b;
    //     b = temp;
    // }

    // // method to sort all process according to increasing order of burst time
    // public static boolean compare(Process a,Process b){
    //     return (a.burstTime < b.burstTime);
    // }

    public static void waitingTime(Process a[],int n, int waitTime[]){
        // wating time for 1st process is 0
        waitTime[0] = 0;
        //calculate waiting time for each process
        for(int i=1;i<n;i++){
            waitTime[i] = a[i-1].burstTime + waitTime[i-1];
        }
    }

    // turnAroundTime = completion time - arrival time
    public static void turnAroundTime(Process a[],int n,int waitingTime[],int turnTime[]){
        for (int i=0;i<n;i++){
            turnTime[i] = a[i].burstTime + waitingTime[i];
        }
    }

    public static void findAverageTime(Process a[],int n){
        int waitTime[]= new int[n];
        int turnTime[]= new int[n];
        int total_waitingTime=0;
        int total_turnAroundTime=0;

        //find waiting time for all process
        waitingTime(a, n, waitTime);

        //find the turn around time
        turnAroundTime(a, n, waitTime, turnTime);

        System.out.println("Process ID\tBurst Time\tWaiting Time\tTurn Around Time");

        for(int i=0;i<n;i++){
            total_waitingTime += waitTime[i];
            total_turnAroundTime += turnTime[i];
            System.out.println(a[i].processID+"\t\t"+a[i].burstTime+"\t\t"+waitTime[i]+"\t\t"+turnTime[i]);
        }

        System.out.println("Average waiting time = "+(float)total_waitingTime/n);
        System.out.println("Average turn around time = "+(float)total_turnAroundTime/n);
    }
    
}

class Process implements Comparable<Process>{
    public String processID;
    public int burstTime;

    public Process(String processID,int burstTime){
        this.processID = processID;
        this.burstTime = burstTime;
    }

    public String getID(){
        return processID;
    }

    public int getTime(){
        return burstTime;
    }

    public static void swap(int a,int b){
        int temp = a;
        a = b;
        b = temp;
    }

    @Override
    public int compareTo(Process p){
        if(this.burstTime != p.getTime()){
            return this.burstTime - p.getTime();
        }
        return this.processID.compareTo(p.getID());
    }

    public String toString(){
        System.out.println();
        return "{"+processID+" "+burstTime+"}";
    }
}