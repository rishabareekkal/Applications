# pygame template
import math
import pygame
from pygame import mixer

pygame.init()
pygame.font.init()
mixer.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
# mixer.music.load("8 Bit Dungeon.mp3")
# mixer.music.set_volume(0.7)
# mixer.music.play(-1)

# Use proper path
mega_font = pygame.font.Font("Grand9K Pixel.ttf", 75)
reg_font = pygame.font.Font("Grand9K Pixel.ttf", 50)
tiny_font = pygame.font.Font("Grand9K Pixel.ttf", 17)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0,162,232)
RED = (237,28,36)
MAROON = (136,0,21)
PINK = (255,174,201)
ORANGE = (255,127,39)
YELLOW = (255,242,0)
GREY = (127,127,127)
PURPLE = (163,73,164)
#Start Settings
initial_set = 305, 225, 3
complete1 = False
complete2 = False
complete3 = False
complete4 = False
# Room Sets
# Room List 1
room_list1 = []
room1_0 = [None, None, None, 1, 1]
room1_1 = [None, 0, 2, None, 1]
room1_2 = [1, 3, None, None, 1]
room1_3 = [None, 4, None, 2, 1]
room1_4 = [5, None, None, 3, 1]
room1_5 = [6, None, 4, None, 1]
room1_6 = [None, None, 5, 7, 1]
room1_7 = [None, 6, None, 8, 2]
room1_8 = [None, 7, None, None, 3]
room_list1.append([room1_0, room1_1, room1_2, room1_3, room1_4, room1_5, room1_6, room1_7, room1_8])
room_list1 = room_list1[0]
#Room List 2
room_list2 = []
room2_0 = [None, 1, None, None]
room2_1 = [None, None, 2, 0]
room2_2 = [1, 3, 4, None]
room2_3 = [5, None, 6, 2]
room2_4 = [2, None, None, None]
room2_5 = [None, None, 3, None]
room2_6 = [3, 7, None, None]
room2_7 = [None, None, None, 6]
room_list2.append([room2_0, room2_1, room2_2, room2_3, room2_4, room2_5, room2_6, room2_7])
room_list2 = room_list2[0]
# Room List 3
room_list3 = []
room3_0 = [1, 2, None, None]
room3_1 = [None, 3, 0, None]
room3_2 = [3, None, None, 0]
room3_3 = [None, 4, 2, 1]
room3_4 = [5, None, None, 3]
room3_5 = [None, 6, 4, None]
room3_6 = [None, None, 7, 5]
room3_7 = [6, 8, None, None]
room3_8 = [9, None, None, 7]
room3_9 = [None, 10, 8, None]
room3_10 = [11, None, 12, 9]
room3_11 = [None, None, 10, None]
room3_12 = [10, 13, None, None]
room3_13 = [14, None, None, 12]
room3_14 = [None, None, 13, None]
room_list3.append([room3_0, room3_1, room3_2, room3_3, room3_4, room3_5, room3_6, room3_7, room3_8, room3_9, room3_10, room3_11, room3_12, room3_13, room3_14])
room_list3 = room_list3[0]
# Room List 4
room_list4 = []
room4_0 = [1, None, None, None]
room4_1 = [2, 3, 0, 4]
room4_2 = [5, 6, 1, 7]
room4_3 = [None, None, None, 1]
room4_4 = [None, 1, None, None]
room4_5 = [None, None, 2, None]
room4_6 = [None, 8, None, 2]
room4_7 = [None, 2, None, 13]
room4_8 = [9, None, None, 6]
room4_9 = [10, 11, 8, 12]
room4_10 = [None, None, 9, None]
room4_11 = [None, None, None, 9]
room4_12 = [None, 9, None, None]
room4_13 = [14, 7, None, None]
room4_14 = [15, 16, 13, 17]
room4_15 = [None, None, 14, None]
room4_16 = [None, None, None, 14]
room4_17 = [None, 14, None, None]
room_list4.append([room4_0, room4_1, room4_2, room4_3, room4_4, room4_5, room4_6, room4_7, room4_8, room4_9, room4_10, room4_11, room4_12, room4_13, room4_14, room4_15, room4_16, room4_17])
room_list4 = room_list4[0]

room_list5 = []
room5_0 = [None, 1, None, 19]
room5_1 = [None, 2, None, 0]
room5_2 = [None, 3, None, 1]
room5_3 = [4, None, None, 2]
room5_4 = [5, None, 3, 6]
room5_5 = [None, None, 4, None]
room5_6 = [None, 5, None, 7]
room5_7 = [8, 6, None, None]
room5_8 = [None, None, 7, 9]
room5_9 = [10, 8, 11, 12]
room5_10 = [None, None, 9, None]
room5_11 = [9, None, None, None]
room5_12 = [None, 9, 13, None]
room5_13 = [12, None, None, 14]
room5_14 = [None, 13, None, 15]
room5_15 = [16, 14, 17, None]
room5_16 = [None, None, 15, None]
room5_17 = [15, 18, None, None]
room5_18 = [None, 19, None, 17]
room5_19 = [None, 0, None, 18]
room_list5.append([room5_0, room5_1, room5_2, room5_3, room5_4, room5_5, room5_6, room5_7, room5_8, room5_9, room5_10, room5_11, room5_12, room5_13, room5_14, room5_15, room5_16, room5_17, room5_18, room5_19])
room_list5 = room_list5[0]

# ---------------------------

def room_generate(room_list, room_start, current_room):
    global player_x, player_y, player, complete1
    if room_list[current_room][0] != None:
        next_room = room_list[current_room][0]
        door1 = pygame.draw.rect(screen, RED, [220, 3, 200, 10])
        if player.colliderect(door1):
            player_x = 305
            player_y = 437
            room_start = True
            current_room = next_room
    if room_list[current_room][1] != None:
        next_room = room_list[current_room][1]
        door2 = pygame.draw.rect(screen, RED, [547, 140, 10, 200])
        if player.colliderect(door2):
            player_x = 93
            player_y = 225
            room_start = True
            current_room = next_room
    if room_list[current_room][2] != None:
        next_room = room_list[current_room][2]
        door3 = pygame.draw.rect(screen, RED, [220, 467, 200, 10])
        if player.colliderect(door3):
            player_x = 305
            player_y = 13
            room_start = True
            current_room = next_room
    if room_list[current_room][3] != None:
        next_room = room_list[current_room][3]
        door4 = pygame.draw.rect(screen, RED, [83, 140, 10, 200])
        if player.colliderect(door4):
            player_x = 517
            player_y = 225
            room_start = True
            current_room = next_room
    if room_list[current_room] == room_list[-1]:
        dungeon_door = pygame.draw.rect(screen, RED, [305, 300, 30, 30])
        if player.colliderect(dungeon_door):
            complete1 = True
            main_base()
    return current_room, room_start

def movement():
    global player_x, player_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_y > 3:
            player_y -= 3
    if keys[pygame.K_s]:
        if player_y < 447:
            player_y += 3
    if keys[pygame.K_a]:
        if player_x > 83:
            player_x -= 3
    if keys[pygame.K_d]:
        if player_x < 527:
            player_x += 3

    if player_x < 83:
        player_x = 83
    if player_x > 527:
        player_x = 527
    if player_y < 3:
        player_y = 3
    if player_y > 447:
        player_y = 447

def event_getter(run_value, pause_value, select_value):
    global left, right
    select_value = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run_value = False
            if event.key == pygame.K_SPACE or event.key == pygame.K_i:
                if pause_value == True:
                    select_value = True
                else:
                    print("attack")
                    select_value = False
            if event.key == pygame.K_o:
                if pause_value == True:
                    pause_value = False
                elif not pause_value:
                    pause_value = True
                else:
                    print("error occured")
            if pause_value == True:
                if event.key == pygame.K_a:
                    if right == True:
                        left = True
                        right = False
                if event.key == pygame.K_d:
                    if left == True:
                        right = True
                        left = False
        elif event.type == pygame.QUIT:
            run_value = False
    return run_value, pause_value, select_value

def extra_displays(hearts):
    w_inst = tiny_font.render("W: Up", False, RED)
    s_inst = tiny_font.render("S: Down", False, RED)
    a_inst = tiny_font.render("A: Left", False, RED)
    d_inst = tiny_font.render("D: Right", False, RED)
    i_inst = tiny_font.render("I: ATK", False, RED)
    o_inst = tiny_font.render("O: Pause", False, RED)
    screen.blit(w_inst, (5, 5))
    screen.blit(s_inst, (5, 25))
    screen.blit(a_inst, (5, 45))
    screen.blit(d_inst, (5, 65))
    screen.blit(i_inst, (5, 85))
    screen.blit(o_inst, (5, 105))
    if hearts >= 1:
        pygame.draw.rect(screen, RED, [90, 5, 10, 10])
    if hearts >= 2:
        pygame.draw.rect(screen, RED, [105, 5, 10, 10])
    if hearts == 3:
        pygame.draw.rect(screen, RED, [120, 5, 10, 10])
    if hearts == 0:
        main_base()
        

def enemy(enemies, room_start, hearts):
    global player_x, player_y, enemies_list, damage, shoot
    if room_start:
        damage = True
        enemies_list = []
        for i in range(enemies):
            enemyx = i * 100 + 80
            enemyy = 30
            enemies_list.append([enemyx, enemyy, None])
        room_start = False
    if len(enemies_list) > 0:
        for enemy in enemies_list:
            if enemy[0] < player_x:
                enemy[0] += 1
            elif enemy[0] > player_x:
                enemy[0] -= 1
            if enemy[1] < player_y:
                enemy[1] += 1
            elif enemy[1] > player_y:
                enemy[1] -= 1
            enemy[2] = pygame.draw.rect(screen, RED, [enemy[0], enemy[1], 30, 30])
            mathangle = math.atan2((player_y+15) - (enemyy+15), (player_x+15) - (enemyx+15))
            rotation = int(mathangle * 180 / math.pi)
            dx = (math.cos(mathangle) * 2)
            dy = (math.sin(mathangle) * 2)
        
        if shoot:
            bulletx += dx * 1
            bullety += dy * 1
            bullet = pygame.circle.draw(screen, PURPLE, (bulletx, bullety), 2)

            if enemy[2].colliderect(player):
                if damage == True:
                    hearts -= 1
                    if enemy[0] < player_x and player_x < 477:
                        player_x += 50
                    elif enemy[0] > player_x and player_x > 133:
                        player_x -= 50
                    if enemy[1] < player_y and player_y > 53:
                        player_y += 50
                    elif enemy[1] > player_y and player_y < 397:
                        player_y -= 50
                    damage = False
                
            else: 
                damage = True
    return room_start, hearts


def player_settings(select):
    global left, right, atk_power
    screen.fill(BLACK)  # always the first drawing command
    pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)
    set_text = mega_font.render("Settings", False, RED)
    screen.blit(set_text, (set_text.get_rect(center = screen.get_rect().center)[0], 5))
    atk_text = reg_font.render(f"> Atk: {atk_power}", False, RED)
    atktxt_rect = atk_text.get_rect(center = screen.get_rect().center)
    screen.blit(atk_text, atktxt_rect)
    if select:
        atk_power += 0.1
        atk_power = round(atk_power, 1)
        print("atk selected")
        select = False
    return select


def main_base():
    global player_x, player_y, player, atk_power, damage
    global complete1, complete2, complete3, complete4
    global left, right
    player_x, player_y, hearts = initial_set
    atk_power = 0.1
    damage = True
    player = pygame.draw.rect(screen, BLUE, [player_x, player_y, 30, 30])
    left = True
    right = False
    select = False
    running = True
    pause = False
    while running:
        if pause:
            select = player_settings(select)
        else:
            screen.fill(BLACK)  # always the first drawing command
            pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)
            home = mega_font.render("HOME", False, RED)
            screen.blit(home, (home.get_rect(center = screen.get_rect().center)))
            extra_displays(hearts)

            door1 = pygame.draw.rect(screen, RED, [220, 3, 200, 10])
            if player.colliderect(door1):
                dungeon1()
            if complete1:
                door2 = pygame.draw.rect(screen, RED, [547, 140, 10, 200])
                if player.colliderect(door2):
                    dungeon2()
            if complete2:
                door3 = pygame.draw.rect(screen, RED, [220, 467, 200, 10])
                if player.colliderect(door3):
                    dungeon3()
            if complete3:
                door4 = pygame.draw.rect(screen, RED, [83, 140, 10, 200])
                if player.colliderect(door4):
                    dungeon4()
            if complete4:
                door5 = pygame.draw.rect(screen, RED, [305, 300, 30, 30], 5)
                if player.colliderect(door5):
                    dungeon5()

            player = pygame.draw.rect(screen, BLUE, [player_x, player_y, 30, 30])
            movement()
        running, pause, select = event_getter(running, pause, select)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

def dungeon1():

    global player_x, player_y, player, enemies_list
    global left, right
    current_room = 0
    player_x, player_y, hearts = initial_set

    left = True
    right = False
    select = False
    pause = False
    room_start = True
    enemies_list = []
    running = True
    while running:
        if pause:
            player_settings(select)
        else:
            screen.fill(BLACK)  # always the first drawing command
            pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)
            dun1_txt = mega_font.render("1", False, RED)
            screen.blit(dun1_txt, (dun1_txt.get_rect(center = screen.get_rect().center)))
            enemies = room_list1[current_room][-1]
            room_start, hearts = enemy(enemies, room_start, hearts)
            extra_displays(hearts)

            player = pygame.draw.rect(screen, BLUE, [player_x, player_y, 30, 30])
            current_room, room_start = room_generate(room_list1, room_start, current_room)
            movement()
        running, pause, select = event_getter(running, pause, select)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

def dungeon2():
    global player_x, player_y, player
    global left, right
    current_room = 0
    player_x, player_y, hearts = initial_set
    left = True
    right = False
    select = False
    pause = False
    running = True
    while running:
        if pause:
            player_settings(select)
        else:
            screen.fill(BLACK)  # always the first drawing command
            pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)
            dun1_txt = mega_font.render("1", False, RED)
            screen.blit(dun1_txt, (dun1_txt.get_rect(center = screen.get_rect().center)))
            extra_displays(hearts)


            player = pygame.draw.rect(screen, BLUE, [player_x, player_y, 30, 30])
            current_room = room_generate(room_list2, current_room)
            movement()
        running, pause, select = event_getter(running, pause, select)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    
def dungeon3():
    global player_x, player_y, player
    global left, right
    current_room = 0
    player_x, player_y, hearts = initial_set
    left = True
    right = False
    select = False
    pause = False
    running = True
    while running:
        if pause:
            player_settings(select)
        else:
            screen.fill(BLACK)  # always the first drawing command
            pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)
            dun1_txt = mega_font.render("1", False, RED)
            screen.blit(dun1_txt, (dun1_txt.get_rect(center = screen.get_rect().center)))
            extra_displays(hearts)


            player = pygame.draw.rect(screen, BLUE, [player_x, player_y, 30, 30])
            current_room = room_generate(room_list3, current_room)
            movement()
        running, pause, select = event_getter(running, pause, select)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

def dungeon4():
    global player_x, player_y, player
    global left, right
    current_room = 0
    player_x, player_y, hearts = initial_set
    left = True
    right = False
    select = False
    pause = False
    running = True
    while running:
        if pause:
            player_settings(select)
        else:
            screen.fill(BLACK)  # always the first drawing command
            pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)
            dun1_txt = mega_font.render("1", False, RED)
            screen.blit(dun1_txt, (dun1_txt.get_rect(center = screen.get_rect().center)))
            extra_displays(hearts)


            player = pygame.draw.rect(screen, BLUE, [player_x, player_y, 30, 30])
            current_room = room_generate(room_list4, current_room)
            movement()
        running, pause, select = event_getter(running, pause, select)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

def dungeon5():
    global player_x, player_y, player
    global left, right
    current_room = 0
    player_x, player_y, hearts = initial_set
    left = True
    right = False
    select = False
    pause = False
    running = True
    while running:
        if pause:
            player_settings(select)
        else:
            screen.fill(BLACK)  # always the first drawing command
            pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)
            dun1_txt = mega_font.render("1", False, RED)
            screen.blit(dun1_txt, (dun1_txt.get_rect(center = screen.get_rect().center)))
            extra_displays(hearts)


            player = pygame.draw.rect(screen, BLUE, [player_x, player_y, 30, 30])
            current_room = room_generate(room_list5, current_room)
            movement()
        running, pause, select = event_getter(running, pause, select)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


if __name__ == "__main__":
    main_base()
