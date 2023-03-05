# python3

import sys
import threading
import numpy

def get_height(parents):
     depths = [-1] * len(parents)

     def get_depth(i):
         if i == -1:
             return -1
         if depths[i] == -1:
             depths[i] = 1 + get_depth(parents[i])
         return depths[i]

     for i in range(len(parents)):
         get_depth(i)
     return max(depths)
  
#def compute_height(n, parents):
    # Write this function
    #max_height = 0
    #return max_height
    #pass
    

def main():
    modee = input()
    if "I" in modee:
        int(input())
        parents = (list(map(int, input().split())))
        height = get_height(parents)
        print(height+1)
    elif "F" in modee:
        num = input()
        with open("./test/"+ num, mode="r") as fails:
            text = fails.read()
            x = text.splitlines()
            txt = x[1]
            parents = (list(map(int, txt.split())))
            height = get_height(parents)
            print(height+1)
            
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