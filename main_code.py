
import pygame
import random

pygame.init()

image = pygame.image.load("C:\\Users\\SANK8\\Desktop\\snake.jpg")
# colours
red = (255, 0, 0)
blue = (23, 72, 23)
green = (55, 95, 4)

# Setting the screen
screen_x = 900
screen_y = 400
screen = pygame.display.set_mode((screen_x, screen_y))

# adding the screen titile
pygame.display.set_caption("Sanket's Snake Game..!")

# defining snake values
snake_x = 40
snake_y = 40
snake_size = 20

snake_img=pygame.image.load("C:\\Users\\SANK8\\Desktop\\snake_head.png")
snake_head_extra = pygame.image.load("C:\\Users\\SANK8\\Desktop\\snake_head _extra.png")
food=pygame.image.load("C:\\Users\\SANK8\\Desktop\\food.png")
# defining velocity
velocity_x = 0
velocity_y = 0
fps = 60

score = 0

# for food
food_x = random.randint(0, screen_x)
food_y = random.randint(0, screen_y)
food_size = 15
clock = pygame.time.Clock()

game_exit = False
game_over = False

snake_list = []
snake_length = 1

font = pygame.font.SysFont(None, 40)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])


def screen_game_over(text, color, x, y):
    font_game_over = pygame.font.SysFont(None, 80)
    screen_text = font_game_over.render(text, True, color)
    screen.blit(screen_text, [x, y])


def plot_new_big_snake(snake_list):
    for x, y in snake_list:

        screen.blit(snake_head_extra,[x,y])
     


def game_ov(a):
    if a is True:
        screen.fill(red)

        screen_game_over("GAME OVER (PRESS ENTER TO RESTART)", red, 400, 400)
        pygame.display.update()


while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -10

            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    screen.fill(green)
    screen.blit(image, (0, 0))

    if abs(snake_x - food_x) < 25 and abs(snake_y - food_y) < 25:
        score += 1
        print("Score", score)
        food_x = random.randint(100, 800)
        food_y = random.randint(80, 350)
        snake_length += 2

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    text_screen("SCORE BOARD : " + str(score * 10), (0, 0, 0), 5, 5)
    if len(snake_list) > snake_length:
        del snake_list[0]

    plot_new_big_snake(snake_list)

    screen.blit(snake_img,[snake_x,snake_y])
    screen.blit(food,[food_x,food_y])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()


