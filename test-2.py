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

#https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/
start_time = time.time()
import numpy
from memory_profiler import profile

@profile
def countFreq2(number): 
    frekuensi = {}
    i = 0
    for n in number:
        #print(n)
        if n in frekuensi:
            frekuensi[n] += 1
        else:
            frekuensi[n] = 1
        i+=1
    return frekuensi

result = countFreq2(angka)
sort_orders = sorted(result.items(), key=lambda x: x[1], reverse=True)[:10]
for y in sort_orders:
    print(y[0], y[1])

print("--- %s seconds ---" % (time.time() - start_time))