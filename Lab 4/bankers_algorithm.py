# Banker's Algorithm
'''
Write a program to simulate the Banker’s algorithm for the purpose of
deadlock avoidance. Your program receives as input the number of 
processes in the systems and how many devices each job requires to complete 
execution. Your program shows how devices are allocated to each process as it 
executes and if the system is currently in a safe or unsafe state.
'''
def calculate_need():
    for a in range(process_total):
        resource_need.append([0 for number in range(process_total)])
        for b in range(resource_total):
            resource_need[a][b] = process_maximum[a][b] - process_allocation[a][b]

def list_difference(list1, list2):
    return len(list(a for a in list(x - y for (x, y) in zip(list1, list2)) if a < 0)) == 0

def print_table():
    print("Processes     Allocation          Max           Available           Need")
    for a in range(process_total):
        print(process_name[a], "          ", process_allocation[a], "   ", 
            process_maximum[a], "   ", resource_available[a], "   ", resource_need[a], end="\n")

def is_safe():
    index = 0
    while flag != [0] * process_total:
        for i in range(process_total):
            if list_difference(resource_available[index], resource_need[i]) and flag[i] == 1:
                flag[i] = 0
                resource_available[index+1] = [x1 + x2 for (x1, x2) in zip(resource_available[index], process_allocation[i])]
                index += 1
                print_table()
                print("Processs ", process_name[i], " done")
                process_done_queue.append(process_name[i])

process_allocation = [[0, 0, 1 ,2], [1, 0, 0, 0], [1, 3, 5, 4], [0, 6, 3, 2], [0, 0, 1, 4]]
process_total = len(process_allocation)
process_name = [i for i in range(1, process_total+1)]
process_maximum = [[0, 0, 1 ,2], [1, 7, 5, 0], [2, 3, 5, 6], [0, 6, 5, 2], [0, 6, 5, 6]]
process_done_queue = []

resource_total = len(process_allocation[0])
resource_available = [[0 for j in range(resource_total)] for i in range(process_total+1)] # +1 to store the last process_available 
resource_available[0] = [1, 5, 2, 0]
resource_need = []


flag = [1 for n in range(process_total)] # flag as 0 or 1 

calculate_need()
print_table()
is_safe()
print("Processes sequence: ", process_done_queue)