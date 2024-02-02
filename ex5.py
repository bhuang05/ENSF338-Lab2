import numpy as np
import random


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
    return vector, value

vector1000, key1000 = vectorandkey(1000)
vector2000, key2000 = vectorandkey(2000)
vector4000, key4000 = vectorandkey(4000)
vector8000, key8000 = vectorandkey(8000)
vector16000, key16000 = vectorandkey(16000)
vector32000, key32000 = vectorandkey(32000)


