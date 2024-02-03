import numpy as np
import timeit
import matplotlib.pyplot as plt
import scipy.optimize


def linearsearch(data, key):
    for index, value in enumerate(data):
        if key == value:
            return index
    return -1

def binarysearch(data, first, last, key):
    if(first <= last):
        mid = (first+last) // 2
    if(key == data[mid]):
        return mid
    elif (key < data[mid]):
        return binarysearch(data, first, mid-1, key)
    elif (key > data[mid]):
        return binarysearch(data, mid+1, last, key)
    return -1

def vectorandkey(size):
    #line 24 from ChatGPT
    vector = np.random.randint(low=np.iinfo(np.int32).min, high=np.iinfo(np.int32).max, size = size)
    value = np.random.choice(vector)
    vector.sort()
    return vector, value


sizes = [1000,2000,4000,8000,16000,32000]

linear_times = []
binary_times = []

for size in sizes:
    vector,key = vectorandkey(size)

    lineartime =  timeit.timeit(lambda: linearsearch(vector, key), number=100)
    binarytime =  timeit.timeit(lambda: binarysearch(vector, 0, len(vector)-1, key), number=100)

    linear_times.append(lineartime)
    binary_times.append(binarytime)

slope, intercept = np.polyfit(sizes, linear_times, 1)
plt.scatter(sizes, linear_times)
linevalues = [slope * x + intercept for x in sizes]
plt.plot(sizes, linevalues, 'r-')

slope_linear, intercept_linear = np.polyfit(sizes, linear_times, 1)
linear_fit_values = [slope_linear * x + intercept_linear for x in sizes]


plt.xlabel('Sizes')
plt.ylabel('Line Values')
plt.title("Linear Complexity Plot for the Sizes")
plt.show()

#Lines 61 - 68 from ChatGPT
def func(n, a, b):
    return a * np.log2(n) + b

popt, pcov = scipy.optimize.curve_fit(func, sizes, binary_times)

plt.scatter(sizes, binary_times)
binary_linevalues = func(np.array(sizes), *popt)
plt.plot(sizes, binary_linevalues, 'r')

plt.xlabel('Sizes')
plt.ylabel('Line Values ')
plt.title('Logarithmic Complexity Plot for the Sizes')
plt.show()

#4. Linear search is a linear function while binary search is a logarithmic function. The parameters are the various sizes of arrays for the x-axis and the line values/search times for the y-axis
# The results are somewhat as expected. You can see that in general, linear complexity of the linear search tends to increase linearly from one size to the next, which leads to the averge times
# having such a large variance between them. The logarithmic complexity increasing in time much slower, which can be seen by the line values barely incresing. The linear search has times close 
# to the binary search when the array is of smaller size, however, we can see how big the difference is once the arrays get larger, even while not accounting for the randomness of the data. 