import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Розміри екрану
screen_width = 600
screen_height = 500

# Колір
white = (255, 255, 255)

# Створення вікна гри
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Простий рух")

# Початкові координати фігури
object_x = 50
object_y = 400
object_x2 = 50
object_y2 = 450
object_x3 = 50
object_y3 = 350
# Швидкість руху фігури
object_speed_x = -4
object_speed_y = 3
object_speed_x2 = 1
object_speed_y2 = 4
object_speed_x3 = 4
object_speed_y3 = 2
# Основний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рух фігури
    object_x += object_speed_y
    object_y += object_speed_x
    object_x2 += object_speed_y2
    object_y2 += object_speed_x2
    object_x3 += object_speed_y3
    object_y3 -= object_speed_x3

    # Перевірка на зіткнення з краями
    if object_x < 0 or object_x > screen_width - 50:
        object_speed_y = -object_speed_y
    if object_y < 0 or object_y > screen_height - 50:
        object_speed_x = -object_speed_x
    if object_x2 < 0 or object_x2 > screen_width - 50:
        object_speed_y2 = -object_speed_y2
    if object_y2 < 0 or object_y2 > screen_height - 50:
        object_speed_x2 = -object_speed_x2
    if object_x3 < 0 or object_x3 > screen_width - 50:
        object_speed_y3 = -object_speed_y3
    if object_y3 < 0 or object_y3 > screen_height - 50:
        object_speed_x3 = -object_speed_x3

    # Перевірка на зіткнення між квадратами
    if abs(object_x - object_x2) < 50 and abs(object_y - object_y2) < 50:
        object_speed_x, object_speed_x2 = object_speed_x2, object_speed_x
        object_speed_y, object_speed_y2 = object_speed_y2, object_speed_y
    if abs(object_x - object_x3) < 50 and abs(object_y - object_y3) < 50:
        object_speed_x, object_speed_x3 = object_speed_x3, object_speed_x
        object_speed_y, object_speed_y3 = object_speed_y3, object_speed_y
    if abs(object_x2 - object_x3) < 50 and abs(object_y2 - object_y3) < 50:
        object_speed_x2, object_speed_x3 = object_speed_x3, object_speed_x2
        object_speed_y2, object_speed_y3 = object_speed_y3, object_speed_y2

    # Очистити екран
    screen.fill(white)

    # Відобразити фігуру на екрані
    pygame.draw.rect(screen, (0, 255, 0), (object_x, object_y, 50, 50))
    pygame.draw.rect(screen, (255, 0, 0), (object_x2, object_y2, 50, 50))
    pygame.draw.rect(screen, (0, 0, 255), (object_x3, object_y3, 50, 50))
    # Оновити екран
    pygame.display.update()

    # Затримка для плавного руху
    pygame.time.delay(20)

# Завершення гри
pygame.quit()
sys.exit()
