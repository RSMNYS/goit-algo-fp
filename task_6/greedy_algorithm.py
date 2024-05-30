def greedy_algorithm(items, budget):
    # Сортуємо за співвідношенням калорій до вартості в порядку спадання
    sorted_items = sorted(items.items(), key=lambda item: item[1]['calories'] / item[1]['cost'], reverse=True)
    
    result = {}
    total_calories = 0
    remaining_budget = budget

    for item, info in sorted_items:
        if info['cost'] <= remaining_budget:
            result[item] = info
            total_calories += info['calories']
            remaining_budget -= info['cost']

    return result, total_calories

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

greedy_result, greedy_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm Result:", greedy_result)
print("Total Calories (Greedy):", greedy_calories)
