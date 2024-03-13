import numpy as np
import matplotlib.pyplot as plt

# Кількість кидків
num_rolls = 100000

# Генерація випадкових чисел для кидків кубиків
rolls_1 = np.random.randint(1, 7, num_rolls)
rolls_2 = np.random.randint(1, 7, num_rolls)

# Обчислення суми чисел, що випали на обох кубиках
sum = rolls_1 + rolls_2

# Підрахунок, скільки разів кожна можлива сума з’являється
sum_counts = {total: np.sum(sum == total) for total in range(2, 13)}

# Обчислення ймовірностей
probabilities = {total: count / num_rolls for total, count in sum_counts.items()}

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), probabilities.values(), color='blue')
plt.xlabel('Сума чисел')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум чисел на двох кубиках (Метод Монте-Карло)')
plt.xticks(range(2, 13))
plt.grid(axis='y')
plt.show()
