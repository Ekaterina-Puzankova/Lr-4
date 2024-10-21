import random
import numpy as np
import pandas as pd

def kubik_randint(n):
    return [random.randint(1, 6) for _ in range(n)]

def kubik_sample(n):
    if n > 6:
        return [random.choice(range(1, 7)) for _ in range(n)]
    else:
        return random.sample(range(1, 7), n)

def kubik_randrange(n):
    return [random.randrange(1, 7) for _ in range(n)]

def kubik_loop_randint(n):
    lis = []
    for _ in range(n):
        lis.append(random.randint(1, 6))
    return lis

def kubik_numpy_randint(n):
    return list(np.random.randint(low=1, high=7, size=n))

results = {
    "Method randint": kubik_randint(100),
    "Method sample": kubik_sample(100),
    "Method randrange": kubik_randrange(100),
    "Loop randint": kubik_loop_randint(100),
    "Numpy randint": kubik_numpy_randint(100)
}

results1 = {
    "Method randint": kubik_randint(1000),
    "Method sample": kubik_sample(1000),
    "Method randrange": kubik_randrange(1000),
    "Loop randint": kubik_loop_randint(1000),
    "Numpy randint": kubik_numpy_randint(1000)
}

results2 = {
    "Method randint": kubik_randint(10000),
    "Method sample": kubik_sample(10000),
    "Method randrange": kubik_randrange(10000),
    "Loop randint": kubik_loop_randint(10000),
    "Numpy randint": kubik_numpy_randint(10000)
}

results3 = {
    "Method randint": kubik_randint(100000),
    "Method sample": kubik_sample(100000),
    "Method randrange": kubik_randrange(100000),
    "Loop randint": kubik_loop_randint(100000),
    "Numpy randint": kubik_numpy_randint(100000)
}


df = pd.DataFrame(results)
df1 = pd.DataFrame(results1)
df2 = pd.DataFrame(results2)
df3 = pd.DataFrame(results3)
print(df, df1, df2,df3)











