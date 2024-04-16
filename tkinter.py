import tkinter as tk
import random

def move_left(event):
    canvas.move(hero, -10, 0)
    check_collision()

def move_right(event):
    canvas.move(hero, 10, 0)
    check_collision()

def move_up(event):
    canvas.move(hero, 0, -10)
    check_collision()

def move_down(event):
    canvas.move(hero, 0, 10)
    check_collision()

def create_enemy():
    x = random.randint(0, width)
    y = random.randint(0, height)
    enemy = canvas.create_rectangle(x, y, x + 30, y + 30, fill="red")
    enemies.append(enemy)

def check_collision():
    global score
    hero_coords = canvas.coords(hero)
    for enemy in enemies.copy():
        enemy_coords = canvas.coords(enemy)
        if (hero_coords[0] < enemy_coords[2] and
            hero_coords[2] > enemy_coords[0] and
            hero_coords[1] < enemy_coords[3] and
            hero_coords[3] > enemy_coords[1]):
            canvas.delete(enemy)
            enemies.remove(enemy)
            score += 1
            update_score()

def update_score():
    canvas.itemconfig(score_display, text=f"Score: {score}")

# Створюємо вікно гри
root = tk.Tk()
root.title("Гра з героєм і ворогами")

# Розмір вікна гри
width = 800
height = 600

# Встановлюємо розмір вікна гри
root.geometry(f"{width}x{height}")

# Створюємо поле для гри
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Додаємо героя
hero = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

# Створюємо список ворогів
enemies = []

# Додаємо ворогів
for _ in range(5):
    create_enemy()

# Реакція на клавіші
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

# Лічильник балів
score = 0
score_display = canvas.create_text(50, 50, text=f"Score: {score}", font=("Arial", 16), fill="black")

# Основний цикл вікна гри
root.mainloop()
