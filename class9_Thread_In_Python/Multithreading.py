import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number :- {i}")
        


def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter :- {letter}")
        
start_time = time.time()

# t1 = threading.Thread(target=print_number)
# t2 = threading.Thread(target=print_letter)

# t1.start()
# t2.start()
# t1.join()
# t2.join()
print_number()
print_letter()

total_time= time.time() - start_time
print(f"Total time taken to execute the process {total_time}")