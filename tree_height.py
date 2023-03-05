# python3

import sys
import threading
import numpy

def build_tree(root_node, nodes):
    children = [
        build_tree(child, nodes)
        for child, node in enumerate(nodes)
        if node == root_node
    ]
    return {'key': root_node, 'children': children}

def compute_height(tree):
    return 1 + max((compute_height(c) for c in tree['children']), default=-1)
  
#def compute_height(n, parents):
    # Write this function
    #max_height = 0
    #return max_height
    #pass
    

def main():
    modee = input("mode: ")
    if "I" in modee:
        int(input())
        tree = build_tree(-1, list(map(int, input().split())))
        print(compute_height(tree))
    elif "F" in modee:
        num = input("dok nr: ")
        with open("./test/"+ num, mode="r") as fails:
            text = fails.read()
            x = text.splitlines()
            txt = x[1]
            tree = build_tree(-1, list(map(int, txt.split())))
            #tree = int (x[1])
            print(compute_height(tree))
            
        # text = input("T: ")
        # text = text.split()
        # text = map(int, text)
        # text = list(text)
        # print (n, text) 
        #list(map(input().split()))           
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    #pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))