# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    return max_height

def main():
    modee = input("mode: ")
    if "I" in modee:
        n = int(input("Num: "))
        text = input("T: ")
        text = text.split()
        text = map(int, text)
        text = list(text)
        print (n, text)
        #list(map(input().split()))
        compute_height(n, text)
        
    else:
        num = input("dok nr: ")
        with open("./test/"+ num, mode="r") as fails:
            text = fails.read()
            print(text)
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
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))