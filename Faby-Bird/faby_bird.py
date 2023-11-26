# pygame template

import pygame
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#POINTS DISPLAY/WRITING
points = 0
points_text = "0"
number = ""
font = pygame.font.SysFont(None, 30)
bird_image = pygame.image.load("faby.png")
background = pygame.image.load("flappy_bird_background.webp")

#BIRD MOVEMENT
jump = False
bird_x = 10
bird_y = 200
jump_height = bird_y + 15
x_movespeed = 1
y_movespeed = 1
move_increase = pygame.USEREVENT + 0
time_interval = 50000
pygame.time.set_timer(pygame.USEREVENT, 10000 + time_interval)

#COLOURS \(^3^)/!!
WHITE = (255, 255, 255)
BLUE = (112, 198, 213)
GREEN = (117, 192, 14)
LIGHT_GREEN = (166, 233, 86)
DARK_GREEN = (67,125,0)
RED = (186, 72, 48)
LIGHT_RED = (186, 122, 48)
DARK_RED = (186, 48, 68)
YELLOW = (202, 203, 39)
LIGHT_YELLOW = (196, 253, 39)
DARK_YELLOW = (155, 155, 12)
BROWN = (66, 44, 42)
#INITAL PIPE COLOURS
pipe_colour1 = [GREEN, LIGHT_GREEN, DARK_GREEN]
pipe_colour2 = [RED, LIGHT_RED, DARK_RED]
pipe_colour3 = [YELLOW, LIGHT_YELLOW, DARK_YELLOW]
pipe_colour4 = [GREEN, LIGHT_GREEN, DARK_GREEN]

#PIPE POSITIONS
pipe1_x = 640
pipe1_y = random.randrange(205, 401)
pipe2_x = 815
pipe2_y = random.randrange(205, 401)
pipe3_x = 990
pipe3_y = random.randrange(205, 401)
pipe4_x = 1165
pipe4_y = random.randrange(205, 401)

#START GAME!!
running = True
while running:
#SCREEN COLOUR/BACKGROUND
    screen.fill(BLUE)
    screen.blit(background, (0, -200))

#BIRD
    screen.blit(bird_image, (bird_x, bird_y))
    bird = pygame.Rect(bird_x, bird_y, 30, 20)


#LOOP PIPES AND RANDOM COLOURS
    if pipe1_x <= -60:
        pipe1_x = 640
        pipe1_y = random.randrange(200, 401)
        pipe_colour1 = random.randrange(0, 3)
        if pipe_colour1 == 0:
            pipe_colour1 = [GREEN, LIGHT_GREEN, DARK_GREEN]
        elif pipe_colour1 == 1:
            pipe_colour1 = [YELLOW, LIGHT_YELLOW, DARK_YELLOW]
        elif pipe_colour1 == 2:
            pipe_colour1 = [RED, LIGHT_RED, DARK_RED]
    if pipe2_x <= -60:
        pipe2_x = 640
        pipe2_y = random.randrange(200, 401)
        pipe_colour2 = random.randrange(0, 3)
        if pipe_colour2 == 0:
            pipe_colour2 = [GREEN, LIGHT_GREEN, DARK_GREEN]
        elif pipe_colour2 == 1:
            pipe_colour2 = [YELLOW, LIGHT_YELLOW, DARK_YELLOW]
        elif pipe_colour2 == 2:
            pipe_colour2 = [RED, LIGHT_RED, DARK_RED]
    if pipe3_x <= -60:
        pipe3_x = 640
        pipe3_y = random.randrange(200, 401)
        pipe_colour3 = random.randrange(0, 3)
        if pipe_colour3 == 0:
            pipe_colour3 = [GREEN, LIGHT_GREEN, DARK_GREEN]
        elif pipe_colour3 == 1:
            pipe_colour3 = [YELLOW, LIGHT_YELLOW, DARK_YELLOW]
        elif pipe_colour3 == 2:
            pipe_colour3 = [RED, LIGHT_RED, DARK_RED]
    if pipe4_x <= -60:
        pipe4_x = 640
        pipe4_y = random.randrange(200, 401)
        pipe_colour4 = random.randrange(0, 3)
        if pipe_colour4 == 0:
            pipe_colour4 = [GREEN, LIGHT_GREEN, DARK_GREEN]
        elif pipe_colour4 == 1:
            pipe_colour4 = [YELLOW, LIGHT_YELLOW, DARK_YELLOW]
        elif pipe_colour4 == 2:
            pipe_colour4 = [RED, LIGHT_RED, DARK_RED]

#PIPE 1
    #BOTTOM PIPE
    pygame.draw.polygon(screen, pipe_colour1[0], ((pipe1_x, pipe1_y), (pipe1_x+60, pipe1_y), (pipe1_x+60, pipe1_y+35), (pipe1_x+55, pipe1_y+35), (pipe1_x+55, 480), (pipe1_x+5, 480), (pipe1_x+5, pipe1_y+35), (pipe1_x, pipe1_y+35)))
    pygame.draw.line(screen, pipe_colour1[1], (pipe1_x+8, pipe1_y), (pipe1_x+8, 480), 2)
    pygame.draw.line(screen, pipe_colour1[1], (pipe1_x+15, pipe1_y), (pipe1_x+15, 480), 5)
    pygame.draw.line(screen, WHITE, (pipe1_x+14, pipe1_y), (pipe1_x+14, 480))
    pygame.draw.line(screen, pipe_colour1[2], (pipe1_x+40, pipe1_y), (pipe1_x+40, 480), 3)
    pygame.draw.line(screen, pipe_colour1[2], (pipe1_x+50, pipe1_y), (pipe1_x+50, 480), 8)
    pygame.draw.rect(screen, pipe_colour1[1], [pipe1_x, pipe1_y, 8, 35])
    pygame.draw.rect(screen, pipe_colour1[2], [pipe1_x+54, pipe1_y, 8, 35])
    pygame.draw.polygon(screen, BROWN, ((pipe1_x, pipe1_y), (pipe1_x+60, pipe1_y), (pipe1_x+60, pipe1_y+35), (pipe1_x+55, pipe1_y+35), (pipe1_x+55, 480), (pipe1_x+5, 480), (pipe1_x+5, pipe1_y+35), (pipe1_x, pipe1_y+35)), 2)
    pygame.draw.line(screen, BROWN, (pipe1_x, pipe1_y+35), (pipe1_x+60, pipe1_y+35), 2)
#TOP PIPE
    pygame.draw.polygon(screen, pipe_colour1[0], ((pipe1_x, pipe1_y-100), (pipe1_x+60, pipe1_y-100), (pipe1_x+60, pipe1_y-135), (pipe1_x+55, pipe1_y-135), (pipe1_x+55, -2), (pipe1_x+5, -2), (pipe1_x+5, pipe1_y-135), (pipe1_x, pipe1_y-135)))
    pygame.draw.line(screen, pipe_colour1[1], (pipe1_x+8, pipe1_y-100), (pipe1_x+8, -2), 2)
    pygame.draw.line(screen, pipe_colour1[1], (pipe1_x+15, pipe1_y-100), (pipe1_x+15, -2), 5)
    pygame.draw.line(screen, WHITE, (pipe1_x+14, pipe1_y-100), (pipe1_x+14, -2))
    pygame.draw.line(screen, pipe_colour1[2], (pipe1_x+40, pipe1_y-100), (pipe1_x+40, -2), 3)
    pygame.draw.line(screen, pipe_colour1[2], (pipe1_x+50, pipe1_y-100), (pipe1_x+50, -2), 8)
    pygame.draw.rect(screen, pipe_colour1[1], [pipe1_x, pipe1_y-135, 8, 35])
    pygame.draw.rect(screen, pipe_colour1[2], [pipe1_x+54, pipe1_y-135, 8, 35])
    pygame.draw.polygon(screen, BROWN, ((pipe1_x, pipe1_y-100), (pipe1_x+60, pipe1_y-100), (pipe1_x+60, pipe1_y-135), (pipe1_x+55, pipe1_y-135), (pipe1_x+55, -2), (pipe1_x+5, -2), (pipe1_x+5, pipe1_y-135), (pipe1_x, pipe1_y-135)), 2)
    pygame.draw.line(screen, BROWN, (pipe1_x, pipe1_y-135), (pipe1_x+60, pipe1_y-135), 2)
    pipe1_point = pygame.Rect(pipe1_x+30, 0, 1, 480)
    bottom_pipe1 = pygame.Rect(pipe1_x, pipe1_y, 60, 480-pipe1_y)
    top_pipe1 = pygame.Rect(pipe1_x, 0, 60, pipe1_y-100)
#PIPE 2
    #BOTTOM PIPE
    pygame.draw.polygon(screen, pipe_colour2[0], ((pipe2_x, pipe2_y), (pipe2_x+60, pipe2_y), (pipe2_x+60, pipe2_y+35), (pipe2_x+55, pipe2_y+35), (pipe2_x+55, 480), (pipe2_x+5, 480), (pipe2_x+5, pipe2_y+35), (pipe2_x, pipe2_y+35)))
    pygame.draw.line(screen, pipe_colour2[1], (pipe2_x+8, pipe2_y), (pipe2_x+8, 480), 2)
    pygame.draw.line(screen, pipe_colour2[1], (pipe2_x+15, pipe2_y), (pipe2_x+15, 480), 5)
    pygame.draw.line(screen, WHITE, (pipe2_x+14, pipe2_y), (pipe2_x+14, 480))
    pygame.draw.line(screen, pipe_colour2[2], (pipe2_x+40, pipe2_y), (pipe2_x+40, 480), 3)
    pygame.draw.line(screen, pipe_colour2[2], (pipe2_x+50, pipe2_y), (pipe2_x+50, 480), 8)
    pygame.draw.rect(screen, pipe_colour2[1], [pipe2_x, pipe2_y, 8, 35])
    pygame.draw.rect(screen, pipe_colour2[2], [pipe2_x+54, pipe2_y, 8, 35])
    pygame.draw.polygon(screen, BROWN, ((pipe2_x, pipe2_y), (pipe2_x+60, pipe2_y), (pipe2_x+60, pipe2_y+35), (pipe2_x+55, pipe2_y+35), (pipe2_x+55, 480), (pipe2_x+5, 480), (pipe2_x+5, pipe2_y+35), (pipe2_x, pipe2_y+35)), 2)
    pygame.draw.line(screen, BROWN, (pipe2_x, pipe2_y+35), (pipe2_x+60, pipe2_y+35), 2)
    #TOP PIPE
    pygame.draw.polygon(screen, pipe_colour2[0], ((pipe2_x, pipe2_y-100), (pipe2_x+60, pipe2_y-100), (pipe2_x+60, pipe2_y-135), (pipe2_x+55, pipe2_y-135), (pipe2_x+55, -2), (pipe2_x+5, -2), (pipe2_x+5, pipe2_y-135), (pipe2_x, pipe2_y-135)))
    pygame.draw.line(screen, pipe_colour2[1], (pipe2_x+8, pipe2_y-100), (pipe2_x+8, -2), 2)
    pygame.draw.line(screen, pipe_colour2[1], (pipe2_x+15, pipe2_y-100), (pipe2_x+15, -2), 5)
    pygame.draw.line(screen, WHITE, (pipe2_x+14, pipe2_y-100), (pipe2_x+14, -2))
    pygame.draw.line(screen, pipe_colour2[2], (pipe2_x+40, pipe2_y-100), (pipe2_x+40, -2), 3)
    pygame.draw.line(screen, pipe_colour2[2], (pipe2_x+50, pipe2_y-100), (pipe2_x+50, -2), 8)
    pygame.draw.rect(screen, pipe_colour2[1], [pipe2_x, pipe2_y-135, 8, 35])
    pygame.draw.rect(screen, pipe_colour2[2], [pipe2_x+54, pipe2_y-135, 8, 35])
    pygame.draw.polygon(screen, BROWN, ((pipe2_x, pipe2_y-100), (pipe2_x+60, pipe2_y-100), (pipe2_x+60, pipe2_y-135), (pipe2_x+55, pipe2_y-135), (pipe2_x+55, -2), (pipe2_x+5, -2), (pipe2_x+5, pipe2_y-135), (pipe2_x, pipe2_y-135)), 2)
    pygame.draw.line(screen, BROWN, (pipe2_x, pipe2_y-135), (pipe2_x+60, pipe2_y-135), 2)
    pipe2_point = pygame.Rect(pipe2_x+30, 0, 1, 480)
    bottom_pipe2 = pygame.Rect(pipe2_x, pipe2_y, 60, 480-pipe2_y)
    top_pipe2 = pygame.Rect(pipe2_x, 0, 60, pipe2_y-100)
#PIPE 3
    #BOTTOM PIPE
    pygame.draw.polygon(screen, pipe_colour3[0], ((pipe3_x, pipe3_y), (pipe3_x+60, pipe3_y), (pipe3_x+60, pipe3_y+35), (pipe3_x+55, pipe3_y+35), (pipe3_x+55, 480), (pipe3_x+5, 480), (pipe3_x+5, pipe3_y+35), (pipe3_x, pipe3_y+35)))
    pygame.draw.line(screen, pipe_colour3[1], (pipe3_x+8, pipe3_y), (pipe3_x+8, 480), 2)
    pygame.draw.line(screen, pipe_colour3[1], (pipe3_x+15, pipe3_y), (pipe3_x+15, 480), 5)
    pygame.draw.line(screen, WHITE, (pipe3_x+14, pipe3_y), (pipe3_x+14, 480))
    pygame.draw.line(screen, pipe_colour3[2], (pipe3_x+40, pipe3_y), (pipe3_x+40, 480), 3)
    pygame.draw.line(screen, pipe_colour3[2], (pipe3_x+50, pipe3_y), (pipe3_x+50, 480), 8)
    pygame.draw.rect(screen, pipe_colour3[1], [pipe3_x, pipe3_y, 8, 35])
    pygame.draw.rect(screen, pipe_colour3[2], [pipe3_x+54, pipe3_y, 8, 35])
    pygame.draw.polygon(screen, BROWN, ((pipe3_x, pipe3_y), (pipe3_x+60, pipe3_y), (pipe3_x+60, pipe3_y+35), (pipe3_x+55, pipe3_y+35), (pipe3_x+55, 480), (pipe3_x+5, 480), (pipe3_x+5, pipe3_y+35), (pipe3_x, pipe3_y+35)), 2)
    pygame.draw.line(screen, BROWN, (pipe3_x, pipe3_y+35), (pipe3_x+60, pipe3_y+35), 2)
    #TOP PIPE
    pygame.draw.polygon(screen, pipe_colour3[0], ((pipe3_x, pipe3_y-100), (pipe3_x+60, pipe3_y-100), (pipe3_x+60, pipe3_y-135), (pipe3_x+55, pipe3_y-135), (pipe3_x+55, -2), (pipe3_x+5, -2), (pipe3_x+5, pipe3_y-135), (pipe3_x, pipe3_y-135)))
    pygame.draw.line(screen, pipe_colour3[1], (pipe3_x+8, pipe3_y-100), (pipe3_x+8, -2), 2)
    pygame.draw.line(screen, pipe_colour3[1], (pipe3_x+15, pipe3_y-100), (pipe3_x+15, -2), 5)
    pygame.draw.line(screen, WHITE, (pipe3_x+14, pipe3_y-100), (pipe3_x+14, -2))
    pygame.draw.line(screen, pipe_colour3[2], (pipe3_x+40, pipe3_y-100), (pipe3_x+40, -2), 3)
    pygame.draw.line(screen, pipe_colour3[2], (pipe3_x+50, pipe3_y-100), (pipe3_x+50, -2), 8)
    pygame.draw.rect(screen, pipe_colour3[1], [pipe3_x, pipe3_y-135, 8, 35])
    pygame.draw.rect(screen, pipe_colour3[2], [pipe3_x+54, pipe3_y-135, 8, 35])
    pygame.draw.polygon(screen, BROWN, ((pipe3_x, pipe3_y-100), (pipe3_x+60, pipe3_y-100), (pipe3_x+60, pipe3_y-135), (pipe3_x+55, pipe3_y-135), (pipe3_x+55, -2), (pipe3_x+5, -2), (pipe3_x+5, pipe3_y-135), (pipe3_x, pipe3_y-135)), 2)
    pygame.draw.line(screen, BROWN, (pipe3_x, pipe3_y-135), (pipe3_x+60, pipe3_y-135), 2)
    pipe3_point = pygame.Rect(pipe3_x+30, 0, 1, 480)
    bottom_pipe3 = pygame.Rect(pipe3_x, pipe3_y, 60, 480-pipe3_y)
    top_pipe3 = pygame.Rect(pipe3_x, 0, 60, pipe3_y-100)
#PIPE 4
    #BOTTOM PIPE
    pygame.draw.polygon(screen, pipe_colour4[0], ((pipe4_x, pipe4_y), (pipe4_x+60, pipe4_y), (pipe4_x+60, pipe4_y+35), (pipe4_x+55, pipe4_y+35), (pipe4_x+55, 480), (pipe4_x+5, 480), (pipe4_x+5, pipe4_y+35), (pipe4_x, pipe4_y+35)))
    pygame.draw.line(screen, pipe_colour4[1], (pipe4_x+8, pipe4_y), (pipe4_x+8, 480), 2)
    pygame.draw.line(screen, pipe_colour4[1], (pipe4_x+15, pipe4_y), (pipe4_x+15, 480), 5)
    pygame.draw.line(screen, WHITE, (pipe4_x+14, pipe4_y), (pipe4_x+14, 480))
    pygame.draw.line(screen, pipe_colour4[2], (pipe4_x+40, pipe4_y), (pipe4_x+40, 480), 3)
    pygame.draw.line(screen, pipe_colour4[2], (pipe4_x+50, pipe4_y), (pipe4_x+50, 480), 8)
    pygame.draw.rect(screen, pipe_colour4[1], [pipe4_x, pipe4_y, 8, 35])
    pygame.draw.rect(screen, pipe_colour4[2], [pipe4_x+54, pipe4_y, 8, 35])
    pygame.draw.polygon(screen, BROWN, ((pipe4_x, pipe4_y), (pipe4_x+60, pipe4_y), (pipe4_x+60, pipe4_y+35), (pipe4_x+55, pipe4_y+35), (pipe4_x+55, 480), (pipe4_x+5, 480), (pipe4_x+5, pipe4_y+35), (pipe4_x, pipe4_y+35)), 2)
    pygame.draw.line(screen, BROWN, (pipe4_x, pipe4_y+35), (pipe4_x+60, pipe4_y+35), 2)
    #TOP PIPE
    pygame.draw.polygon(screen, pipe_colour4[0], ((pipe4_x, pipe4_y-100), (pipe4_x+60, pipe4_y-100), (pipe4_x+60, pipe4_y-135), (pipe4_x+55, pipe4_y-135), (pipe4_x+55, -2), (pipe4_x+5, -2), (pipe4_x+5, pipe4_y-135), (pipe4_x, pipe4_y-135)))
    pygame.draw.line(screen, pipe_colour4[1], (pipe4_x+8, pipe4_y-100), (pipe4_x+8, -2), 2)
    pygame.draw.line(screen, pipe_colour4[1], (pipe4_x+15, pipe4_y-100), (pipe4_x+15, -2), 5)
    pygame.draw.line(screen, WHITE, (pipe4_x+14, pipe4_y-100), (pipe4_x+14, -2))
    pygame.draw.line(screen, pipe_colour4[2], (pipe4_x+40, pipe4_y-100), (pipe4_x+40, -2), 3)
    pygame.draw.line(screen, pipe_colour4[2], (pipe4_x+50, pipe4_y-100), (pipe4_x+50, -2), 8)
    pygame.draw.rect(screen, pipe_colour4[1], [pipe4_x, pipe4_y-135, 8, 35])
    pygame.draw.rect(screen, pipe_colour4[2], [pipe4_x+54, pipe4_y-135, 8, 35])
    pygame.draw.polygon(screen, BROWN, ((pipe4_x, pipe4_y-100), (pipe4_x+60, pipe4_y-100), (pipe4_x+60, pipe4_y-135), (pipe4_x+55, pipe4_y-135), (pipe4_x+55, -2), (pipe4_x+5, -2), (pipe4_x+5, pipe4_y-135), (pipe4_x, pipe4_y-135)), 2)
    pygame.draw.line(screen, BROWN, (pipe4_x, pipe4_y-135), (pipe4_x+60, pipe4_y-135), 2)
    pipe4_point = pygame.Rect(pipe4_x+30, 0, 1, 480)
    bottom_pipe4 = pygame.Rect(pipe4_x, pipe4_y, 60, 480-pipe4_y)
    top_pipe4 = pygame.Rect(pipe4_x, 0, 60, pipe4_y-100)

#BIRD JUMPING
    if jump == False:
        bird_y += y_movespeed
    elif jump == True:
        bird_y -= y_movespeed
        if bird_y <= jump_height:
            jump = False

#MOVING PIPES
    pipe1_x -= x_movespeed
    pipe2_x -= x_movespeed
    pipe3_x -= x_movespeed
    pipe4_x -= x_movespeed

#POINTS TALLY
    #POINT NUMBER
    if bird.colliderect(pipe1_point) or bird.colliderect(pipe2_point) or bird.colliderect(pipe3_point) or bird.colliderect(pipe4_point):
        if x_movespeed == 1:
            points += 1
        elif x_movespeed == 2:
            points += 2
        elif x_movespeed == 3:
            points += 3
        elif x_movespeed == 4:
            points += 4
        elif x_movespeed == 5:
            points += 5
        elif x_movespeed == 6:
            points += 6
        points_text = str(points)
    #POINTS DISPLAY
    number = font.render(points_text, True, WHITE)
    screen.blit(number, (number.get_rect(center = screen.get_rect().center)[0], number.get_rect(center = screen.get_rect().center)[1]-200))

#GAME OVER (YOU ARE BAD AT BAD FLAPPY BIRD ;:D)
    if bird.colliderect(bottom_pipe1) or bird.colliderect(bottom_pipe2) or bird.colliderect(bottom_pipe3) or bird.colliderect(bottom_pipe4):
        running = False
    if bird.colliderect(top_pipe1) or bird.colliderect(top_pipe2) or bird.colliderect(top_pipe3) or bird.colliderect(top_pipe4):
        running = False
    if bird_y <= -30 or bird_y >= 480:
        running = False

#EVENTS LOOP
    for event in pygame.event.get():
        #QUITTER PT. 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                jump = True
                jump_height = bird_y - 20
        #QUITTER PT. 2
        elif event.type == pygame.QUIT:
            running = False
        #INCREASE SPEED
        if event.type == move_increase:
            if x_movespeed < 7:
                x_movespeed += 1
            if y_movespeed < 7:
                y_movespeed += 1
            time_interval -= 5000
            #WARNINGS
            print(f"Your move speed has increased to {x_movespeed}") 
            print(f"Time till next speed boost: {time_interval/1000+10}s")

#DISLAY UPDATE AND FPS
    pygame.display.flip()
    clock.tick(30)

#YOU FINISHED, FINAL POINTS
print(f"Your score is {points}")
pygame.time.delay(1500)
pygame.quit()