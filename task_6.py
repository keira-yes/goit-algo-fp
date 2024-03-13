def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item in sorted_items:
        name = item[0]
        cost = item[1]['cost']
        calories = item[1]['calories']
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories

    return selected_items, total_calories

def dynamic_programming(items, budget):
    # Ініціалізація таблиці для збереження максимальної калорійності для кожної суми грошей
    dp = [0] * (budget + 1)
    item_choice = [[] for _ in range(budget + 1)]

    for item, details in items.items():
        cost, calories = details['cost'], details['calories']
        for b in range(budget, cost - 1, -1):
            if dp[b] < dp[b - cost] + calories:
                dp[b] = dp[b - cost] + calories
                item_choice[b] = item_choice[b - cost] + [item]

    # Пошук максимальної калорійності в межах бюджету
    max_calories = max(dp)
    # Відновлення набору страв, які призвели до максимальної калорійності
    result_items = item_choice[dp.index(max_calories)]

    return result_items, max_calories


# Дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Тестування
budget = 100

print('Жадібний алгоритм: продукти, калорії', greedy_algorithm(items, budget))
print('Динамічне програмування: продукти, калорії', dynamic_programming(items, budget))
