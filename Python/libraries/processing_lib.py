import time
from threading import Lock
from multiprocessing import Process
from urllib.request import urlopen

lock = Lock() # Makes sure there is no conflict between different threads..

def do_cpu_work() -> None:
    for i in range(100_000):
        2**i

def do_io_work(process_number: int) -> None:
    #with lock:
    #print(f"Process #{process_number} started.")
    urlopen("https://www.youtube.com")
    #print(f"Process #{process_number} finished")

if __name__ == "__main__":
    processes = []
    start = time.perf_counter()
    
    for i in range(10):
        do_io_work(i)
#        do_cpu_work()
#        p = Process(target=do_io_work, args=(i,))
#        p = Process(target=do_cpu_work)
#        processes.append(p)
#        p.start()

#    for p in processes:
#        p.join()
    
    end = time.perf_counter()
    
    print(f"Total time: {end - start:.2f}s")
    
    """
    RESULTS
    
        1. GPU based work (better to use mutli-processing)
            - Single threading/processing:
                - for 10_000 x 10 -> 0.32s
                - for 100_000 x 10 -> 48.42s
            
            - Multi-threading (Ten threads):
                - for 10_000 x 10 -> 0.89s
                - for 100_000 x 10 -> 105.80s
            
            - Multi-processing (Ten processes):
                - for 10_000 x 10 -> 0.07s
                - for 100_000 x 10 -> 7.65s
        
        2. IO based work (better to use multi-threading)
            - Single threading/processing:
                - for 10 -> 1.21s
                - for 100 -> 12.77s
            
            - Multi-threading (Ten threads):
                - for 10 -> 0.20s
                - for 100 -> 0.53s
            
            - Multi-processing (Ten processes):
                - for 10 -> 0.22s
                - for 100 -> 0.58s
    """