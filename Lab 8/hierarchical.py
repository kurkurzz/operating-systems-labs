'''
Write a program to simulate the following file organization techniques:
a) Hierarchical

Source idea: 
http://avanthioslab.blogspot.com/2016/08/file-organization-techniques.html
https://stackoverflow.com/questions/23153319/n-ary-tree-in-python

-Implement tree data structure
-Prompt user to create folder or file (input string)
-Simulate linux/unix cd, mkdir, mkfile, ls command because I can & I like
-Method to print directory and tree
-Start with root folder first
'''

class Node():
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
        self.children = []

    def get_name(self):
        return str(self.data)

    def add_file(self, data):
        node = Node(self, data)
        self.children.append(node)

    def get_parent(self):
        return self.parent

    def get_children(self, index):
        return self.children[index]

    def print_children(self):
        for file in self.children:
            print(file.get_name())

    def print_tree(self, level):
        if (level == 0):
            print("Directory List: ")
        for i in range(level):
            print("-|", end="")
        print(self.get_name())
        if len(self.children) != 0:
            for file in self.children:
                file.print_tree(level+1)

    def find_folder(self, input_name):
        for file in self.children:
            if (file.get_name() == input_name):
                return file

        return -1

def print_working_directory(node):
    path = ''
    temp_node = node
    while (temp_node.get_name() != "/"):
        path = temp_node.get_name() + "/" + path
        temp_node = temp_node.get_parent()

    path = "/" + path
    print(path, end=":~$ ") 

def hierarchical():
    root = Node(None, "/")
    current_folder = root

    while True:
        print_working_directory(current_folder)

        command_line = [word for word in input().split()]
        arguments = len(command_line)
        if arguments == 1:
            command = command_line[0]
        elif arguments == 2:
            command = command_line[0]
            file_name = str(command_line[1])
        else:
            print("Please enter the right command")
            continue

        if (command == "cd" and arguments == 2):
            if file_name == ".." and current_folder != root:
                current_folder = current_folder.get_parent()
            elif file_name == ".." and current_folder == root:
                print("In root")
            else:
                if (current_folder.find_folder(file_name) == -1):
                    print(f"\"{file_name}\" not found")
                else:
                    current_folder = current_folder.find_folder(file_name)
        elif (command == "mkdir" and arguments == 2):
            current_folder.add_file(file_name)
        elif (command == "mkfile" and arguments == 2):
            current_folder.add_file(file_name)
        elif(command == "ls"):
            current_folder.print_children()
        elif (command == "tree"):
            root.print_tree(0)
        elif (command == "exit"):
            root.print_tree(0)
            print("Exited")
            break
        else: 
            print("Please enter the right command")
            continue

hierarchical()