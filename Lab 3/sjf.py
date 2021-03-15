'''
Shortest Job First

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
def change_arrangement(job1, job2):
    for c in range(0,6):
        temp = array[c][job1]
        array[c][job1] = array[c][job2]
        array[c][job2] = temp

def sort_arrival_time():
    for a in range(job_number):
        for b in range(job_number):
            if (a == b): continue
            if (array[2][a] < array[2][b]):
                change_arrangement(a, b)
                
'''
# Pseudocode for determining arrival time
assign new variable for temp_job 
calculate completion time, waiting time, turnaround time for first job 
iterate every job after the first one (i = 1)

    determine shortest burst time
        assign a temp variable to store completion time of previous job (i-1)
        assign another temp varialbe to store burst time of current i-th job
        iterate every i-th loop with j
            if first temp variable is more than completion time of j AND
            if second temp shortest burst time 
                assign new second temp
                assign new temp_job

    calculate completion waiting time, turnaround time for i-th temp_job (same as first part)

    swap temp_job with the shortest burst time with i-th job 
'''
def completion_time():
    temp_job = -1
    array[3][0] = array[2][0] + array[1][0]
    array[5][0] = array[3][0] - array[2][0]
    array[4][0] = array[5][0] - array[1][0]

    for i in range(1, job_number):
        previous_completion_time = array[3][i - 1]
        shortest_burst_time = array[1][i]

        for j in range(i, job_number):
            if (previous_completion_time >= array[2][j] and shortest_burst_time >= array[1][j]):
                shortest_burst_time = array[1][j]
                temp_job = j

        array[3][temp_job] = previous_completion_time + array[1][temp_job]
        array[5][temp_job] = array[3][temp_job] - array[2][temp_job]
        array[4][temp_job] = array[5][temp_job] - array[1][temp_job]
        change_arrangement(temp_job, i)

def print_time():
    print ("Job Number      Burst Time      Arrival Time    Waiting Time    Turaround Time  ")
    for a in range(job_number):
        for b in range(0, 6):
            if (b == 3): continue
            print(array[b][a], end = "\t\t")
        print()

def shortest_job_first():
    sort_arrival_time()
    completion_time()

job_number = int(input("Enter number of jobs: "))
array = [[0 for j in range(job_number)] for i in range(6)] # Initialize 2D Array
array[0] = [number for number in range(1, job_number+1)]
array[1] = [int(time) for time in input("Enter burst time: ").split()]
array[2] = [int(time) for time in input("Enter arrival time: ").split()]
print_time()

shortest_job_first()
print("Final Result: ")
print_time()
print("Average waiting time = ", (sum(array[4])/job_number), end="s\n")
print("Average turnaround time = ", (sum(array[5])/job_number), end="s\n")