// 1. Create two arrays of burst time res_b[] and of 
//   arrival time res_a[] and copy the value of 
//   the b[] and a[] array for calculate the 
//   remaining time.(b[] is burst time, a[] arrival time).
// 2. Create an another array for wt[] to store waiting time.
// 3. Initialize Time : t=0;
// 4. Keep traversing the all process while all 
//    process are not done.
//    Do following for i'th process if it is not done yet.
//    a- if res_a[i]<= q   (quantum time :- q)
//         1. if res_b[i]>q 
//              a. t=t+q
//              b. res_b[i]-=q;
//              c. a[i]+=q;
//         2. else res_b[i]<=q(for last to execute)
//               a. t=t+b[i];
//               b. wt[i]=t-b[i]-a[i];
//               c.res_b[i]=0;
//     b- else res_a[i]<q
//           1. Initialize j=0 to number of process
//              if a[j]<a[i] (compare is there any 
//              other process come before these process)
//                     1. if res_b[j]>q 
//                             a. t=t+q
//                             b. res_b[j]-=q;
//                             c. a[j]+=q;
//                     2. else res_b[j]<=q
//                            a. t=t+b[j];
//                            b. wt[j]=t-b[j]-a[j];
//                            c.res_b[j]=0; 
//           2. now we executing the i'th process 
//                       1. if res_b[i]>q 
//                             a. t=t+q
//                             b. res_b[i]-=q;
//                             c. a[i]+=q;
//                       2. else res_b[i]<=q
//                             a. t=t+b[i];
//                             b. wt[i]=t-b[i]-a[i];
//                             c.res_b[i]=0;

import java.util.*;

public class roundRobin_differentTime {
    public static void main(String args[]){
        int process[] = {1,2,3,4,5};
        int burstTime[] = {6,4,8,3,9};
        int arrivalTime[] = {0,1,2,3,4};
        int timeSlice = 2; //quantum

        findAverageTime(process, process.length, burstTime, arrivalTime, timeSlice);
    }

    public static void waitingTime(int process[],int numOfProcess,int burstTime[],int arrivalTime[],int waitTime[],int completionTime[],int timeSlice){
        //var to calculate the remaining time for each iteration process
        int remainingTime[] = new int[numOfProcess];

        for(int i=0;i<numOfProcess;i++){
            remainingTime[i] = burstTime[i];
        }

        int time = 0;
        int arrival = 0;

        while(true){
            boolean processOver = true;
            for(int i=0;i<numOfProcess;i++){
                if(remainingTime[i] > 0){
                    processOver = false;
                    if(remainingTime[i] <= timeSlice && arrivalTime[i] <= arrival){
                        time += timeSlice;
                        remainingTime[i] -= timeSlice;
                        arrival++;
                    }
                    else{
                        if(arrivalTime[i] <= arrival){
                            time += remainingTime[i];
                            remainingTime[i] = 0;
                            arrival++;
                            completionTime[i] = time;
                        }
                    }
                }
            }
            if(processOver == true){
                break;
        }
        }
    }

    public static void turnAroundTime(int process[],int numOfProcess,int burstTime[],int arrivalTime[],int waitTime[],int completionTime[],int turnTime[]){
        for(int i=0;i<numOfProcess;i++){
            turnTime[i] = completionTime[i] - arrivalTime[i];
            waitTime[i] = turnTime[i] - burstTime[i];
        }
    }

    public static void findAverageTime(int process[],int numOfProcess,int burstTime[],int arrivalTime[],int timeSlice){
        int waitTime[] = new int[numOfProcess];
        int turnTime[] = new int[numOfProcess];
        int completionTime[] = new int[numOfProcess];

        waitingTime(process, numOfProcess, burstTime, arrivalTime, waitTime, completionTime, timeSlice);

        turnAroundTime(process, numOfProcess, burstTime, arrivalTime, waitTime, completionTime, turnTime);

        int total_waitingTime = 0;
        int total_turnAroundTime = 0;

        System.out.println("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnAround Time     Completion Time");

        for(int i=0;i<numOfProcess;i++){
            total_waitingTime += waitTime[i];
            total_turnAroundTime =+ turnTime[i];
            System.out.println(i+1+"\t\t"+arrivalTime[i]+"\t\t"+burstTime[i]+"\t\t"+waitTime[i]+"\t\t"+turnTime[i]+"\t\t     "+completionTime[i]);
        }

        System.out.printf("Average waiting time: %.2f",((float)total_waitingTime/(float)numOfProcess));
        System.out.printf("\nAverage turn around time: %.2f",((float)total_turnAroundTime/(float)numOfProcess));
    }
}
