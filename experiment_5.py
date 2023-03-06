import time

def for_loop_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def while_loop_sum(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

n_values = [10, 100, 1000, 10000, 100000]
for n in n_values:
    start_time = time.time()
    for_loop_sum(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"For loop: n={n}, sum={for_loop_sum(n)}, execution time={execution_time:.6f} seconds")
    
    start_time = time.time()
    while_loop_sum(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"While loop: n={n}, sum={while_loop_sum(n)}, execution time= {execution_time:.6f} seconds\n")