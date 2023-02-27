# This code compares linear, binary and jump searches' steps each takes to find the target number

import math , random
import matplotlib.pyplot as plt

#linear search
def search(arr,target, n):
    step = 0

    # searches through the list left to right
    for i in range(0, n):
      step += 1
      if (arr[i] == target):
        return step
    return -1
  
def jump_search( arr , target , n ): 
    # Finding block size to be jumped 
    jump = math.sqrt(n) 
    step = 0  
    # Finding the area with the target, if present.
    prev = 0
    while arr[int(min(jump, n)-1)] < target: 
        prev = jump 
        jump += math.sqrt(n) 
        step += 1
        if prev >= n:
            break
      
    # Doing a linear search for target from prev  
    
    while arr[int(prev)] < target: 
        prev += 1 
        step += 1
        # If we reached next block or end  
        # of array, element is not present. 
        if prev == min(jump, n): 
            break
      
    # If element is found 
    if arr[int(prev)] == target:
        step += 1
        return step
      
    return -1

def binary(arr,target,left,right,step):
  # steps are counted within binary
  mid_i = (left+right)//2 
  # checking if the mid index is the target 
  if arr[mid_i] == target:
    step += 1
    return step

  elif arr[mid_i] > target:
    return binary(arr,target,left,mid_i,step +1)  

  elif arr[mid_i] < target:
    left = arr[mid_i]
    return binary(arr,target,mid_i,right,step +1)

  else:
    return -1

# Test the functions
N = 1000
x_vals = [i for i in range(100,N)]

# jump seach values 
jump_vals = [jump_search([j for j in range(1,i+1)],random.randint(1,i), len(range(1,i+1))) for i in x_vals]

liny_vals = [search([j for j in range(1,i+1)],random.randint(1,i), len(range(1,i+1))) for i in x_vals]

bin_vals = [binary([j for j in range(1,i+1)],random.randint(1,i),0, len(range(1,i+1)),1) for i in x_vals]





fig = plt.figure()

fig.add_subplot(3,1,1)
plt.title("Jump search vs Linear")
plt.plot(x_vals,jump_vals,'r.',label="jump search")
plt.plot(x_vals,liny_vals, 'b.',label="linear search")
plt.xlabel("List Length")
plt.ylabel("Steps")
plt.legend(loc= "upper left")

fig.add_subplot(3,1,3)
plt.title("Jump search vs Binary")
plt.plot(x_vals,jump_vals,'r.',label="jump search")
plt.plot(x_vals,bin_vals, 'g.',label="binary search")
plt.xlabel("List Length")
plt.ylabel("Steps")
plt.legend(loc="upper left")

fig.savefig('plot.png')
