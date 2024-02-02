# 1. A profiler in Python helps create a profile, that provides a set of statistics and describes how much time is spent on different parts of the code, as well as how often and for how long certain parts of the code are executed. And these statistics can then be formatted through the pstats module

#2. Profiling differs from Benchmarking in that profiling focuses more on the behavior of smaller parts of the code and identifying which parts take up the most execution time and providing details on how many times a function was called. Benchmarking on the other hand focuses more on the entire  system's overall performance rather than specific and smaller parts of the code.

# 4. A sample output is: 
"""Profiling results:
         69 function calls (24 primitive calls) in 29.976 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   29.975   29.975 ex3.py:27(third_function)
        1   29.975   29.975   29.975   29.975 ex3.py:29(<listcomp>)
        1    0.000    0.000    0.000    0.000 ex3.py:21(test_function)
    55/10    0.000    0.000    0.000    0.000 ex3.py:14(sub_function)
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""
# This meant that majority of the execution time was through the "third_function" which took 29.975 seconds whereas the other functions did not take up a significant amount of execution time. It also says how many times functions were called, which as 69 times.


import timeit
import cProfile

def sub_function(n):
    #sub that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    #third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

# ChatGPT was used to create the following profiling function.
if __name__ == "__main__":
    # Profiling the entire script
    profiler = cProfile.Profile()
    profiler.enable()

    # Run the functions
    test_function()
    third_function()

    profiler.disable()
    
    # Print profiling results
    print("Profiling results:")
    profiler.print_stats(sort='cumulative')

    