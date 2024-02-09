"""
Exercise 1/3:
1. This code in the function "func" recursively calculates the nth number in the Fibonacci sequence.

2. No. All the function calls are calculating a smaller problem of the same type, not dividing the problem into smaller subproblems. 

3. If you imagine each sub-function call as a tree, you should be able to see that the amount of problems
created doubles with each call. 
Thus, the time complexity of this function is O(2^n) as the function calls itself twice for each call.
"""

import matplotlib.pyplot as plt
import timeit

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)


"""      4.       """
memo_cache = {}
def improved_func(n):
    if n in memo_cache:
        return memo_cache[n]
    if n == 0 or n == 1:
        return n
    else:
        memo_cache[n] = improved_func(n-1) + improved_func(n-2)
        return memo_cache[n]
    

"""
Exercise 1/4:
5. Now that the function uses memoization, the time complexity is O(n) as the function only 
calls itself once for each n because if the result is already in the cache, it is returned.
"""

"""      6.       """
n = [i for i in range(0, 35)]
memo_time = []
time = []
for num in n:
    memo_time.append(timeit.timeit(lambda: improved_func(num), number=1))
    time.append(timeit.timeit(lambda: func(num), number=1))

plt.plot(n, time)
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Time complexity of func")
plt.savefig('ex1.6.1.jpg')

plt.clf()

plt.plot(n, memo_time)
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Time complexity of improved_func")
plt.savefig('ex1.6.2.jpg')

