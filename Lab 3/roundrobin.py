from queue import Queue
'''
Round Robin

Your program receives as input the number of jobs waiting in queue
and the time required to execute each job. 
Display the outcome of each scheduling algorithm.

INDEXES
0 - Job number
1 - Burst time
2 - Arrival time
3 - Completion Time
4 - Waiting time = Turnaround time - Burst time
5 - Turnaround time = Completion time - Arrival time 
'''
def print_time():
    print ("Job Number      Burst Time      Arrival Time    Waiting Time    Turaround Time  ")
    for a in range(job_number):
        for b in range(0, 6):
            if (b == 3): continue
            print(array[b][a], end = "\t\t")
        print()

def round_robin():
    burst_time = array[1].copy()
    not_yet_queue = array[0].copy()
    time_quantum = 3 # Suppose its 3 unit
    t = 0
    q = Queue()

    while burst_time != [0]*job_number:
        for i in range(job_number):
            if (t+time_quantum >= array[2][i] and i+1 in not_yet_queue): # Check arrival time
                q.put(i)
                not_yet_queue.remove(i+1)

        index = q.get()
        if burst_time[index] > time_quantum:
            t += time_quantum
            burst_time[index] -= time_quantum
            q.put(index)
        else:
            t += burst_time[index]
            burst_time[index] = 0

            array[3][index] = t # Completion time
            array[5][index] = t - array[2][index] # Turnaround time
            array[4][index] = array[5][index] - array[1][index] # Waiting time

job_number = int(input("Enter number of jobs: "))
array = [[0 for j in range(job_number)] for i in range(6)] # Initialize 2D Array
array[0] = [number for number in range(1, job_number+1)]
array[1] = [int(time) for time in input("Enter burst time: ").split()]
array[2] = [int(time) for time in input("Enter arrival time: ").split()]
print_time()

round_robin()
print("Final Result: ")
print_time()
print("Average waiting time = ", (sum(array[4])/job_number), end="s\n")
print("Average turnaround time = ", (sum(array[5])/job_number), end="s\n")