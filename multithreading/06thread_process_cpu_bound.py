

# 被自身和1整除是素数
import time
import math
from operator import truediv
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import math 
PRIMES =[122131288783123] * 100
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n+1,2):
        if n % i == 0:
            return False

    return True

# 单线程
def single_thread():
    for number in PRIMES:
        is_prime(number)

# 多线程
def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime,PRIMES)

# 多进程
def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime,PRIMES)

if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread, cost:",end-start,"seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread, cost:",end-start,"seconds")

    start = time.time()
    multi_process()
    end = time.time()
    print("multi_process, cost:",end-start,"seconds")

#single_thread, cost: 0.524777889251709 seconds
# multi_thread, cost: 0.5671963691711426 seconds
# multi_process, cost: 0.11627411842346191 seconds