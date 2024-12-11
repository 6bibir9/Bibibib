import tkinter as tk
import random

def roll_dice():
    try:
        input_text = entry.get()
        num_dice, dice_type = map(int, input_text.lower().split('d'))
        if num_dice <= 0 or dice_type <= 0:
            raise ValueError("Числа должны быть больше нуля.")
        
        results = [random.randint(1, dice_type) for _ in range(num_dice)]
        total = sum(results)
        result_label.config(text=f"Результаты: {results} | Сумма: {total}")
    except ValueError:
        result_label.config(text="Ошибка: Введите в формате 'XdY'.")

# Создаем основное окно
root = tk.Tk()
root.title("D&D Dice Roller")

# Создаем виджеты
label = tk.Label(root, text="Введите количество и тип кубиков (например, 2d6):")
label.pack()

entry = tk.Entry(root)
entry.pack()

roll_button = tk.Button(root, text="Бросить кубики", command=roll_dice)
roll_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Запускаем главный цикл приложения
root.mainloop()

