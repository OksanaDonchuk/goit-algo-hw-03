import turtle
from typing import Union

def koch_curve(t: turtle.Turtle, order: int, size: Union[int, float]) -> None:
    """
    Рекурсивно малює одну сторону фрактала «сніжинка Коха».

    Args:
        t (turtle.Turtle): Черепашка для малювання.
        order (int): Рівень рекурсії.
        size (Union[int, float]): Довжина лінії.
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order: int, size: Union[int, float] = 300) -> None:
    """
    Малює фрактал «сніжинка Коха» заданого рівня рекурсії.

    Args:
        order (int): Рівень рекурсії.
        size (Union[int, float]): Загальний розмір сніжинки.
    """
    # Налаштування екрану
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    # Налаштування черепашки
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість
    t.penup()
    # Центруємо сніжинку
    t.goto(-size / 2, size / (2 * 3**0.5))  # Центрування для трикутника
    t.pendown()

    # Малюємо три сторони сніжинки
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    # Завершення роботи
    window.mainloop()

if __name__ == "__main__":
    try:
        # Задаємо рівень рекурсії сніжинки
        order = int(input("Введіть рівень рекурсії сніжинки (0 або більше): "))
        if order < 0:
            raise ValueError("Рівень рекурсії не може бути від'ємним.")
        
        # Виклик функції
        draw_koch_snowflake(order)
    except ValueError as e:
        print(f"Помилка: {e}")