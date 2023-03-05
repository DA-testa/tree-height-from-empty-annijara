# python3

import sys
import threading
import numpy


def compute_height(parents):
# Write this function
    #max_height = 0
# Your code here
    #return max_height
    n = len(parents)
    length = [-1] * n
    
    def max_height(i):
        if i == -1:
            return -1
         
        if length[i] == -1:
            length[i] = 1 + compute_height(parents[i])                      
            return length[i]
        
        for i in range(n):
            max_height(i)
            return max(length)  
  
    

def main():
    option = input()
    if "I" in option:
        n = int(input())
        text = input()
        text = text.split()
        parents = (list(map(int, text)))
        
        height = (compute_height( parents))
        print(height)
    
    elif "F" in option:
        num = input()
        if num != "a":
            with open("./test/"+ num, mode="r") as fails:
                text = fails.read()
                x = text.splitlines()
                #n = int(x[0])
                txt = x[1].split()
                parents = (list(map(int, txt)))
                height = (compute_height(parents))
                print(height)
            
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