def dynamic_programming(items, budget):
    # Ініціалізація таблиці dp
    dp = [0] * (budget + 1)
    item_choice = [[[] for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    # Перетворюємо items у список для зручного ітерації
    item_list = list(items.items())

    for i in range(1, len(item_list) + 1):
        item_name, item_info = item_list[i - 1]
        cost = item_info['cost']
        calories = item_info['calories']

        for w in range(budget, cost - 1, -1):
            if dp[w - cost] + calories > dp[w]:
                dp[w] = dp[w - cost] + calories
                item_choice[i][w] = item_choice[i - 1][w - cost] + [item_name]
            else:
                item_choice[i][w] = item_choice[i - 1][w]

    max_calories = dp[budget]
    selected_items = item_choice[len(item_list)][budget]
    result = {item: items[item] for item in selected_items}

    return result, max_calories

# Приклад використання:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

dp_result, dp_calories = dynamic_programming(items, budget)
print("Dynamic Programming Result:", dp_result)
print("Total Calories (DP):", dp_calories)
