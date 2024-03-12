import turtle

def draw_pifagor_tree(t, length, depth):
    """
    Малювання фрактала "дерево Піфагора" за допомогою рекурсії.

    :param t: Об'єкт черепахи для малювання
    :param length: Довжина початкового сегменту
    :param depth: Глибина рекурсії
    """
    if depth == 0:
        return
    t.forward(length)
    t.left(45)
    draw_pifagor_tree(t, length * 0.7, depth - 1)
    t.right(90)
    draw_pifagor_tree(t, length * 0.7, depth - 1)
    t.left(45)
    t.backward(length)

def get_depth():
    """
    Отримання рівня рекурсії від користувача
    """
    depth = turtle.numinput("Рівень рекурсії", "Введіть рівень рекурсії (ціле число більше або дорівнює 0): ", minval=0)
    return int(depth) if depth is not None else None

def draw_pifagor_tree_fractal():
    depth = get_depth()
    if depth is None:
        return

    # Ініціалізація черепахи
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)
    t.color("green")

    # Початкова позиція
    t.penup()
    t.goto(0, -200)
    t.setheading(90)
    t.pendown()

    # Малюємо фрактал "дерево Піфагора"
    draw_pifagor_tree(t, 150, depth)

    screen.mainloop()

if __name__ == "__main__":
    draw_pifagor_tree_fractal()
