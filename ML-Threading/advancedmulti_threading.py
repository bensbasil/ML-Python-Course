from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number :{number}"

numbers=[1,2,3,4,5,7,8,9,10,11,12,13,14,15]

with ThreadPoolExecutor(max_workers=3) as executer:
    result=executer.map(print_number,numbers)

for result in result:
    print(result)