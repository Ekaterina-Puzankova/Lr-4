import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
    dataframe['Вероятность'] = dataframe['Частота'] / sum_rate
    return dataframe

# Обработка данных и построение гистограмм
def process_and_plot(methods, num_rolls):
    for method_name, results in methods.items():
        df = pd.DataFrame(results, columns=['Результаты'])
        frequency = df['Результаты'].value_counts().reset_index()
        frequency.columns = ['Число', 'Частота']
        frequency = probability_solving(frequency)
        
        # Построение гистограммы с вероятностью
        ax = frequency.plot(x='Число', y='Вероятность', kind='bar', legend=False, color=np.random.rand(3,))
        ax.set_title(f'{method_name} для {num_rolls} бросков')
        ax.set_xlabel('Число')
        ax.set_ylabel('Вероятность')  # Изменено с 'Частота' на 'Вероятность'
        
        # Сохранение гистограммы
        plt.savefig(f'{method_name}_{num_rolls}_histogram.png')
        plt.close()

# Сбор данных для каждого метода и количества бросков
roll_counts = [100, 1000, 10000, 1000000]
methods_func = [kubik_randint, kubik_sample, kubik_randrange, kubik_loop_randint, kubik_numpy_randint]

for count in roll_counts:
    methods = {f"Method {i+1}": func(count) for i, func in enumerate(methods_func)}
    process_and_plot(methods, count)
