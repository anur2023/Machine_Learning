import multiprocessing
import multiprocessing.process
import time

def get_square():
    for i in range(1,21):
        print(f"Square of {i} :- {i**2}")
        time.sleep(1)

def get_cube():
    for i in range(1,21):
        print(f"Cube of number {i} :- {i**3} ")
        time.sleep(1.5)


if __name__ == "__main__":
    start_time = time.time()
    t1 = multiprocessing.Process(target = get_square)
    t2 = multiprocessing.Process(target=get_cube)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time() -start_time
    print(f"Total time in execution is :-  {end_time}")