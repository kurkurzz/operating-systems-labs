'''
Write a program to simulate the following file allocation strategies:
a) Sequential

Source algorithm: https://exploringbits.com/sequential-file-allocation-program-in-c/
'''

maximum_size = 50
files = [0 for file in range(maximum_size)]

def print_files():
    # 1 for allocated and 0 for non-allocated
    for a in range(maximum_size):
        if (files[a] == 1):
            print(a+1, "\t1")
        else:
            print(a+1, "\t0")

def prompt_continue():
    input2 = input("Do you want to enter more files?\nEnter Yes/No: ")
    if (input2.lower() == "yes"):
        sequential_allocation()
    elif (input2.lower() == "no"):
        print_files()
    else:
        print("Please enter the right key")
        prompt_continue()

def sequential_allocation():
    while True:
        inputs = [int(number) for number in input(f"Enter the starting block (1-{maximum_size}) and the length of the files: ").split()]
        if (len(inputs) != 2): 
            print("Please enter only two values")
            continue

        start_block = inputs[0]
        length = inputs[1]

        # start_block-1 to indicate the logical index inside array
        # length-1 because its inclusive
        if (start_block-1 >= maximum_size or start_block-1 + length-1 >= maximum_size):
            print("Maximum size exceeded")
            print("The file is not allocated to the disk")
            break
        if (files[start_block-1] == 1 or files[start_block-1 + length-1] == 1):
            print("Block already occupied")
            print("The file is not allocated to the disk")
            break

        for i in range(length):
            files[start_block-1 + i] = 1
            print(start_block + i, "\t1")
        print("The file is allocated to the disk")
        break

    prompt_continue()   

sequential_allocation()