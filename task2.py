import turtle

def draw_pythagoras_tree(branch_len, level, t):
    if level > 0:
        # Малюємо основну гілку
        t.forward(branch_len)
        
        # Зберігаємо позицію та кут для правого відгалуження
        t.right(45)
        draw_pythagoras_tree(branch_len * 0.7, level - 1, t)
        
        # Повертаємося до позиції для лівого відгалуження
        t.left(90)
        draw_pythagoras_tree(branch_len * 0.7, level - 1, t)
        
        # Повертаємо черепашку у вихідний стан для коректної роботи рекурсії
        t.right(45)
        t.backward(branch_len)

def main():
    # Налаштування екрану
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")
    
    # Створення об'єкта черепашки
    t = turtle.Turtle()
    t.speed(0)  # Найшвидша анімація
    t.left(90)  # Повертаємо вгору
    t.color("brown")
    
    # Запит рівня рекурсії у користувача
    try:
        recursion_level = int(input("Введіть рівень рекурсії (рекомендовано від 5 до 10): "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    # Початкова позиція (зсуваємо вниз екрану)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    # Малювання дерева
    print("Малюю...")
    draw_pythagoras_tree(100, recursion_level, t)
    
    print("Готово!")
    screen.mainloop()

if __name__ == "__main__":
    main()