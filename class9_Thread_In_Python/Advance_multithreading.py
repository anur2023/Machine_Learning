from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number:- {number}"
numbers = [1,2,3,4,5]
with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(print_number,numbers)
for results in result:
    print(results)