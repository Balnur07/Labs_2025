import pygame
import sys  # Импортируем модуль sys для взаимодействия с системой
import copy  # Импортируем модуль copy для создания копий объектов
import random  # Импортируем модуль random для работы с случайными числами
import time  # Импортируем модуль time для работы со временем

pygame.init()  # Инициализируем Pygame

# Устанавливаем параметры игры
scale = 15  # Масштаб объектов
score = 0  # Счет игрока
level = 0  # Уровень игры
SPEED = 10  # Скорость движения змейки

food_x = 10  # Координата x для еды
food_y = 10  # Координата y для еды

# Создаем окно для отображения игры
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")  # Устанавливаем заголовок окна
clock = pygame.time.Clock()  # Создаем объект Clock для управления временем в игре

# Определяем цвета в формате RGB
background_top = (0, 0, 50)  # Цвет верхнего уровня фона
background_bottom = (0, 0, 0)  # Цвет нижнего уровня фона
snake_colour = (255, 137, 0)  # Цвет змейки
food_colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # Цвет еды (случайный)
snake_head = (255, 247, 0)  # Цвет головы змейки
font_colour = (255, 255, 255)  # Цвет шрифта
defeat_colour = (255, 0, 0)  # Цвет при проигрыше


class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start  # Координата x начального положения змейки
        self.y = y_start  # Координата y начального положения змейки
        self.w = 15  # Ширина змейки
        self.h = 15  # Высота змейки
        self.x_dir = 1  # Направление движения по оси x (1 - вправо, -1 - влево)
        self.y_dir = 0  # Направление движения по оси y (1 - вниз, -1 - вверх)
        self.history = [[self.x, self.y]]  # История перемещений змейки
        self.length = 1  # Длина змейки

    def reset(self):
        self.x = 500 / 2 - scale  # Возвращаем змейку в центр по оси x
        self.y = 500 / 2 - scale  # Возвращаем змейку в центр по оси y
        self.w = 15  # Сбрасываем ширину змейки
        self.h = 15  # Сбрасываем высоту змейки
        self.x_dir = 1  # Сбрасываем направление по оси x
        self.y_dir = 0  # Сбрасываем направление по оси y
        self.history = [[self.x, self.y]]  # Сбрасываем историю перемещений
        self.length = 1  # Сбрасываем длину змейки

    def show(self):
        for i in range(self.length):
            if not i == 0:
                pygame.draw.rect(display, snake_colour, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:
                pygame.draw.rect(display, snake_head, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eaten(self):
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale:
            return True

    def check_level(self):
        global level
        if self.length % 5 == 0:
            return True

    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    def death(self):
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    def update(self):
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i - 1])
            i -= 1
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale


class Food:
    def __init__(self):
        self.creation_time = pygame.time.get_ticks()  # Устанавливаем время создания еды
        self.weight = random.randint(1, 3)  # Рандомный вес еды от 1 до 3

    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, int(500 / scale) - 1) * scale
        food_y = random.randrange(1, int(500 / scale) - 1) * scale
        self.creation_time = pygame.time.get_ticks()  # Сбрасываем время создания после перемещения

    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))

    def check_timer(self):
        current_time = pygame.time.get_ticks()  # Получаем текущее время в миллисекундах
        if current_time - self.creation_time > 5000:  # Если прошло более 5 секунд
            self.new_location()  # Перемещаем еду


def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, font_colour)
    display.blit(text, (scale, scale))


def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (90 - scale, scale))


def gameLoop():
    global score
    global level
    global SPEED

    snake = Snake(500 / 2, 500 / 2)
    food = Food()  # Создаем объект еды
    food.new_location()  # Устанавливаем начальное положение еды

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if snake.y_dir == 0:
                    if event.key == pygame.K_UP:
                        snake.x_dir = 0
                        snake.y_dir = -1
                    if event.key == pygame.K_DOWN:
                        snake.x_dir = 0
                        snake.y_dir = 1

                if snake.x_dir == 0:
                    if event.key == pygame.K_LEFT:
                        snake.x_dir = -1
                        snake.y_dir = 0
                    if event.key == pygame.K_RIGHT:
                        snake.x_dir = 1
                        snake.y_dir = 0

        for y in range(500):
            color = (
                background_top[0] + (background_bottom[0] - background_top[0]) * y / 500,
                background_top[1] + (background_bottom[1] - background_top[1]) * y / 500,
                background_top[2] + (background_bottom[2] - background_top[2]) * y / 500
            )
            pygame.draw.line(display, color, (0, y), (500, y))

        snake.show()
        snake.update()
        food.show()
        show_score()
        show_level()

        food.check_timer()  # Проверка таймера для еды

        if snake.check_eaten():
            food.new_location()
            score += food.weight  # Увеличиваем счет в зависимости от веса еды
            snake.grow()

        if snake.check_level():
            food.new_location()
            level += 1
            SPEED += 1
            snake.grow()

        if snake.death():
            score = 0
            level = 0
            font = pygame.font.SysFont(None, 100)
            text = font.render("Game Over!", True, defeat_colour)
            display.blit(text, (50, 200))
            pygame.display.update()
            time.sleep(3)
            snake.reset()

        if snake.history[0][0] > 500:
            snake.history[0][0] = 0

        if snake.history[0][0] < 0:
            snake.history[0][0] = 500

        if snake.history[0][1] > 500:
            snake.history[0][1] = 0
        if snake.history[0][1] < 0:
            snake.history[0][1] = 500

        pygame.display.update()
        clock.tick(SPEED)


gameLoop()

