import random
import numpy as np
import pandas as pd

# Функции для генерации бросков кубика
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

# Функция для вычисления вероятностей
def probability_solving(dataframe: pd.DataFrame):
    sum_rate = dataframe['Частота'].sum()
    probability = []
    for i in dataframe['Частота']:
        probability.append(i / sum_rate)
    dataframe['Вероятность'] = probability
    return dataframe

# Сбор данных для каждого метода
methods = {
    "Method randint": kubik_randint(100),
    "Method sample": kubik_sample(100),
    "Method randrange": kubik_randrange(100),
    "Loop randint": kubik_loop_randint(100),
    "Numpy randint": kubik_numpy_randint(100)
}

methods1 = {
    "Method randint": kubik_randint(1000),
    "Method sample": kubik_sample(1000),
    "Method randrange": kubik_randrange(1000),
    "Loop randint": kubik_loop_randint(1000),
    "Numpy randint": kubik_numpy_randint(1000)
}

methods2 = {
    "Method randint": kubik_randint(10000),
    "Method sample": kubik_sample(10000),
    "Method randrange": kubik_randrange(10000),
    "Loop randint": kubik_loop_randint(10000),
    "Numpy randint": kubik_numpy_randint(10000)
}

methods3 = {
    "Method randint": kubik_randint(1000000),
    "Method sample": kubik_sample(1000000),
    "Method randrange": kubik_randrange(1000000),
    "Loop randint": kubik_loop_randint(1000000),
    "Numpy randint": kubik_numpy_randint(1000000)
}

# Обработка данных и вычисление вероятностей для каждого метода
for method_name, results in methods.items():
    df = pd.DataFrame(results, columns=['Результаты'])
    frequency = df['Результаты'].value_counts().reset_index()
    frequency.columns = ['Число', 'Частота']
    frequency = probability_solving(frequency)
    print(f"\n{method_name}:\n", frequency)

for method_name, results in methods1.items():
    df1 = pd.DataFrame(results, columns=['Результаты'])
    frequency = df1['Результаты'].value_counts().reset_index()
    frequency.columns = ['Число', 'Частота']
    frequency = probability_solving(frequency)
    print(f"\n{method_name}:\n", frequency)

for method_name, results in methods2.items():
    df2 = pd.DataFrame(results, columns=['Результаты'])
    frequency = df2['Результаты'].value_counts().reset_index()
    frequency.columns = ['Число', 'Частота']
    frequency = probability_solving(frequency)
    print(f"\n{method_name}:\n", frequency)

for method_name, results in methods3.items():
    df3 = pd.DataFrame(results, columns=['Результаты'])
    frequency = df3['Результаты'].value_counts().reset_index()
    frequency.columns = ['Число', 'Частота']
    frequency = probability_solving(frequency)
    print(f"\n{method_name}:\n", frequency)

# Обработка данных и построение гистограмм
def process_and_plot(methods, num_rolls):
    for method_name, results in methods.items():
        df = pd.DataFrame(results, columns=['Результаты'])
        frequency = df['Результаты'].value_counts().reset_index()
        frequency.columns = ['Число', 'Частота']
        frequency = probability_solving(frequency)
        
        # Построение гистограммы
        ax = frequency.plot(x='Число', y='Частота', kind='bar', legend=False, color=np.random.rand(3,))
        ax.set_title(f'{method_name} для {num_rolls} бросков')
        ax.set_xlabel('Число')
        ax.set_ylabel('Частота')
        
        # Сохранение гистограммы
        plt.savefig(f'{method_name}_{num_rolls}_histogram.png')
        plt.close()

# Сбор данных для каждого метода и количества бросков
roll_counts = [100, 1000, 10000, 1000000]
methods_func = [kubik_randint, kubik_sample, kubik_randrange, kubik_loop_randint, kubik_numpy_randint]

for count in roll_counts:
    methods = {f"Method {i+1}": func(count) for i, func in enumerate(methods_func)}
    process_and_plot(methods, count)
