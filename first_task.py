import numpy as np
import time


def timer(func):
    def wrapper(*args, **kwargs):
        begin = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Время выполнения функции {func.__name__}: {end - begin}')
    return wrapper

@timer
def np_array_mult(x1, x2):
    return np.multiply(x1, x2)

@timer
def list_mult(x1, x2):
    return [x1[i]*x2[i] for i in range(len(x1))]


np_arr1 = np.random.rand(10**6)
np_arr2 = np.random.rand(10**6)
arr1 = list(np_arr1)
arr2 = list(np_arr2)
np_array_mult(np_arr1, np_arr2)
list_mult(arr1, arr2)

