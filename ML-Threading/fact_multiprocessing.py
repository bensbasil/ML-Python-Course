import multiprocessing
import math
import sys
import time

##Increace the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

##Functions to compute factorials of a given number

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result

if __name__=="__main__":
    number=[5000,6000,700,8000] 
    start_time=time.time()

    ##Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,number)

    end_time=time.time()
    print(f"Results : {results}") 
    print(f"Time Taken: {end_time - start_time} seconds")                 