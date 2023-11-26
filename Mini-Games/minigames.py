import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (126, 126, 126)
DARK_GREY = (63, 63, 63)
LIGHT_GREY = (209, 209, 209)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SEA_GREEN = (53, 140, 64)
PEA_GREEN = (36, 109, 71)
EVERGLADE_GREEN = (27, 71, 47)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (165, 150, 146)
ORANGE = (255, 165, 0)
GOLD = (255, 215, 0)
PURPLE = (200, 116, 178)
SPACE = (50, 50, 50)
ASTEROID = (165, 150, 146)
ASTRONAUT = (240, 240, 240)


global game_complete1
game_complete1 = False
global game_complete2
game_complete2 = False
global game_complete3
game_complete3 = False
global game_complete4
game_complete4 = False
global games_complete
games_complete = 0
global complete
complete = False

pygame.init()
pygame.font.init()
pygame.display.set_caption('Mini Games')
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

global screen
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

def main_menu():
    star_list=[]
    for i in range (100):
        x = random.randrange(-480, 320)
        y = random.randrange(-300, 0)
        star_list.append([x,y])
    global games_complete
    if games_complete == 4:
        global complete
        complete = True
    colour_change = 0
    colour = RED

    click = False
    while True:
        if games_complete == 4:
            complete = True

        mx, my = pygame.mouse.get_pos()

        screen.fill(BLACK)

        
        for item in star_list:
            item[0] += 1
            item[1] += 1
            pygame.draw.circle(screen, WHITE, item, 3)
            if item[0] > 640 or item[1] > 480:
                item[0] = random.randrange(-480, 320)
                item[1] = random.randrange(-300, 0)

        title_font = pygame.font.SysFont("papyrus", 50)
        select_title = title_font.render('Welcome, Select Game', True, PURPLE)
        screen.blit(select_title, (select_title.get_rect(center = screen.get_rect().center)[0], select_title.get_rect(center = screen.get_rect().center)[1]-200))
        if games_complete < 4:
            completion_title = title_font.render(f'Games Complete: {games_complete}', True, PURPLE)
            screen.blit(completion_title, (completion_title.get_rect(center = screen.get_rect().center)[0], completion_title.get_rect(center = screen.get_rect().center)[1]+200))
        if complete:
            colour_change += 1
            if colour_change == 60:
                colour_change = 0
            if colour_change in range(0, 15):
                colour = RED
            elif colour_change in range(15, 30):
                colour = GREEN
            elif colour_change in range(30, 45):
                colour = BLUE
            elif colour_change in range(45, 60):
                colour = GOLD
            complete_text = title_font.render('Complete', True, colour)
            screen.blit(complete_text, (complete_text.get_rect(center = screen.get_rect().center)[0], complete_text.get_rect(center = screen.get_rect().center)[1]+200))

#makes the shapes and colours it 
        game1 = pygame.Rect(50,120,250,110)
        pygame.draw.rect(screen, PURPLE, game1)
        game2 = pygame.Rect(340,120,250,110)
        pygame.draw.rect(screen, PURPLE, game2)
        game3 = pygame.Rect(50,270,250,110)
        pygame.draw.rect(screen, PURPLE, game3)
        game4 = pygame.Rect(340,270,250,110)
        pygame.draw.rect(screen, PURPLE, game4)
        
        game_font = pygame.font.SysFont(None, 30)
        game_title1 = game_font.render('Asteroid Avoid', True, BLACK)
        screen.blit(game_title1, (game_title1.get_rect(center = screen.get_rect().center)[0]-145, game_title1.get_rect(center = screen.get_rect().center)[1]-65))
        game_title2 = game_font.render('Fuse Defuse', True, BLACK)
        screen.blit(game_title2, (game_title2.get_rect(center = screen.get_rect().center)[0]+150, game_title2.get_rect(center = screen.get_rect().center)[1]-65))
        game_title3 = game_font.render('Camo Clicker', True, BLACK)
        screen.blit(game_title3, (game_title3.get_rect(center = screen.get_rect().center)[0]-145, game_title3.get_rect(center = screen.get_rect().center)[1]+85))
        game_title4 = game_font.render('Asteroid Attack', True, BLACK)
        screen.blit(game_title4, (game_title4.get_rect(center = screen.get_rect().center)[0]+150, game_title4.get_rect(center = screen.get_rect().center)[1]+85))


        if game1.collidepoint((mx, my)):
            pygame.draw.rect(screen,RED,game1,5)
            if click:
                game_num1()
        else:
            pygame.draw.rect(screen,BLACK,game1,5)
        if game2.collidepoint((mx, my)):
            pygame.draw.rect(screen,RED,game2,5)
            if click:
                game_num2()
        else:
            pygame.draw.rect(screen,BLACK,game2,5)
        if game3.collidepoint((mx, my)):
            pygame.draw.rect(screen,RED,game3,5)
            if click:
               game_num3()
        else:
            pygame.draw.rect(screen,BLACK,game3,5)
        if game4.collidepoint((mx, my)):
            pygame.draw.rect(screen,RED,game4,5)
            if click:
                game_num4()
        else:
            pygame.draw.rect(screen,BLACK,game4,5)


        font = pygame.font.SysFont(None, 50)

#lets program know if a key is pressed
        click = False
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                pygame.quit()
          if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
              click = True
  
        pygame.display.update()
        clock.tick(60)

#ANDREAS CHOWDER
def game_num1():


    #Initializations
    points = 0
    x_speed = 4
    x_distance = 981
    lives = 3
    life = True
    end = False
    some_font = pygame.font.SysFont('Arial', 50)
    star_list=[]
    for i in range (100):
        x = random.randrange(-480, 320)
        y = random.randrange(-300, 0)
        star_list.append([x,y])
    #Positions of Asteroids
    asteroid_1_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
    asteroid_2_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
    asteroid_3_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
    asteroid_4_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
    asteroid_5_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
    asteroid_6_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
    asteroid_7_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
    asteroid_8_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
    asteroid_9_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
    asteroid_10_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
    asteroid_11_pos = [-30, random.randrange(0, 481)]
    asteroid_12_pos = [-30, random.randrange(0, 481)]
    asteroid_13_pos = [-30, random.randrange(0, 481)]
    asteroid_14_pos = [-30, random.randrange(0, 481)]
    asteroid_15_pos = [-30, random.randrange(0, 481)]
    asteroid_16_pos = [-30, random.randrange(0, 481)]
    asteroid_17_pos = [-30, random.randrange(0, 481)]
    asteroid_18_pos = [-30, random.randrange(0, 481)]
    asteroid_19_pos = [-30, random.randrange(0, 481)]
    asteroid_20_pos = [-30, random.randrange(0, 481)]

    #Speed of Asteroids
    asteroid_1_move = random.randint(3, x_speed)
    asteroid_2_move = random.randint(3, x_speed)
    asteroid_3_move = random.randint(3, x_speed)
    asteroid_4_move = random.randint(3, x_speed)
    asteroid_5_move = random.randint(3, x_speed)
    asteroid_6_move= random.randint(3, x_speed)
    asteroid_7_move = random.randint(3, x_speed)
    asteroid_8_move = random.randint(3, x_speed)
    asteroid_9_move = random.randint(3, x_speed)
    asteroid_10_move = random.randint(3, x_speed)
    asteroid_11_move = random.randint(3, x_speed)
    asteroid_12_move = random.randint(3, x_speed)
    asteroid_13_move = random.randint(3, x_speed)
    asteroid_14_move = random.randint(3, x_speed)
    asteroid_15_move = random.randint(3, x_speed)
    asteroid_17_move = random.randint(3, x_speed)
    asteroid_18_move = random.randint(3, x_speed)
    asteroid_19_move = random.randint(3, x_speed)
    asteroid_20_pos_move = random.randint(3, x_speed)

    #Asteroid Size
    roid_size_1 = random.randrange(10, 30)
    roid_size_2 = random.randrange(10, 30)
    roid_size_3 = random.randrange(10, 30)
    roid_size_4 = random.randrange(10, 30)
    roid_size_5 = random.randrange(10, 30)
    roid_size_6 = random.randrange(10, 30)
    roid_size_7 = random.randrange(10, 30)
    roid_size_8 = random.randrange(10, 30)
    roid_size_9 = random.randrange(10, 30)
    roid_size_10 = random.randrange(10, 30)
    roid_size_11= random.randrange(10, 30)
    roid_size_12 = random.randrange(10, 30)
    roid_size_13 = random.randrange(10, 30)
    roid_size_14 = random.randrange(10, 30)
    roid_size_15 = random.randrange(10, 30)
    roid_size_16 = random.randrange(10, 30)
    roid_size_17 = random.randrange(10, 30)
    roid_size_18 = random.randrange(10, 30)
    roid_size_19 = random.randrange(10, 30)
    roid_size_20 = random.randrange(10, 30)
    #-------------------------------------------------------------------

    # EVENT HANDLING
    click = False
    intro = True
    running = True
    while running:
        astro_x, astro_y = pygame.mouse.get_pos()
        if not end:
            if lives == 0 or points == 100:
                end = True               
            screen.fill(SPACE)
    #Main Menu Background Code
            if intro:
                for item in star_list:
                    item[0] += 1
                    item[1] += 1
                    pygame.draw.circle(screen, WHITE, item, 3)
                    if item[0] > 640 or item[1] > 480:
                        item[0] = random.randrange(-480, 320)
                        item[1] = random.randrange(-300, 0)

    #Main Menu Stuff
                some_font = pygame.font.SysFont('Arial', 50)
                description = some_font.render("Avoid the Asteroid!", True, (WHITE))
                some_font = pygame.font.SysFont('Arial', 20)
                instructions = some_font.render("*Note: You lose a life if your MOUSE hits an Asteroid.", True, WHITE)
                some_font = pygame.font.SysFont('Arial', 15)
                credits = some_font.render("*Background Credits to Rishab!", True, WHITE)
                screen.blit(description, (description.get_rect(center = screen.get_rect().center)[0], description.get_rect(center = screen.get_rect().center)[1]-70))
                screen.blit(instructions, (instructions.get_rect(center = screen.get_rect().center)[0], instructions.get_rect(center = screen.get_rect().center)[1]+75))
                screen.blit(credits, (credits.get_rect(center = screen.get_rect().center)[0], credits.get_rect(center = screen.get_rect().center)[1]+200))
                start_button = pygame.Rect([220, 200, 200, 80])
                pygame.draw.rect(screen, (GOLD), start_button)
                some_font = pygame.font.SysFont('Arial', 50)
                start_title = some_font.render("START", True, WHITE)
                screen.blit(start_title, (start_title.get_rect(center = screen.get_rect().center)[0], start_title.get_rect(center = screen.get_rect().center)[1]))
                if start_button.collidepoint((astro_x, astro_y)):
                    if click:
                        intro = False
            else:
        
        
    # Drawing Asteroids
                asteroid_1 = pygame.draw.circle(screen, ASTEROID, (asteroid_1_pos), roid_size_1)
                asteroid_2 = pygame.draw.circle(screen, ASTEROID, (asteroid_2_pos), roid_size_2)
                asteroid_3 = pygame.draw.circle(screen, ASTEROID, (asteroid_3_pos), roid_size_3)
                asteroid_4 = pygame.draw.circle(screen, ASTEROID, (asteroid_4_pos), roid_size_4)
                asteroid_5 = pygame.draw.circle(screen, ASTEROID, (asteroid_5_pos), roid_size_5)
                asteroid_6 = pygame.draw.circle(screen, ASTEROID, (asteroid_6_pos), roid_size_6)
                asteroid_7 = pygame.draw.circle(screen, ASTEROID, (asteroid_7_pos), roid_size_7)
                asteroid_8 = pygame.draw.circle(screen, ASTEROID, (asteroid_8_pos), roid_size_8)
                asteroid_9 = pygame.draw.circle(screen, ASTEROID, (asteroid_9_pos), roid_size_9)
                asteroid_10 = pygame.draw.circle(screen, ASTEROID, (asteroid_10_pos), roid_size_10)
                asteroid_11 = pygame.draw.circle(screen, ASTEROID, (asteroid_11_pos), roid_size_11)
                asteroid_12 = pygame.draw.circle(screen, ASTEROID, (asteroid_12_pos), roid_size_12)
                asteroid_13 = pygame.draw.circle(screen, ASTEROID, (asteroid_13_pos), roid_size_13)
                asteroid_14 = pygame.draw.circle(screen, ASTEROID, (asteroid_14_pos), roid_size_14)
                asteroid_15 = pygame.draw.circle(screen, ASTEROID, (asteroid_15_pos), roid_size_15)
                asteroid_16 = pygame.draw.circle(screen, ASTEROID, (asteroid_16_pos), roid_size_16)
                asteroid_17 = pygame.draw.circle(screen, ASTEROID, (asteroid_17_pos), roid_size_17)
                asteroid_18 = pygame.draw.circle(screen, ASTEROID, (asteroid_18_pos), roid_size_18)
                asteroid_19 = pygame.draw.circle(screen, ASTEROID, (asteroid_19_pos), roid_size_19)
                asteroid_20 = pygame.draw.circle(screen, ASTEROID, (asteroid_20_pos), roid_size_20)
                
            
    #Asteroid Speed Increments
                asteroid_1_pos[0] -= asteroid_1_move
                asteroid_2_pos[0] -= asteroid_2_move
                asteroid_3_pos[0] -= asteroid_3_move
                asteroid_4_pos[0] -= asteroid_4_move
                asteroid_5_pos[0] -= asteroid_5_move
                asteroid_6_pos[0] -= asteroid_6_move
                asteroid_7_pos[0] -= asteroid_7_move
                asteroid_8_pos[0] -= asteroid_8_move
                asteroid_9_pos[0] -= asteroid_9_move
                asteroid_10_pos[0] -= asteroid_10_move
                asteroid_11_pos[0] -= asteroid_11_move
                asteroid_12_pos[0] -= asteroid_12_move
                asteroid_13_pos[0] -= asteroid_13_move
                asteroid_14_pos[0] -= asteroid_14_move
                asteroid_15_pos[0] -= asteroid_15_move
                asteroid_16_pos[0] -= asteroid_15_move
                asteroid_17_pos[0] -= asteroid_15_move
                asteroid_18_pos[0] -= asteroid_15_move
                asteroid_19_pos[0] -= asteroid_15_move
                asteroid_20_pos[0] -= asteroid_15_move
            
    # Speed + Spawn Mechanic
                if asteroid_1_pos[0] <= -30 and asteroid_2_pos[0] <= -30 and asteroid_3_pos[0] <= -30 and asteroid_4_pos[0] <= -30 and asteroid_5_pos[0] <= -30 and asteroid_6_pos[0] <= -30 and asteroid_7_pos[0] <= -30 and asteroid_8_pos[0] <= -30 and asteroid_9_pos[0] <= -30 and asteroid_10_pos[0] <= -30 and asteroid_11_pos[0] <= -30 and asteroid_12_pos[0] <= -30 and asteroid_13_pos[0] <= -30 and asteroid_14_pos[0] <= -30 and asteroid_15_pos[0] <= -30 and asteroid_16_pos[0] <= -30 and asteroid_17_pos[0] <= -30 and asteroid_18_pos[0] <= -30 and asteroid_19_pos[0] <= -30 and asteroid_20_pos[0] <= -30: #Checks to see if asteroids passed
                    if x_speed <= 24:
                        x_speed += 2
                    points += 9
                    x_distance -= 10 #Distance Asteroid can be spawned in
            
    #Reset the Asteroids after each point
                if points == 9 or points == 19 or points == 29 or points == 39 or points == 49 or points == 59 or points == 69 or points == 79 or points == 89 or points == 99:
                    points += 1
                    asteroid_1_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    asteroid_2_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    asteroid_3_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    asteroid_4_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    asteroid_5_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    asteroid_6_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    asteroid_7_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    asteroid_8_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    asteroid_9_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    asteroid_10_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    
                    #Adding an Asteroid after each round
                    if points == 9:
                        asteroid_11_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    if points == 19:
                        asteroid_12_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    if points == 29:
                        asteroid_13_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    if points == 39:
                        asteroid_14_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    if points == 49:
                        asteroid_15_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    if points == 59:
                        asteroid_16_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    if points == 69:
                        asteroid_17_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    if points == 79:
                        asteroid_18_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    if points == 89:
                        asteroid_19_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                    if points == 99:
                        asteroid_20_pos = [random.randrange(640, x_distance), random.randrange(0, 481)]
                
                        
    #When Level passes, speed changes again
                    asteroid_1_move = random.randint(3, x_speed)
                    asteroid_2_move = random.randint(3, x_speed)
                    asteroid_3_move = random.randint(3, x_speed)
                    asteroid_4_move = random.randint(3, x_speed)
                    asteroid_5_move = random.randint(3, x_speed)
                    asteroid_6_move= random.randint(3, x_speed)
                    asteroid_7_move = random.randint(3, x_speed)
                    asteroid_8_move = random.randint(3, x_speed)
                    asteroid_9_move = random.randint(3, x_speed)
                    asteroid_10_move = random.randint(3, x_speed)
                    asteroid_11_move = random.randint(3, x_speed)
                    asteroid_12_move = random.randint(3, x_speed)
                    asteroid_13_move = random.randint(3, x_speed)
                    asteroid_14_move = random.randint(3, x_speed)
                    asteroid_15_move = random.randint(3, x_speed)
                    asteroid_16_move = random.randint(3, x_speed)
                    asteroid_17_move = random.randint(3, x_speed)
                    asteroid_18_move = random.randint(3, x_speed)
                    asteroid_19_move = random.randint(3, x_speed)
                    asteroid_20_move = random.randint(3, x_speed)
                        
    #Astronaut
                pygame.draw.ellipse(screen, ASTRONAUT, (astro_x - 5, astro_y - 10, 35, 23)) #Head
                pygame.draw.ellipse(screen, ASTRONAUT, (astro_x, astro_y, 25, 30)) #Body
                pygame.draw.ellipse(screen, ASTRONAUT, (astro_x + 13, astro_y + 10, 10, 30)) #Right Leg
                pygame.draw.ellipse(screen, ASTRONAUT, (astro_x + 2, astro_y + 10, 10, 30)) #Right Leg
                pygame.draw.ellipse(screen, ASTRONAUT, (astro_x - 8, astro_y + 8, 40, 12)) #Arms
                pygame.draw.ellipse(screen, GREY, (astro_x, astro_y - 5, 25, 13)) #Helmet
                pygame.draw.rect(screen, GREY, (astro_x + 5, astro_y + 15, 15, 10), 1)
        
    #Life Text
                some_text = some_font.render(f'Lives: {lives}', True, (255, 0, 0))
                screen.blit(some_text, (10, 10))
    #Points Text
                some_text2 = some_font.render(f'Points: {points}', True, (255, 215, 0))
                screen.blit(some_text2, (370, 10))
            
    #Life Mechanic
                if asteroid_1.collidepoint((astro_x, astro_y)) or asteroid_2.collidepoint((astro_x, astro_y)) or asteroid_3.collidepoint((astro_x, astro_y)) or asteroid_4.collidepoint((astro_x, astro_y)) or asteroid_5.collidepoint((astro_x, astro_y)) or asteroid_6.collidepoint((astro_x, astro_y)) or asteroid_7.collidepoint((astro_x, astro_y)) or asteroid_8.collidepoint((astro_x, astro_y)) or asteroid_9.collidepoint((astro_x, astro_y)) or asteroid_10.collidepoint((astro_x, astro_y)) or asteroid_11.collidepoint((astro_x, astro_y)) or asteroid_12.collidepoint((astro_x, astro_y)) or asteroid_13.collidepoint((astro_x, astro_y)) or asteroid_14.collidepoint((astro_x, astro_y)) or asteroid_15.collidepoint((astro_x, astro_y)) or asteroid_16.collidepoint((astro_x, astro_y)) or asteroid_17.collidepoint((astro_x, astro_y)) or asteroid_18.collidepoint((astro_x, astro_y)) or asteroid_19.collidepoint((astro_x, astro_y)) or asteroid_20.collidepoint((astro_x, astro_y)): 
                    if life == True:
                        lives -= 1
                        life = False
                else: 
                    life = True
        #Lose Screen
        elif lives == 0:
            screen.fill(SPACE)
            for item in star_list:
                item[0] += 1
                item[1] += 1
                pygame.draw.circle(screen, WHITE, item, 3)
                if item[0] > 640 or item[1] > 480:
                    item[0] = random.randrange(-480, 320)
                    item[1] = random.randrange(-300, 0)
            some_font = pygame.font.SysFont('Arial', 100)
            lose_screen = some_font.render("YOU LOSE", True, (RED))
            some_font = pygame.font.SysFont('Arial', 60)
            point_txt = some_font.render(f"Score: {points}", True, (GOLD))
            some_font = pygame.font.SysFont('Arial', 15)
            credits = some_font.render("*Background Credits to Rishab!", True, WHITE)
            screen.blit(lose_screen, (lose_screen.get_rect(center = screen.get_rect().center)[0], lose_screen.get_rect(center = screen.get_rect().center)[1]-70))
            screen.blit(point_txt, (point_txt.get_rect(center = screen.get_rect().center)[0], point_txt.get_rect(center = screen.get_rect().center)[1]))
            screen.blit(credits, (credits.get_rect(center = screen.get_rect().center)[0], credits.get_rect(center = screen.get_rect().center)[1]+200))
    #Menu Buttons
            menu_button = pygame.Rect([10, 300, 300, 80])
            pygame.draw.rect(screen, BLACK, menu_button)
            some_font = pygame.font.SysFont('Arial', 60)
            menu_title = some_font.render("MENU", True, WHITE)
            menu_rect = menu_title.get_rect
            screen.blit(menu_title, (100, menu_rect(center = screen.get_rect().center)[1]+100))
            if menu_button.collidepoint((astro_x, astro_y)):
                if click:
                    main_menu()
            restart_button = pygame.Rect([330, 300, 300, 80])
            pygame.draw.rect(screen, BLACK, restart_button)
            some_font = pygame.font.SysFont('Arial', 60)
            restart_title = some_font.render("RESTART", True, WHITE)
            restart_rect = restart_title.get_rect
            screen.blit(restart_title, (345, restart_rect(center = screen.get_rect().center)[1]+100))
            if restart_button.collidepoint((astro_x, astro_y)):
                if click:
                    game_num1()

    #Win Screen
        elif points == 100:
            screen.fill(SPACE)
            global game_complete1
            if game_complete1 == False:
                global games_complete
                games_complete += 1
                game_complete1 = True

    #Background
            for item in star_list:
                item[0] += 1
                item[1] += 1
                pygame.draw.circle(screen, WHITE, item, 3)
                if item[0] > 640 or item[1] > 480:
                    item[0] = random.randrange(-480, 320)
                    item[1] = random.randrange(-300, 0)
    #Win Text
            some_font = pygame.font.SysFont('Arial', 100)
            win_screen = some_font.render("YOU WIN!", (GREEN), True)
            some_font = pygame.font.SysFont('Arial', 60)
            point_txt = some_font.render(f"Score: {points}", True, (GOLD))
            some_font = pygame.font.SysFont('Arial', 15)
            credits = some_font.render("*Background Credits to Rishab!", True, WHITE)
#Buttons
            menu_button = pygame.Rect([10, 300, 300, 80])
            pygame.draw.rect(screen, BLACK, menu_button)
            some_font = pygame.font.SysFont('Arial', 60)
            menu_title = some_font.render("MENU", True, WHITE)
            menu_rect = menu_title.get_rect
            screen.blit(win_screen, (win_screen.get_rect(center = screen.get_rect().center)[0], win_screen.get_rect(center = screen.get_rect().center)[1]-70))
            screen.blit(point_txt, (point_txt.get_rect(center = screen.get_rect().center)[0], point_txt.get_rect(center = screen.get_rect().center)[1]))
            screen.blit(menu_title, (100, menu_rect(center = screen.get_rect().center)[1]+100))
            screen.blit(credits, (credits.get_rect(center = screen.get_rect().center)[0], credits.get_rect(center = screen.get_rect().center)[1]+200))
            if menu_button.collidepoint((astro_x, astro_y)):
                if click:
                    main_menu()
            restart_button = pygame.Rect([330, 300, 300, 80])
            pygame.draw.rect(screen, BLACK, restart_button)
            some_font = pygame.font.SysFont('Arial', 60)
            restart_title = some_font.render("RESTART", True, WHITE)
            restart_rect = restart_title.get_rect
            screen.blit(restart_title, (355, restart_rect(center = screen.get_rect().center)[1]+100))
            if restart_button.collidepoint((astro_x, astro_y)):
                if click:
                    game_num1()

            
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.flip()
        clock.tick(60)




  #Asteroid
  # pygame.draw.circle(SCREEN, BROWN)

#RUSTIN IS RUSTIN'
def game_num2():
    # pygame template
    font = pygame.font.Font("freesansbold.ttf", 30)

# ---------------------------
    # Initialize global variables
    lives = 3
    completed_tasks = 0
    timer_width = 0
    check_button1_colour = WHITE
    check_button2_colour = WHITE
    check_button3_colour = WHITE
    check_button4_colour = WHITE
    check_button1 = pygame.draw.rect(screen, GREY, (68, 73, 30, 30), border_radius = 10)
    check_button2 = pygame.draw.rect(screen, GREY, (322, 73, 30, 30), border_radius = 10)

    lives_colour1 = WHITE
    lives_colour2 = WHITE
    lives_colour3 = WHITE

    flash_list = [RED, GREEN, BLUE, YELLOW]
    random.shuffle(flash_list)
    flash_list.append(WHITE) 
    flash_list_place = 0
    flash_list_time = 1
    flash_list_input = []
    red_button = pygame.draw.rect(screen, RED, (200, 115, 40, 40))
    green_button = pygame.draw.rect(screen, RED, (200, 155, 40, 40))
    blue_button = pygame.draw.rect(screen, RED, (240, 115, 40, 40))
    yellow_button = pygame.draw.rect(screen, RED, (240, 155, 40, 40))

    numbers_input = []
    numbers_list = [1, 2, 3, 4]
    random.shuffle(numbers_list)
    numbers_text = font.render(f"{numbers_list}", True, ORANGE)
    numbers_button_1 = font.render("1", True, WHITE)
    numbers_button_2 = font.render("2", True, WHITE)
    numbers_button_3 = font.render("3", True, WHITE)
    numbers_button_4 = font.render("4", True, WHITE)
    button_1 = pygame.draw.rect(screen, ORANGE, (365, 145, 70, 30))
    button_2 = pygame.draw.rect(screen, ORANGE, (445, 145, 70, 30))
    button_3 = pygame.draw.rect(screen, ORANGE, (365, 185, 70, 30))
    button_4 = pygame.draw.rect(screen, ORANGE, (445, 185, 70, 30))

    click = False
    rline = False
    gline = False
    bline = False
    rconnect = False
    gconnect = False
    bconnect = False
    connect = True

    line_pick = [300, 335, 370]
    line_hook = [300, 335, 370]
    line_pick_input = []
    line_hook_input = []
    random.shuffle(line_pick)
    random.shuffle(line_hook)
    line_red_y = line_pick[0]
    line_green_y = line_pick[1] 
    line_blue_y = line_pick[2]
    line_red_x = 69
    line_green_x = 69
    line_blue_x = 69
    line_red_clicked = False
    line_green_clicked = False
    line_blue_clicked = False

    wire_y = [275, 305, 335, 365]
    random.shuffle(wire_y)
    red_wire = pygame.draw.line(screen, RED, (322, wire_y[0]), (564, wire_y[0]), 10)
    green_wire = pygame.draw.line(screen, GREEN, (322, wire_y[1]), (564, wire_y[1]), 10)
    blue_wire = pygame.draw.line(screen, BLUE, (322, wire_y[2]), (564, wire_y[2]), 10)
    yellow_wire = pygame.draw.line(screen, YELLOW, (322, wire_y[3]), (564, wire_y[3]), 10)
    wire_colour1 = RED
    wire_colour2 = GREEN
    wire_colour3 = BLUE
    wire_colour4 = YELLOW

    font = pygame.font.Font("freesansbold.ttf", 20)
    start_text = ["Memory Game Rules:", 
    "1. Press the buttons in the coresponding order of the lights",
    "2. if the first number is:",
    "    1. type in the numbers in the order they appear in",
    '    2. type in "1 2 3 4"',
    '    3. type in "4 3 2 1"',    
    "    4. type in the numbers in the opposite order they appear in",
    "3. Connect the wire to the hook with the corresponding colour",
    "4. if the first wire is:",
    "    Red. Cut Green",
    "    Green. Cut Yellow",
    "    Blue. Cut Blue",
    "    Yellow. Cut Red"]
    start_game = pygame.draw.rect(screen, GREEN, (400, 300, 150, 100))
    start = True
    end = False
    button_font = pygame.font.Font("freesansbold.ttf", 30)

    # ---------------------------

    while True:
        screen.fill(GREY)  # always the first drawing command
        mx, my = pygame.mouse.get_pos()
        
        if start == True:
            screen.blit(font.render(start_text[0], True, WHITE), (10, 100))
            screen.blit(font.render(start_text[1], True, WHITE), (10, 120))
            screen.blit(font.render(start_text[2], True, WHITE), (10, 140))
            screen.blit(font.render(start_text[3], True, WHITE), (10, 160))
            screen.blit(font.render(start_text[4], True, WHITE), (10, 180))
            screen.blit(font.render(start_text[5], True, WHITE), (10, 200))
            screen.blit(font.render(start_text[6], True, WHITE), (10, 220))
            screen.blit(font.render(start_text[7], True, WHITE), (10, 240))
            screen.blit(font.render(start_text[8], True, WHITE), (10, 260))
            screen.blit(font.render(start_text[9], True, WHITE), (10, 280))
            screen.blit(font.render(start_text[10], True, WHITE), (10, 300))
            screen.blit(font.render(start_text[11], True, WHITE), (10, 320))
            screen.blit(font.render(start_text[12], True, WHITE), (10, 340))
            pygame.draw.rect(screen, GREEN, (400, 300, 150, 100))
            screen.blit(font.render("START", True, WHITE), (440, 340))
            if start_game.collidepoint((mx, my)):
                if click:
                    start = False
        else:
            if timer_width >= 492 or lives == 0:
                screen.fill(BLACK)
                font = pygame.font.Font("freesansbold.ttf", 100)
                button_font = pygame.font.Font("freesansbold.ttf", 30)
                screen.blit(font.render("YOU LOSE", True, RED), (60, 200))
                end = True
                menu_button = pygame.Rect([10, 300, 300, 80])
                pygame.draw.rect(screen, RED, menu_button)
                menu_title = button_font.render("BACK TO MENU", True, WHITE)
                menu_rect = menu_title.get_rect
                screen.blit(menu_title, (40, menu_rect(center = screen.get_rect().center)[1]+100))
                if menu_button.collidepoint((mx, my)):
                    if click:
                        main_menu()
                restart_button = pygame.Rect([330, 300, 300, 80])
                pygame.draw.rect(screen, RED, restart_button)
                restart_title = button_font.render("RESTART GAME", True, WHITE)
                restart_rect = restart_title.get_rect
                screen.blit(restart_title, (355, restart_rect(center = screen.get_rect().center)[1]+100))
                if restart_button.collidepoint((mx, my)):
                    if click:
                        game_num2()
            elif completed_tasks == 4:
                end_screen_y = 0
                win_screen_y = 0
                screen.fill(BLACK)
                font = pygame.font.Font("freesansbold.ttf", 100)
                screen.blit(font.render("YOU WIN!", True, GREEN) , (80, 200))
                end = True
                global game_complete2
                if game_complete2 == False:
                    global games_complete
                    games_complete += 1
                    game_complete2 = True
                menu_button = pygame.Rect([10, 300, 300, 80])
                pygame.draw.rect(screen, RED, menu_button)
                menu_title = button_font.render("BACK TO MENU", True, WHITE)
                menu_rect = menu_title.get_rect
                screen.blit(menu_title, (40, menu_rect(center = screen.get_rect().center)[1]+100))
                if menu_button.collidepoint((mx, my)):
                    if click:
                        main_menu()
                restart_button = pygame.Rect([330, 300, 300, 80])
                pygame.draw.rect(screen, RED, restart_button)
                restart_title = button_font.render("RESTART GAME", True, WHITE)
                restart_rect = restart_title.get_rect
                screen.blit(restart_title, (355, restart_rect(center = screen.get_rect().center)[1]+100))
                if restart_button.collidepoint((mx, my)):
                    if click:
                        game_num2()
            else:
                timer_width += 0.2
                pygame.draw.rect(screen, LIGHT_GREY, (40, 25, 550, 430))   
                pygame.draw.rect(screen, DARK_GREY, (55, 60, 522, 350), border_radius = 20)   
                pygame.draw.rect(screen, GREY, (68, 73, 242, 155), border_radius = 10)   
                pygame.draw.rect(screen, GREY, (322, 73, 242, 155), border_radius = 10)
                pygame.draw.rect(screen, GREY, (68, 242, 242, 155), border_radius = 10)   
                pygame.draw.rect(screen, GREY, (322, 242, 242, 155), border_radius = 10)
                
                pygame.draw.rect(screen, check_button1_colour, (68, 73, 30,30), border_radius = 10)
                pygame.draw.rect(screen, check_button2_colour, (322, 73, 30,30), border_radius = 10)
                pygame.draw.rect(screen, check_button3_colour, (322, 242, 30,30), border_radius = 10)
                pygame.draw.rect(screen, check_button4_colour, (68, 242, 30,30), border_radius = 10)
                
                pygame.draw.rect(screen, lives_colour1, (255, 420, 20, 20))
                pygame.draw.rect(screen, lives_colour2, (305, 420, 20, 20))
                pygame.draw.rect(screen, lives_colour3, (355, 420, 20, 20))
                
                pygame.draw.rect(screen, RED, (200, 115, 40, 40))
                pygame.draw.rect(screen, GREEN, (200, 155, 40, 40))
                pygame.draw.rect(screen, BLUE, (240, 115, 40, 40))
                pygame.draw.rect(screen, YELLOW, (240, 155, 40, 40))    
                
                pygame.draw.rect(screen, LIGHT_GREY, (90, 115, 50, 80)) 
                pygame.draw.rect(screen, flash_list[flash_list_place], (102.5, 135, 25, 40))
            
                if flash_list_time == 15:
                    flash_list_place += 1
                    flash_list_time = 0
                    if flash_list_place > 4:
                        flash_list_place = 0
                else:
                    flash_list_time += 1
            
                pygame.draw.rect(screen, BLACK, (365, 90, 150, 45), border_radius = 5)
                pygame.draw.rect(screen, ORANGE, (365, 145, 70, 30), border_radius = 5)
                pygame.draw.rect(screen, ORANGE, (365, 185, 70, 30), border_radius = 5)
                pygame.draw.rect(screen, ORANGE, (445, 145, 70, 30), border_radius = 5)
                pygame.draw.rect(screen, ORANGE, (445, 185, 70, 30), border_radius = 5)
                screen.blit(numbers_text, (370, 100))
                screen.blit(numbers_button_1, (390, 146))
                screen.blit(numbers_button_2, (470, 146))
                screen.blit(numbers_button_3, (390, 186))
                screen.blit(numbers_button_4, (470, 186))
            
                
                pygame.draw.line(screen, RED, (322, wire_y[0]), (563, wire_y[0]), 10)
                pygame.draw.line(screen, wire_colour1, (440, wire_y[0]), (446, wire_y[0]), 10)
                pygame.draw.line(screen, GREEN, (322, wire_y[1]), (563, wire_y[1]), 10)
                pygame.draw.line(screen, wire_colour2, (440, wire_y[1]), (446, wire_y[1]), 10)
                pygame.draw.line(screen, BLUE, (322, wire_y[2]), (563, wire_y[2]), 10)
                pygame.draw.line(screen, wire_colour3, (440, wire_y[2]), (446, wire_y[2]), 10)
                pygame.draw.line(screen, YELLOW, (322, wire_y[3]), (563, wire_y[3]), 10)
                pygame.draw.line(screen, wire_colour4, (440, wire_y[3]), (446, wire_y[3]), 10)
            
                pygame.draw.rect(screen, RED, (68, 40, 492, 10)) 
                pygame.draw.rect(screen, GREEN, (68, 40, timer_width, 10)) 
            
                if red_button.collidepoint((mx, my)):
                    if click:
                        flash_list_input.append(RED)
                elif green_button.collidepoint((mx, my)):
                    if click:
                        flash_list_input.append(GREEN)
                elif blue_button.collidepoint((mx, my)):
                    if click:   
                        flash_list_input.append(BLUE)
                elif yellow_button.collidepoint((mx, my)):
                    if click:
                        flash_list_input.append(YELLOW)            
                elif check_button1.collidepoint((mx, my)):
                    if click:
                        flash_list_input.append(WHITE)
                        if flash_list_input == flash_list:
                            completed_tasks += 1
                            check_button1_colour = GREEN       
                        else:
                            lives -= 1
                            flash_list_input = []
                
                if button_1.collidepoint((mx, my)):
                    if click:
                        numbers_input.append(1)
                elif button_2.collidepoint((mx, my)):
                    if click:
                        numbers_input.append(2)
                elif button_3.collidepoint((mx, my)):
                    if click:
                        numbers_input.append(3)
                elif button_4.collidepoint((mx, my)):
                    if click:
                        numbers_input.append(4)
                elif check_button2.collidepoint((mx, my)):
                    if click:
                        if numbers_list[0] == 1 and numbers_input == numbers_list:
                            completed_tasks += 1
                            check_button2_colour = GREEN
                        elif numbers_list[0] == 2 and numbers_input == [1, 2, 3, 4]:
                            completed_tasks += 1
                            check_button2_colour = GREEN
                        elif numbers_list[0] == 3 and numbers_input == [4, 3, 2, 1]:
                            completed_tasks += 1
                            check_button2_colour = GREEN
                        elif numbers_list[0] == 4 and numbers_input == [numbers_list[3], numbers_list[2], numbers_list[1], numbers_list[0]]:
                            completed_tasks += 1
                            check_button2_colour = GREEN
                        else:
                            lives -= 1
                            numbers_input = []
                            random.shuffle(numbers_list)
                            font = pygame.font.Font("freesansbold.ttf", 30)
                            numbers_text = font.render(f"{numbers_list}", True, ORANGE)
                
                red_start = pygame.Rect([68, line_pick[0], 10, 10])
                pygame.draw.rect(screen, RED, red_start)
                green_start = pygame.Rect([68, line_pick[1], 10, 10])
                pygame.draw.rect(screen, GREEN, green_start)
                blue_start = pygame.Rect([68, line_pick[2], 10, 10])
                pygame.draw.rect(screen, BLUE, blue_start)
                red_end = pygame.Rect([300, line_hook[0], 10, 10])
                pygame.draw.rect(screen, RED, red_end)
                green_end = pygame.Rect([300, line_hook[1], 10, 10])
                pygame.draw.rect(screen, GREEN, green_end)
                blue_end = pygame.Rect([300, line_hook[2], 10, 10])
                pygame.draw.rect(screen, BLUE, blue_end)
            
                if red_start.collidepoint((mx, my)):
                    if click:
                        rline = True
                if green_start.collidepoint((mx, my)):
                    if click:
                        gline = True
                if blue_start.collidepoint((mx, my)):
                    if click:
                        bline = True
                
                if rline:
                    pygame.draw.line(screen, (255, 0, 0), [red_start[0], red_start[1]+4], [mx, my], 10)
                    if red_end.collidepoint((mx, my)):
                        if click:
                            rconnect = True
                    elif green_end.collidepoint((mx, my)) or blue_end.collidepoint((mx, my)):
                        if click:
                            rline = False
                            lives -= 1
                if rconnect:
                    pygame.draw.line(screen, (255, 0, 0), [red_start[0], red_start[1]+4], [red_end[0], red_end[1]+4], 10)
                    rline = False
                if gline:
                    pygame.draw.line(screen, (0, 255, 0), [green_start[0], green_start[1]+4], [mx, my], 10)
                    if green_end.collidepoint((mx, my)):
                        if click:
                            gconnect = True
                    elif red_end.collidepoint((mx, my)) or blue_end.collidepoint((mx, my)):
                        if click:
                            gline = False
                            lives -= 1
                if gconnect:
                    pygame.draw.line(screen, (0, 255, 0), [green_start[0], green_start[1]+4], [green_end[0], green_end[1]+4], 10)
                    gline = False
                if bline:
                    pygame.draw.line(screen, (0, 0, 255), [blue_start[0], blue_start[1]+4], [mx, my], 10)
                    if blue_end.collidepoint((mx, my)):
                        if click:
                            bconnect = True
                    elif green_end.collidepoint((mx, my)) or red_end.collidepoint((mx, my)):
                        if click:
                            bline = False
                            lives -= 1
                if bconnect:
                    pygame.draw.line(screen, (0, 0, 255), [blue_start[0], blue_start[1]+4], [blue_end[0], blue_end[1]+4], 10)
                    bline = False
                if rconnect and gconnect and bconnect and connect:
                    completed_tasks += 1
                    connect = False
                    check_button4_colour = GREEN
                    
                if red_wire.collidepoint((mx, my)):
                    if click:
                        wire_colour1 = GREY
                        if wire_y[3] == 275:
                            check_button3_colour = GREEN
                            completed_tasks += 1
                        else:
                            lives = 0
                elif green_wire.collidepoint((mx, my)):
                    if click:
                        wire_colour2 = GREY
                        if wire_y[0] == 275:
                            check_button3_colour = GREEN
                            completed_tasks += 1
                        else:
                            lives = 0
                elif blue_wire.collidepoint((mx, my)):
                    if click:
                        wire_colour3 = GREY
                        if wire_y[2] == 275:
                            check_button3_colour = GREEN
                            completed_tasks += 1
                        else:
                            lives = 0
                elif yellow_wire.collidepoint((mx, my)):
                    if click:
                        wire_colour4 = GREY
                        if wire_y[1] == 275:
                            check_button3_colour = GREEN
                            completed_tasks += 1
                        else:
                            lives = 0
                if lives == 1:
                    lives_colour2 = RED
                elif lives == 2:
                    lives_colour1 = RED
            # GAME STATE UPDATES
            # All game math and comparisons happen here
        
            # DRAWING
        
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True 
        

        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(30)

#LANCE AND SHIELD
def game_num3():
    some_font = pygame.font.SysFont(None, 50)
    timer_width = 1
    circle_1x = random.randrange(15,630) #CIRCLE 1 X POSITION
    circle_1y = random.randrange(15,470) #CIRCLE 1 Y POSITION

    circle_2x = random.randrange(15,630) #CIRCLE 2 X POSITION
    circle_2y = random.randrange(15,470) #CIRCLE 2 Y POSITION
    radius1 = 30
    radius2 = 30
    # ---------------------------
    points = 0 # COUNTER
    click = False # 
    intro = True
    running = True
    while running:
        # EVENT HANDLING

        # GAME STATE UPDATES
        # All game math and comparisons happen here
        mx, my = pygame.mouse.get_pos()

        screen.fill((BLACK))

        if intro:
                description = some_font.render("CLICK THE CIRCLES!", True, (WHITE))
                instructions = some_font.render("Click the hidden and visible circles!", True, WHITE)
                screen.blit(description, (description.get_rect(center = screen.get_rect().center)[0], description.get_rect(center = screen.get_rect().center)[1]-65))
                screen.blit(instructions, (instructions.get_rect(center = screen.get_rect().center)[0], instructions.get_rect(center = screen.get_rect().center)[1]+75))
                start_button = pygame.Rect([220, 200, 200, 80])
                pygame.draw.rect(screen, (ORANGE), start_button)
                start_title = some_font.render("START", True, WHITE)
                screen.blit(start_title, (start_title.get_rect(center = screen.get_rect().center)[0], start_title.get_rect(center = screen.get_rect().center)[1]))
                if start_button.collidepoint((mx, my)):
                    if click:
                        intro = False
        # DRAWING
        else:
            if points <= 20:
                screen.fill((0, 0, 255))  
            else:
                screen.fill((255, 0, 0))
            
            #Points System
        
            circle_1 = pygame.draw.circle(screen, (0, 0, 230), (circle_1x, circle_1y), radius1)
            circle_2 = pygame.draw.circle(screen, (230, 0, 0), (circle_2x, circle_2y), radius2)
            
            if circle_1.collidepoint((mx, my)): #if mouse collides with circle coordinates
                if click == True:
                    if points <= 20:
                        points += 2
                    else:
                        points += 1
                    circle_1x = random.randrange(50,630)
                    circle_1y = random.randrange(50,470)
                    circle_2x = random.randrange(50,630)
                    circle_2y = random.randrange(50,470)
                    if radius1 >= 8:
                        radius1 -= 2
                    if radius2 >= 8:
                        radius2 -= 2
            if circle_2.collidepoint((mx, my)):
                if click == True:
                    if points <= 20:
                        points += 1
                    else:
                        points += 2
                    circle_1x = random.randrange(15,630)
                    circle_1y = random.randrange(15,470)
                    circle_2x = random.randrange(15,630)
                    circle_2y = random.randrange(15,470)
                    if radius1 >= 8:
                        radius1 -= 2
                    if radius2 >= 8:
                        radius2 -= 2
        
            if points >= 40:
                global game_complete3
                if game_complete3 == False:
                    global games_complete
                    games_complete += 1
                    game_complete3 = True
                screen.fill((255, 165, 0))
                win_text = some_font.render(f"GAME OVER! You win! Score: {points} / 40", True, (0, 0, 0))
                screen.blit(win_text, (win_text.get_rect(center = screen.get_rect().center)[0], win_text.get_rect(center = screen.get_rect().center)[1]))
                menu_button = pygame.Rect([10, 300, 300, 80])
                pygame.draw.rect(screen, BLACK, menu_button)
                menu_title = some_font.render("MENU", True, WHITE)
                menu_rect = menu_title.get_rect
                screen.blit(menu_title, (120, menu_rect(center = screen.get_rect().center)[1]+100))
                if menu_button.collidepoint((mx, my)):
                    if click:
                        main_menu()
                restart_button = pygame.Rect([330, 300, 300, 80])
                pygame.draw.rect(screen, BLACK, restart_button)
                restart_title = some_font.render("RESTART GAME", True, WHITE)
                restart_rect = restart_title.get_rect
                screen.blit(restart_title, (345, restart_rect(center = screen.get_rect().center)[1]+100))
                if restart_button.collidepoint((mx, my)):
                    if click:
                        game_num3()
            
            pygame.draw.rect(screen, (0, 255, 0), (260, 10, 360, 10))
            pygame.draw.rect(screen, (0, 0, 0), (260, 10, timer_width, 10))
            if timer_width >= 360:
                screen.fill((255, 165, 0))
                lose_text = some_font.render(f"GAME OVER! You Lost. Score: {points} / 40", True, (0, 0, 0))
                screen.blit(lose_text, (lose_text.get_rect(center = screen.get_rect().center)[0], lose_text.get_rect(center = screen.get_rect().center)[1]))
                menu_button = pygame.Rect([10, 300, 300, 80])
                pygame.draw.rect(screen, BLACK, menu_button)
                menu_title = some_font.render("MENU", True, WHITE)
                menu_rect = menu_title.get_rect
                screen.blit(menu_title, (120, menu_rect(center = screen.get_rect().center)[1]+100))
                if menu_button.collidepoint((mx, my)):
                    if click:
                        main_menu()
                restart_button = pygame.Rect([330, 300, 300, 80])
                pygame.draw.rect(screen, BLACK, restart_button)
                restart_title = some_font.render("RESTART GAME", True, WHITE)
                restart_rect = restart_title.get_rect
                screen.blit(restart_title, (345, restart_rect(center = screen.get_rect().center)[1]+100))
                if restart_button.collidepoint((mx, my)):
                    if click:
                        game_num3()
            else:
                if points < 40:
                    timer_width += 0.35
                
            points_text = some_font.render(f"Points: {points} / 40", True, (0, 0, 0))
            points_rect = points_text.get_rect()
            points_rect.left = 10
            screen.blit(points_text, points_rect)
        # Must be the last two lines
        # of the game loop
        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.flip()
        clock.tick(30)

#REESHAB
def game_num4():
#ASTEROID POSITION
    ast1_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
    ast2_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
    ast3_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
    ast4_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
    ast5_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
    ast6_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
    ast7_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
    ast8_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
    ast9_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
    ast10_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
#ASTEROID MOVESPEEDS
    move_limit = 1
    ast1_move = random.randint(1, move_limit)
    ast2_move = random.randint(1, move_limit)
    ast3_move = random.randint(1, move_limit)
    ast4_move = random.randint(1, move_limit)
    ast5_move = random.randint(1, move_limit)
    ast6_move = random.randint(1, move_limit)
    ast7_move = random.randint(1, move_limit)
    ast8_move = random.randint(1, move_limit)
    ast9_move = random.randint(1, move_limit)
    ast10_move = random.randint(1, move_limit)
#ASTEROID DESTROY VARIABLES
    ast1_destroy = False
    ast2_destroy = False
    ast3_destroy = False
    ast4_destroy = False
    ast5_destroy = False
    ast6_destroy = False
    ast7_destroy = False
    ast8_destroy = False
    ast9_destroy = False
    ast10_destroy = False

    scores_font = pygame.font.SysFont("stencil", 25)
    font = pygame.font.SysFont(None, 30)
    round = 0
    points = 0
    click = False
    intro = True
    running = True
    while running:
#MOUSE POSITION
        mx, my = pygame.mouse.get_pos()
#BACKGROUND
        screen.fill(SEA_GREEN)

        if intro:
            description = scores_font.render("SHOOT 50 ASTEROIDS DOWN!", True, WHITE)
            instructions = scores_font.render("Drag your mouse to aim and click to shoot!", True, WHITE)
            screen.blit(description, (description.get_rect(center = screen.get_rect().center)[0], description.get_rect(center = screen.get_rect().center)[1]-65))
            screen.blit(instructions, (instructions.get_rect(center = screen.get_rect().center)[0], instructions.get_rect(center = screen.get_rect().center)[1]+75))
            start_button = pygame.Rect([220, 200, 200, 80])
            pygame.draw.rect(screen, EVERGLADE_GREEN, [220+5, 200+5, 200, 80])
            pygame.draw.rect(screen, PEA_GREEN, start_button)
            pygame.draw.rect(screen, EVERGLADE_GREEN, start_button, 1)
            start_title = font.render("START GAME", True, WHITE)
            screen.blit(start_title, (start_title.get_rect(center = screen.get_rect().center)[0], start_title.get_rect(center = screen.get_rect().center)[1]))
            if start_button.collidepoint((mx, my)):
                if click:
                    intro = False


#BORDER DRAWING
        else:
            pygame.draw.rect(screen, (36, 76, 58), [5, 5, 630, 470], 3)
            pygame.draw.rect(screen, (36, 76, 58), [10, 10, 620, 460], 2)
            pygame.draw.rect(screen, (36, 76, 58), [15, 15, 610, 450], 1)

    #SCORE AND ROUND NUMBER TEXT
            number = scores_font.render(f"Destroyed: {points}", True, WHITE)
            number_rect = number.get_rect()
            number_rect.left = 5
            screen.blit(number, number_rect)
            round_text = scores_font.render(f"Round: {round + 1}", True, WHITE)
            round_rect = round_text.get_rect()
            round_rect.right = 635
            screen.blit(round_text, round_rect)

    #ASTEROIDS AND THEIR MOVEMENT
            if ast1_destroy == False:
                ast1_pos[0] += ast1_move
                ast1 = pygame.draw.circle(screen, EVERGLADE_GREEN, (ast1_pos[0]+15, ast1_pos[1]+15), 15)
            if ast2_destroy == False:
                ast2_pos[0] += ast2_move
                ast2 = pygame.draw.circle(screen, EVERGLADE_GREEN, (ast2_pos[0]+15, ast2_pos[1]+15), 15)
            if ast3_destroy == False:
                ast3_pos[0] += ast3_move
                ast3 = pygame.draw.circle(screen, EVERGLADE_GREEN, (ast3_pos[0]+15, ast3_pos[1]+15), 15)
            if ast4_destroy == False:
                ast4_pos[0] += ast4_move
                ast4 = pygame.draw.circle(screen, EVERGLADE_GREEN, (ast4_pos[0]+15, ast4_pos[1]+15), 15)
            if ast5_destroy == False:
                ast5_pos[0] += ast5_move
                ast5 = pygame.draw.circle(screen, EVERGLADE_GREEN, (ast5_pos[0]+15, ast5_pos[1]+15), 15)
            if ast6_destroy == False:
                ast6_pos[0] += ast6_move
                ast6 = pygame.draw.circle(screen, EVERGLADE_GREEN, (ast6_pos[0]+15, ast6_pos[1]+15), 15)
            if ast7_destroy == False:
                ast7_pos[0] += ast7_move
                ast7 = pygame.draw.circle(screen, EVERGLADE_GREEN, (ast7_pos[0]+15, ast7_pos[1]+15), 15)
            if ast8_destroy == False:
                ast8_pos[0] += ast8_move
                ast8 = pygame.draw.circle(screen, EVERGLADE_GREEN, (ast8_pos[0]+15, ast8_pos[1]+15), 15)
            if ast9_destroy == False:
                ast9_pos[0] += ast9_move
                ast9 = pygame.draw.circle(screen, EVERGLADE_GREEN, (ast9_pos[0]+15, ast9_pos[1]+15), 15)
            if ast10_destroy == False:
                ast10_pos[0] += ast10_move
                ast10 = pygame.draw.circle(screen, EVERGLADE_GREEN, (ast10_pos[0]+15, ast10_pos[1]+15), 15)
    #ASTEROID CLICKING/SHOOTING
            if ast1.collidepoint((mx, my)):
                if click:
                    ast1_destroy = True
                    ast1 = pygame.Rect([-100, -100, 1, 1])
                    points += 1
            if ast2.collidepoint((mx, my)):
                if click:
                    ast2_destroy = True
                    ast2 = pygame.Rect([-100, -100, 1, 1])
                    points += 1
            if ast3.collidepoint((mx, my)):
                if click:
                    ast3_destroy = True
                    ast3 = pygame.Rect([-100, -100, 1, 1])
                    points += 1
            if ast4.collidepoint((mx, my)):
                if click:
                    ast4_destroy = True
                    ast4 = pygame.Rect([-100, -100, 1, 1])
                    points += 1
            if ast5.collidepoint((mx, my)):
                if click:
                    ast5_destroy = True
                    ast5 = pygame.Rect([-100, -100, 1, 1])
                    points += 1
            if ast6.collidepoint((mx, my)):
                if click:
                    ast6_destroy = True
                    ast6 = pygame.Rect([-100, -100, 1, 1])
                    points += 1
            if ast7.collidepoint((mx, my)):
                if click:
                    ast7_destroy = True
                    ast7 = pygame.Rect([-100, -100, 1, 1])
                    points += 1
            if ast8.collidepoint((mx, my)):
                if click:
                    ast8_destroy = True
                    ast8 = pygame.Rect([-100, -100, 1, 1])
                    points += 1
            if ast9.collidepoint((mx, my)):
                if click:
                    ast9_destroy = True
                    ast9 = pygame.Rect([-100, -100, 1, 1])
                    points += 1
            if ast10.collidepoint((mx, my)):
                if click:
                    ast10_destroy = True
                    ast10 = pygame.Rect([-100, -100, 1, 1])
                    points += 1

    #ROUND RESETS
            if points == 10:
                if round == 0:
                    ast1_destroy = ast2_destroy = ast3_destroy = ast4_destroy = ast5_destroy = ast6_destroy = ast7_destroy = ast8_destroy = ast9_destroy = ast10_destroy = False
                    move_limit += 1
                    ast1_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast2_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast3_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast4_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast5_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast6_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast7_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast8_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast9_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast10_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast1_move = random.randint(1, move_limit)
                    ast2_move = random.randint(1, move_limit)
                    ast3_move = random.randint(1, move_limit)
                    ast4_move = random.randint(1, move_limit)
                    ast5_move = random.randint(1, move_limit)
                    ast6_move = random.randint(1, move_limit)
                    ast7_move = random.randint(1, move_limit)
                    ast8_move = random.randint(1, move_limit)
                    ast9_move = random.randint(1, move_limit)
                    ast10_move = random.randint(1, move_limit)
                    round += 1
            if points == 20:
                if round == 1:
                    ast1_destroy = ast2_destroy = ast3_destroy = ast4_destroy = ast5_destroy = ast6_destroy = ast7_destroy = ast8_destroy = ast9_destroy = ast10_destroy = False
                    move_limit += 1
                    ast1_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast2_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast3_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast4_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast5_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast6_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast7_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast8_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast9_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast10_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast1_move = random.randint(1, move_limit)
                    ast2_move = random.randint(1, move_limit)
                    ast3_move = random.randint(1, move_limit)
                    ast4_move = random.randint(1, move_limit)
                    ast5_move = random.randint(1, move_limit)
                    ast6_move = random.randint(1, move_limit)
                    ast7_move = random.randint(1, move_limit)
                    ast8_move = random.randint(1, move_limit)
                    ast9_move = random.randint(1, move_limit)
                    ast10_move = random.randint(1, move_limit)
                    round += 1
            if points == 30:
                if round == 2:
                    ast1_destroy = ast2_destroy = ast3_destroy = ast4_destroy = ast5_destroy = ast6_destroy = ast7_destroy = ast8_destroy = ast9_destroy = ast10_destroy = False
                    move_limit += 1
                    ast1_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast2_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast3_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast4_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast5_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast6_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast7_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast8_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast9_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast10_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast1_move = random.randint(1, move_limit)
                    ast2_move = random.randint(1, move_limit)
                    ast3_move = random.randint(1, move_limit)
                    ast4_move = random.randint(1, move_limit)
                    ast5_move = random.randint(1, move_limit)
                    ast6_move = random.randint(1, move_limit)
                    ast7_move = random.randint(1, move_limit)
                    ast8_move = random.randint(1, move_limit)
                    ast9_move = random.randint(1, move_limit)
                    ast10_move = random.randint(1, move_limit)
                    round += 1
            if points == 40:
                if round == 3:
                    ast1_destroy = ast2_destroy = ast3_destroy = ast4_destroy = ast5_destroy = ast6_destroy = ast7_destroy = ast8_destroy = ast9_destroy = ast10_destroy = False
                    ast1_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast2_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast3_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast4_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast5_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast6_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast7_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast8_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast9_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast10_pos = [random.randrange(-500, -30), random.randrange(0, 450)]
                    ast1_move = random.randint(1, move_limit)
                    ast2_move = random.randint(1, move_limit)
                    ast3_move = random.randint(1, move_limit)
                    ast4_move = random.randint(1, move_limit)
                    ast5_move = random.randint(1, move_limit)
                    ast6_move = random.randint(1, move_limit)
                    ast7_move = random.randint(1, move_limit)
                    ast8_move = random.randint(1, move_limit)
                    ast9_move = random.randint(1, move_limit)
                    ast10_move = random.randint(1, move_limit)
                    round += 1

                        
    #SHOOTER/TARGETING AND FLASHING LIGHTS
            pygame.draw.line(screen, PEA_GREEN, [0, 480], [mx, my], 4)
            pygame.draw.line(screen, PEA_GREEN, [640, 480], [mx, my], 4)
            pygame.draw.circle(screen, EVERGLADE_GREEN, (mx, my), 20, 3)
            pygame.draw.line(screen, EVERGLADE_GREEN, [mx-27, my], [mx-13, my], 3)
            pygame.draw.line(screen, EVERGLADE_GREEN, [mx+27, my], [mx+13, my], 3)
            pygame.draw.line(screen, EVERGLADE_GREEN, [mx, my-27], [mx, my-13], 3)
            pygame.draw.line(screen, EVERGLADE_GREEN, [mx, my+27], [mx, my+13], 3)
            pygame.draw.line(screen, EVERGLADE_GREEN, [mx-6, my], [mx+6, my], 3)
            pygame.draw.line(screen, EVERGLADE_GREEN, [mx, my-6], [mx, my+6], 3)
            if click:
                pygame.draw.line(screen, RED, [0, 480], [mx, my], 4)
                pygame.draw.line(screen, RED, [640, 480], [mx, my], 4)
    #GAME LOST
            if ast1_pos[0] >= 670 or ast2_pos[0] >= 670 or ast3_pos[0] >= 670 or ast4_pos[0] >= 670 or ast5_pos[0] >= 670 or ast6_pos[0] >= 670 or ast7_pos[0] >= 670 or ast8_pos[0] >= 670 or ast9_pos[0] >= 670 or ast10_pos[0] >= 670:
                ast1_destroy = True
                ast2_destroy = True
                ast3_destroy = True
                ast4_destroy = True
                ast5_destroy = True
                ast6_destroy = True
                ast7_destroy = True
                ast8_destroy = True
                ast9_destroy = True
                ast10_destroy = True
                lost = font.render("You Lost...", True, WHITE)
                screen.blit(lost, (lost.get_rect(center = screen.get_rect().center)[0], 420))
                menu_button = pygame.Rect([220-100, 200, 200, 80])
                pygame.draw.rect(screen, EVERGLADE_GREEN, [220+5-100, 200+5, 200, 80])
                pygame.draw.rect(screen, PEA_GREEN, menu_button)
                pygame.draw.rect(screen, EVERGLADE_GREEN, menu_button, 1)
                menu_title = font.render("BACK TO MENU", True, WHITE)
                menu_rect = menu_title.get_rect
                screen.blit(menu_title, (menu_rect(center = screen.get_rect().center)[0]-100, menu_rect(center = screen.get_rect().center)[1]))
                if menu_button.collidepoint((mx, my)):
                    if click:
                        main_menu()
                restart_button = pygame.Rect([220+100, 200, 200, 80])
                pygame.draw.rect(screen, EVERGLADE_GREEN, [220+5+100, 200+5, 200, 80])
                pygame.draw.rect(screen, PEA_GREEN, restart_button)
                pygame.draw.rect(screen, EVERGLADE_GREEN, restart_button, 1)
                restart_title = font.render("RESTART", True, WHITE)
                restart_rect = restart_title.get_rect
                screen.blit(restart_title, (restart_rect(center = screen.get_rect().center)[0]+100, restart_rect(center = screen.get_rect().center)[1]))
                if restart_button.collidepoint((mx, my)):
                    if click:
                        game_num4()

    #GAME COMPLETION
            if points >= 50:
                global game_complete4
                if game_complete4 == False:
                    global games_complete
                    games_complete += 1
                    game_complete4 = True
                menu_button = pygame.Rect([220, 200, 200, 80])
                pygame.draw.rect(screen, EVERGLADE_GREEN, [220+5, 200+5, 200, 80])
                pygame.draw.rect(screen, PEA_GREEN, menu_button)
                pygame.draw.rect(screen, EVERGLADE_GREEN, menu_button, 1)
                completion = font.render("GAME COMPLETE", True, WHITE)
                screen.blit(completion, (completion.get_rect(center = screen.get_rect().center)[0], 420))
                menu_title = font.render("BACK TO MENU", True, WHITE)
                menu_rect = menu_title.get_rect
                screen.blit(menu_title, (menu_rect(center = screen.get_rect().center)[0], menu_rect(center = screen.get_rect().center)[1]))
                if menu_button.collidepoint((mx, my)):
                    if click:
                        main_menu()
            
#EVENT GETTER
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
#DISPLAY UPDATES
        pygame.display.update()
        clock.tick(60)

main_menu()
