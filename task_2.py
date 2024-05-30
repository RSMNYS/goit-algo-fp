import turtle
import math

# Функція для малювання гілок дерева
def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return

    # Малюємо стовбур
    t.forward(length)

    # Малюємо ліву гілку
    angle = 45
    t.left(angle)
    draw_pythagoras_tree(t, length * math.cos(math.radians(angle)), level - 1)
    t.right(angle)

    # Малюємо праву гілку
    angle = 45
    t.right(angle)
    draw_pythagoras_tree(t, length * math.cos(math.radians(angle)), level - 1)
    t.left(angle)

    # Повертаємося до початкової точки
    t.backward(length)


def main():
    screen = turtle.Screen()
    screen.title("Pythagoras Tree")

    # Вибір рівня рекурсії
    level = int(input("Enter the recursion level: "))

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання

    t.left(90)
    t.up()
    t.backward(200)
    t.down()

    # Малюємо дерево Піфагора
    draw_pythagoras_tree(t, 100, level)

    screen.mainloop()

if __name__ == "__main__":
    main()
