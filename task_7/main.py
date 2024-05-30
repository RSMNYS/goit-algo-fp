import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}  # Ініціалізація лічильників сум від 2 до 12
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sums_count[roll_sum] += 1
    return sums_count

def calculate_probabilities(sums_count, num_rolls):
    probabilities = {roll_sum: (count / num_rolls) * 100 for roll_sum, count in sums_count.items()}
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for roll_sum, probability in sorted(probabilities.items()):
        print(f"{roll_sum}\t{probability:.2f}%")

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Сума')
    plt.ylabel('Імовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.show()

def main():
    num_rolls = 100000  # Велика кількість кидків
    sums_count = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(sums_count, num_rolls)
    print_probabilities(probabilities)
    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()
