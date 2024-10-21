import random
import numpy as np

# Method 1: Using random.randint()
def my_rand1(n=10, low=3, high=9):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(low, high))
    return rand_list
print("Method 1:", my_rand1())

# Method 2: Using random.sample()
def my_rand2(k=7, range_start=1, range_end=50):
    return random.sample(range(range_start, range_end), k)
print("Method 2:", my_rand2())

# Method 3: Using list comprehension + randrange()
def my_rand3(n=7, range_start=1, range_end=50):
    return [random.randrange(range_start, range_end, 1) for i in range(n)]
print("Method 3:", my_rand3())


# Method 4: Using loop + randint()
def my_rand4(n=10, low=0, high=51):
    lis = []
    for _ in range(n):
        lis.append(random.randint(low, high))
    return lis
print("Method 4:", my_rand4())


# Method 1: Generating a list of random integers using numpy.random.randint
def my_rand5(n=10, low=3, high=8):
    return list(np.random.randint(low=low, high=high, size=n))
print("Numpy Method 1:", my_rand5())

# Method 2: Generating a list of random floating values using numpy.random.random_sample
def my_rand6(size=4):
    return np.random.random_sample(size=size)
print("Numpy Method 2:", my_rand6())
