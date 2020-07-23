#import library
import random
import time

#function to generate number
def Rand(start, end, num): 
    res = [] 
    for j in range(num): 
        res.append(random.randint(start, end)) 
    return res 

#settings to generate amount of number
num = 100000
#amount of number that will be generated
start = 10
#start number
end = 600
#end number
angka = Rand(start, end, num)

import numpy as np
# source : https://www.geeksforgeeks.org/counting-frequencies-of-array-elements/
# Python 3 program to count frequencies 
# of array items
from memory_profiler import profile

@profile
def countFreq(arr, n): 
    u =0
    a = []
    # Mark all array elements as not visited 
    visited = [False for i in range(n)] 
  
    # Traverse through array elements  
    # and count frequencies 
    for i in range(n): 
          
        # Skip this element if already  
        # processed 
        if (visited[i] == True): 
            continue
  
        # Count frequency 
        count = 1
        for j in range(i + 1, n, 1): 
            if (arr[i] == arr[j]): 
                visited[j] = True
                count += 1
          
        #print(arr[i], count) 
        a.append([arr[i],count])
        #arr_counter[i][0] = arr[i] 
        #arr_counter[i][1] = count
    a = np.array(a)
    return a

start_time = time.time()
countMe = countFreq(angka, len(angka) ) 
countMe_sort = countMe[countMe[:,1].argsort()[::-1]]
print(countMe_sort[:5])
print("--- %s seconds ---" % (time.time() - start_time))