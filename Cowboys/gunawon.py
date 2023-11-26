import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.fadeout(1000)
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
font = pygame.font.Font("Grand9K Pixel.ttf", 50)
font.set_bold(True)
name_font = pygame.font.Font("Grand9K Pixel.ttf", 30)
name_font.set_bold(True)
info_font = pygame.font.Font("Grand9K Pixel.ttf", 15)
info_font.set_bold(True)
pygame.display.set_caption('Cowboys')

class gungame:
    def __init__(self) -> None:
        self.running = True
        self.click = False
        self.gunshot = pygame.mixer.Sound("cowboy_gunshot.mp3")
        self.background = pygame.image.load("cowboy_background.png")
        self.game_1player = pygame.image.load("cowboy_1player.png")
        self.game_1player = pygame.transform.scale(self.game_1player, (345/3*2, 195/3*2))
        self.game_2player = pygame.image.load("cowboy_2player.png")
        self.game_2player = pygame.transform.scale(self.game_2player, (345/3*2, 195/3*2))
        self.game_mashmode = pygame.image.load("cowboy_mashmode.png")
        self.game_mashmode = pygame.transform.scale(self.game_mashmode, (345/3*2, 195/3*2))
        self.game_timemode = pygame.image.load("cowboy_timemode.png")
        self.game_timemode = pygame.transform.scale(self.game_timemode, (345/3*2, 195/3*2))
        self.game_back = pygame.image.load("cowboy_backbutton.png")
        self.game_back = pygame.transform.scale(self.game_back, (345/3, 195/3))
        self.game_info = pygame.image.load("cowboy_info.png")
        self.game_info = pygame.transform.scale(self.game_info, (345/3, 195/3))
        self.player_mode = 1
        self.game_mode = None
        self.fire_time = False

        self.player1 = pygame.image.load("cowboys1_1.png")
        self.player1 = pygame.transform.scale(self.player1, (50, 100))
        self.player2 = pygame.image.load("cowboys2_1.png")
        self.player2 = pygame.transform.flip(self.player2, True, False)

        self.player1_time = 0
        self.player1_spam = 0
        self.player1_win = False
        self.player2_time = 0
        self.player2_spam = 0
        self.player2_win = False

        self.players_tie = False

        self.player1_frame = 0
        self.player1_idle = True
        self.player1_fire = False
        self.player1_gunshot = False
        self.player1_die = False
        self.player2_frame = 0
        self.player2_idle = True
        self.player2_fire = False
        self.player2_gunshot = False
        self.player2_die = False


    def event_getter(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if self.player_mode == 2:
                    if self.player2_time == 0:
                        if event.key == pygame.K_k:
                            if self.game_mode == "timemode":
                                if self.fire_time:
                                    self.player2_fire = True
                                    self.player2_idle = False
                                    self.player2_time = pygame.time.get_ticks() + self.player2_spam
                                    self.player2_frame = 0
                                    self.player2_gunshot = True
                                else:
                                    self.player2_spam += 50
                            else:
                                if self.fire_time:
                                    self.player2_fire = True
                                    self.player2_idle = False
                                    self.player2_frame = 0
                                    self.player2_gunshot = True
                                    self.player2_spam += 50
                    if self.player1_time == 0:
                        if event.key == pygame.K_s:
                            if self.game_mode == "timemode":
                                if self.fire_time:
                                    self.player1_fire = True
                                    self.player1_idle = False
                                    self.player1_time = pygame.time.get_ticks() + self.player1_spam
                                    self.player1_frame = 0
                                    self.player1_gunshot = True
                                else:
                                    self.player1_spam += 50
                            else:
                                if self.fire_time:
                                    self.player1_fire = True
                                    self.player1_idle = False
                                    self.player1_frame = 0
                                    self.player1_gunshot = True
                                    self.player1_spam += 50
                else:
                    if self.player1_time == 0:
                        if event.key == pygame.K_SPACE:
                            if self.game_mode == "timemode":
                                if self.fire_time:
                                    self.player1_fire = True
                                    self.player1_idle = False
                                    self.player1_time = pygame.time.get_ticks() + self.player1_spam
                                    self.player1_frame = 0
                                    self.player1_gunshot = True
                                else:
                                    self.player1_spam += 50
                            else:
                                if self.fire_time:
                                    self.player1_fire = True
                                    self.player1_idle = False
                                    self.player1_frame = 0
                                    self.player1_gunshot = True
                                    self.player1_spam += 50
            elif event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            else:
                self.click = False

    def animations(self) -> None:
        if self.player1_idle:
            self.player1_frame += 1
            if 0 <= self.player1_frame < 15:
                self.player1 = pygame.image.load("cowboys1_1.png")
                self.player1 = pygame.transform.scale(self.player1, (12*5, 16*5))
            elif 15 <= self.player1_frame < 30:
                self.player1 = pygame.image.load("cowboys1_2.png")
                self.player1 = pygame.transform.scale(self.player1, (12*5, 17*5))
            elif 30 <= self.player1_frame < 45:
                self.player1 = pygame.image.load("cowboys1_3.png")
                self.player1 = pygame.transform.scale(self.player1, (12*5, 16*5))
            elif 45 <= self.player1_frame < 60:
                self.player1 = pygame.image.load("cowboys1_4.png")
                self.player1 = pygame.transform.scale(self.player1, (12*5, 15*5))
            else:
                self.player1_frame = 0
        elif self.player1_fire:
            self.player1_frame += 1
            if 0 <= self.player1_frame < 4:
                self.player1 = pygame.image.load("cowboys1_5.png")
                self.player1 = pygame.transform.scale(self.player1, (13*5, 15*5))
            elif 4 <= self.player1_frame < 8:
                self.player1 = pygame.image.load("cowboys1_6.png")
                self.player1 = pygame.transform.scale(self.player1, (12*5, 16*5))
            elif 8 <= self.player1_frame < 12:
                self.player1 = pygame.image.load("cowboys1_7.png")
                self.player1 = pygame.transform.scale(self.player1, (16*5, 16*5))
                if self.player1_gunshot:
                    pygame.mixer.Sound.play(self.gunshot)
                    self.player1_gunshot = False
            elif 12 <= self.player1_frame < 16:
                self.player1 = pygame.image.load("cowboys1_11.png")
                self.player1 = pygame.transform.scale(self.player1, (12*5, 15*5))
            else:
                self.player1_idle = True
                self.player1_fire = False
        else:
            self.player1_frame += 1
            if 0 <= self.player1_frame < 15:
                self.player1 = pygame.image.load("cowboys1_12.png")
                self.player1 = pygame.transform.scale(self.player1, (16*5, 16*5))
            elif 15 <= self.player1_frame < 30:
                self.player1 = pygame.image.load("cowboys1_13.png")
                self.player1 = pygame.transform.scale(self.player1, (15*5, 14*5))
            elif 30 <= self.player1_frame < 45:
                self.player1 = pygame.image.load("cowboys1_14.png")
                self.player1 = pygame.transform.scale(self.player1, (16*5, 12*5))
            elif 45 <= self.player1_frame < 60:
                self.player1 = pygame.image.load("cowboys1_15.png")
                self.player1 = pygame.transform.scale(self.player1, (21*5, 8*5))
            else:
                self.player1_frame = 60

        player1_rect = self.player1.get_rect()
        player1_rect.bottom = 380
        player1_rect.left = 15
        screen.blit(self.player1, player1_rect)

        if self.player2_idle:
            self.player2_frame += 1
            if 0 <= self.player2_frame < 15:
                self.player2 = pygame.image.load("cowboys2_1.png")
                self.player2 = pygame.transform.scale(self.player2, (13*5, 16*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
            elif 15 <= self.player2_frame < 30:
                self.player2 = pygame.image.load("cowboys2_2.png")
                self.player2 = pygame.transform.scale(self.player2, (13*5, 17*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
            elif 30 <= self.player2_frame < 45:
                self.player2 = pygame.image.load("cowboys2_3.png")
                self.player2 = pygame.transform.scale(self.player2, (13*5, 16*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
            elif 45 <= self.player2_frame < 60:
                self.player2 = pygame.image.load("cowboys2_4.png")
                self.player2 = pygame.transform.scale(self.player2, (13*5, 15*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
            else:
                self.player2_frame = 0
        elif self.player2_fire:
            self.player2_frame += 1
            if 0 <= self.player2_frame < 4:
                self.player2 = pygame.image.load("cowboys2_5.png")
                self.player2 = pygame.transform.scale(self.player2, (13*5, 15*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
            elif 4 <= self.player2_frame < 8:
                self.player2 = pygame.image.load("cowboys2_6.png")
                self.player2 = pygame.transform.scale(self.player2, (12*5, 16*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
            elif 8 <= self.player2_frame < 12:
                self.player2 = pygame.image.load("cowboys2_7.png")
                self.player2 = pygame.transform.scale(self.player2, (16*5, 16*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
                if self.player2_gunshot:
                    pygame.mixer.Sound.play(self.gunshot)
                    self.player2_gunshot = False
            elif 12 <= self.player2_frame < 16:
                self.player2 = pygame.image.load("cowboys2_11.png")
                self.player2 = pygame.transform.scale(self.player2, (12*5, 15*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
            else:
                self.player2_frame = 0
                self.player2_idle = True
                self.player2_fire = False
        else:
            self.player2_frame += 1
            if 0 <= self.player2_frame < 15:
                self.player2 = pygame.image.load("cowboys2_12.png")
                self.player2 = pygame.transform.scale(self.player2, (16*5, 16*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
            elif 15 <= self.player2_frame < 30:
                self.player2 = pygame.image.load("cowboys2_13.png")
                self.player2 = pygame.transform.scale(self.player2, (15*5, 14*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
            elif 30 <= self.player2_frame < 45:
                self.player2 = pygame.image.load("cowboys2_14.png")
                self.player2 = pygame.transform.scale(self.player2, (17*5, 13*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
            elif 45 <= self.player2_frame < 60:
                self.player2 = pygame.image.load("cowboys2_15.png")
                self.player2 = pygame.transform.scale(self.player2, (21*5, 9*5))
                self.player2 = pygame.transform.flip(self.player2, True, False)
            else:
                self.player2_frame = 60

        player2_rect = self.player2.get_rect()
        player2_rect.bottom = 380
        player2_rect.right = 625
        screen.blit(self.player2, player2_rect)
    
    def one_guna_one(self) -> None:
        self.running = True
        start_time = pygame.time.get_ticks()
        time = (pygame.time.get_ticks()-start_time)
        counter = 6*60
        time_text = font.render(f"{counter}", False, (255, 0, 0))
        time_text_rect = time_text.get_rect()
        time_text_rect.centerx = screen.get_rect().centerx
        time_text_rect.centery = 315
        p1_text = name_font.render("P1", False, (255, 0, 0))
        p1_text_rect = p1_text.get_rect()
        p1_text_rect.left = 15
        p1_text_rect.centery = 280
        p2_text = name_font.render("P2", False, (255, 0, 0))
        p2_text_rect = p2_text.get_rect()
        p2_text_rect.right = 625
        p2_text_rect.centery = 280
        p1win_text = font.render("P1 WIN", False, (255, 0, 0))
        p2win_text = font.render("P2 WIN", False, (255, 0, 0))
        tie_text = font.render("TIE", False, (255, 0, 0))

        while self.running:
            gungame.event_getter(self)
            screen.blit(self.background, (0, 0))
            gungame.animations(self)

            screen.blit(p1_text, p1_text_rect)
            screen.blit(p2_text, p2_text_rect)

            time = (pygame.time.get_ticks()-start_time)
            if counter >= -510:
                counter -= 1
                if counter//60 > 0:
                    self.fire_time = False
                    time_text = font.render(f"{counter//60}", False, (255, 0, 0))
                    time_text_rect = time_text.get_rect()
                    time_text_rect.centerx = screen.get_rect().centerx
                    time_text_rect.centery = 315
                    screen.blit(time_text, time_text_rect)
                else:
                    self.fire_time = True
                    time_text = font.render(f"MASH!: {(600+counter)//60}", False, (255, 0, 0))
                    time_text_rect = time_text.get_rect()
                    time_text_rect.centerx = screen.get_rect().centerx
                    time_text_rect.centery = 315
                    screen.blit(time_text, time_text_rect)
            else:
                self.fire_time = False
                if 16000 < time < 16100:
                    print(self.player1_spam, self.player2_spam)
                    if self.player1_spam > self.player2_spam:
                        self.player1_win = True
                        self.player2_die = True
                        self.player2_idle = False
                        self.player2_fire = False
                        self.player2_frame = 0
                    elif self.player2_spam > self.player1_spam:
                        self.player2_win = True
                        self.player1_die = True
                        self.player1_idle = False
                        self.player1_fire = False
                        self.player1_frame = 0
                    else:
                        self.players_tie = True
                        self.player1_die = True
                        self.player1_idle = False
                        self.player1_fire = False
                        self.player1_frame = 0
                        self.player2_die = True
                        self.player2_idle = False
                        self.player2_fire = False
                        self.player2_frame = 0

            if self.player1_win:
                screen.blit(p1win_text, (p1win_text.get_rect(center = screen.get_rect().center)))
            elif self.player2_win:
                screen.blit(p2win_text, (p2win_text.get_rect(center = screen.get_rect().center)))
            elif self.players_tie:
                screen.blit(tie_text, (tie_text.get_rect(center = screen.get_rect().center)))
            if time > 23000:
                pygame.mixer.music.fadeout(1000)
            if time > 24000:
                game = gungame()
                game.run()

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def one_guna_juan(self) -> None:
        self.running = True
        start_time = pygame.time.get_ticks()
        time = (pygame.time.get_ticks()-start_time)
        counter = 6*60
        time_text = font.render(f"{counter}", False, (255, 0, 0))
        time_text_rect = time_text.get_rect()
        time_text_rect.centerx = screen.get_rect().centerx
        time_text_rect.centery = 315
        you_text = name_font.render("YOU", False, (255, 0, 0))
        you_text_rect = you_text.get_rect()
        you_text_rect.left = 15
        you_text_rect.centery = 280
        juan_text = name_font.render("JUAN", False, (255, 0, 0))
        juan_text_rect = juan_text.get_rect()
        juan_text_rect.right = 625
        juan_text_rect.centery = 280
        youwin_text = font.render("YOU WIN", False, (255, 0, 0))
        juanwin_text = font.render("JUAN WON", False, (255, 0, 0))
        tie_text = font.render("TIE", False, (255, 0, 0))

        while self.running:
            gungame.event_getter(self)
            screen.blit(self.background, (0, 0))
            gungame.animations(self)

            screen.blit(you_text, you_text_rect)
            screen.blit(juan_text, juan_text_rect)

            time = (pygame.time.get_ticks()-start_time)
            if counter >= -510:
                counter -= 1
                if counter//60 > 0:
                    self.fire_time = False
                    time_text = font.render(f"{counter//60}", False, (255, 0, 0))
                    time_text_rect = time_text.get_rect()
                    time_text_rect.centerx = screen.get_rect().centerx
                    time_text_rect.centery = 315
                    screen.blit(time_text, time_text_rect)
                else:
                    if random.randrange(9) == 0:
                        self.player2_fire = True
                        self.player2_idle = False
                        self.player2_frame = 0
                        self.player2_gunshot = True
                        self.player2_spam += 50
                    self.fire_time = True
                    time_text = font.render(f"MASH!: {(600+counter)//60}", False, (255, 0, 0))
                    time_text_rect = time_text.get_rect()
                    time_text_rect.centerx = screen.get_rect().centerx
                    time_text_rect.centery = 315
                    screen.blit(time_text, time_text_rect)
            else:
                self.fire_time = False
                if 16000 < time < 16100:
                    print(self.player1_spam, self.player2_spam)
                    if self.player1_spam > self.player2_spam:
                        self.player1_win = True
                        self.player2_die = True
                        self.player2_idle = False
                        self.player2_fire = False
                        self.player2_frame = 0
                    elif self.player2_spam > self.player1_spam:
                        self.player2_win = True
                        self.player1_die = True
                        self.player1_idle = False
                        self.player1_fire = False
                        self.player1_frame = 0
                    else:
                        self.players_tie = True
                        self.player1_die = True
                        self.player1_idle = False
                        self.player1_fire = False
                        self.player1_frame = 0
                        self.player2_die = True
                        self.player2_idle = False
                        self.player2_fire = False
                        self.player2_frame = 0

            if self.player1_win:
                screen.blit(youwin_text, (youwin_text.get_rect(center = screen.get_rect().center)))
            elif self.player2_win:
                screen.blit(juanwin_text, (juanwin_text.get_rect(center = screen.get_rect().center)))
            elif self.players_tie:
                screen.blit(tie_text, (tie_text.get_rect(center = screen.get_rect().center)))
            if time > 23000:
                pygame.mixer.music.fadeout(1000)
            if time > 24000:
                game = gungame()
                game.run()

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def one_won_one(self) -> None:
        self.running = True
        start_time = pygame.time.get_ticks()
        time = float("%.1f" % round((pygame.time.get_ticks()-start_time)/1000, 1))
        countdown = 5

        fire_text = font.render(f"{countdown}", False, (255, 0, 0))
        fire_text_rect = fire_text.get_rect()
        fire_text_rect.centerx = screen.get_rect().centerx
        fire_text_rect.centery = 315
        p1_text = name_font.render("P1", False, (255, 0, 0))
        p1_text_rect = p1_text.get_rect()
        p1_text_rect.left = 15
        p1_text_rect.centery = 280
        p2_text = name_font.render("P2", False, (255, 0, 0))
        p2_text_rect = p2_text.get_rect()
        p2_text_rect.right = 625
        p2_text_rect.centery = 280
        p1win_text = font.render("P1 WIN", False, (255, 0, 0))
        p2win_text = font.render("P2 WIN", False, (255, 0, 0))
        tie_text = font.render("TIE", False, (255, 0, 0))

        topslide = 0
        bottomslide = 640
        while self.running:
            gungame.event_getter(self)
            screen.blit(self.background, (0, 0))
            gungame.animations(self)

            screen.blit(p1_text, p1_text_rect)
            screen.blit(p2_text, p2_text_rect)

            time = round((pygame.time.get_ticks()-start_time)/1000, 1)
            time = float("%.1f" % time)
            if 11.1 <= time <= 12:
                self.fire_time = True
                fire_text = font.render("FIRE!", False, (255, 0, 0))
                fire_text_rect = fire_text.get_rect()
                fire_text_rect.centerx = screen.get_rect().centerx
                fire_text_rect.centery = 315
                screen.blit(fire_text, fire_text_rect)
            elif 11 >= time > 6:
                pygame.draw.rect(screen, (0, 0, 0), [0, 0, 640, topslide])
                pygame.draw.rect(screen, (0, 0, 0), [0, bottomslide, 640, 320])
                countdown = 7-abs(time-5)
                countdown = int(float("%.1f" % countdown))
                if countdown == 5:
                    topslide = 60
                    bottomslide = 640-60
                elif countdown == 4:
                    topslide = 120
                    bottomslide = 640-120
                elif countdown == 3:
                    topslide = 180
                    bottomslide = 640-180
                elif countdown == 2:
                    topslide = 240
                    bottomslide = 640-240
                elif countdown == 1:
                    topslide = 300
                    bottomslide = 640-300
                fire_text = font.render(f"{countdown}", False, (255, 0, 0))
                fire_text_rect = fire_text.get_rect()
                fire_text_rect.centerx = screen.get_rect().centerx
                fire_text_rect.centery = 315
                screen.blit(fire_text, fire_text_rect)
            else:
                self.fire_time = False
                if time == 15:
                    print(self.player1_time-start_time, self.player2_time-start_time)
                    if (self.player1_time < self.player2_time and self.player1_time != 0) or (self.player1_time > self.player2_time and self.player2_time == 0):
                        self.player1_win = True
                        self.player2_die = True
                        self.player2_idle = False
                        self.player2_fire = False
                        self.player2_frame = 0
                    elif (self.player2_time < self.player1_time and self.player2_time != 0) or (self.player2_time > self.player1_time and self.player1_time == 0):
                        self.player2_win = True
                        self.player1_die = True
                        self.player1_idle = False
                        self.player1_fire = False
                        self.player1_frame = 0
                    else:
                        self.players_tie = True
                        self.player1_die = True
                        self.player1_idle = False
                        self.player1_fire = False
                        self.player1_frame = 0
                        self.player2_die = True
                        self.player2_idle = False
                        self.player2_fire = False
                        self.player2_frame = 0

            if self.player1_win:
                screen.blit(p1win_text, (p1win_text.get_rect(center = screen.get_rect().center)))
            elif self.player2_win:
                screen.blit(p2win_text, (p2win_text.get_rect(center = screen.get_rect().center)))
            elif self.players_tie:
                screen.blit(tie_text, (tie_text.get_rect(center = screen.get_rect().center)))
            if time > 23:
                pygame.mixer.music.fadeout(1000)
            if time > 24:
                game = gungame()
                game.run()

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def one_won_juan(self) -> None:
        self.running = True
        start_time = pygame.time.get_ticks()
        time = float("%.1f" % round((pygame.time.get_ticks()-start_time)/1000, 1))
        countdown = 5

        fire_text = font.render(f"{countdown}", False, (255, 0, 0))
        fire_text_rect = fire_text.get_rect()
        fire_text_rect.centerx = screen.get_rect().centerx
        fire_text_rect.centery = 315
        you_text = name_font.render("YOU", False, (255, 0, 0))
        you_text_rect = you_text.get_rect()
        you_text_rect.left = 15
        you_text_rect.centery = 280
        juan_text = name_font.render("JUAN", False, (255, 0, 0))
        juan_text_rect = juan_text.get_rect()
        juan_text_rect.right = 625
        juan_text_rect.centery = 280
        youwin_text = font.render("YOU WIN", False, (255, 0, 0))
        juanwin_text = font.render("JUAN WON", False, (255, 0, 0))
        tie_text = font.render("TIE", False, (255, 0, 0))

        topslide = 0
        bottomslide = 640
        player2_check = 9
        while self.running:
            gungame.event_getter(self)
            screen.blit(self.background, (0, 0))
            gungame.animations(self)

            screen.blit(you_text, you_text_rect)
            screen.blit(juan_text, juan_text_rect)

            time = round((pygame.time.get_ticks()-start_time)/1000, 1)
            time = float("%.1f" % time)
            if 11.1 <= time <= 12:
                if player2_check == 0:
                    self.player2_time = pygame.time.get_ticks()
                    self.player2_fire = True
                    self.player2_idle = False
                    self.player2_frame = 0
                    self.player2_gunshot = True
                    player2_check = -1
                elif player2_check > 0:
                    player2_check = random.randrange(9)
                self.fire_time = True
                fire_text = font.render("FIRE!", False, (255, 0, 0))
                fire_text_rect = fire_text.get_rect()
                fire_text_rect.centerx = screen.get_rect().centerx
                fire_text_rect.centery = 315
                screen.blit(fire_text, fire_text_rect)
            elif 11 >= time > 6:
                pygame.draw.rect(screen, (0, 0, 0), [0, 0, 640, topslide])
                pygame.draw.rect(screen, (0, 0, 0), [0, bottomslide, 640, 320])
                countdown = 7-abs(time-5)
                countdown = int(float("%.1f" % countdown))
                if countdown == 5:
                    topslide = 60
                    bottomslide = 640-60
                elif countdown == 4:
                    topslide = 120
                    bottomslide = 640-120
                elif countdown == 3:
                    topslide = 180
                    bottomslide = 640-180
                elif countdown == 2:
                    topslide = 240
                    bottomslide = 640-240
                elif countdown == 1:
                    topslide = 300
                    bottomslide = 640-300
                fire_text = font.render(f"{countdown}", False, (255, 0, 0))
                fire_text_rect = fire_text.get_rect()
                fire_text_rect.centerx = screen.get_rect().centerx
                fire_text_rect.centery = 315
                screen.blit(fire_text, fire_text_rect)
            else:
                self.fire_time = False
                if time == 15:
                    print(self.player1_time-start_time, self.player2_time-start_time)
                    if (self.player1_time < self.player2_time and self.player1_time != 0) or (self.player1_time > self.player2_time and self.player2_time == 0):
                        self.player1_win = True
                        self.player2_die = True
                        self.player2_idle = False
                        self.player2_fire = False
                        self.player2_frame = 0
                    elif (self.player2_time < self.player1_time and self.player2_time != 0) or (self.player2_time > self.player1_time and self.player1_time == 0):
                        self.player2_win = True
                        self.player1_die = True
                        self.player1_idle = False
                        self.player1_fire = False
                        self.player1_frame = 0
                    else:
                        self.players_tie = True
                        self.player1_die = True
                        self.player1_idle = False
                        self.player1_fire = False
                        self.player1_frame = 0
                        self.player2_die = True
                        self.player2_idle = False
                        self.player2_fire = False
                        self.player2_frame = 0

            if self.player1_win:
                screen.blit(youwin_text, (youwin_text.get_rect(center = screen.get_rect().center)))
            elif self.player2_win:
                screen.blit(juanwin_text, (juanwin_text.get_rect(center = screen.get_rect().center)))
            elif self.players_tie:
                screen.blit(tie_text, (tie_text.get_rect(center = screen.get_rect().center)))
            if time > 23:
                pygame.mixer.music.fadeout(1000)
            if time > 24:
                game = gungame()
                game.run()

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def run(self) -> None:
        pygame.mixer.music.load("tiny guitar.mp3")
        pygame.mixer.music.play(-1, 0, 1000)
        self.running = True
        game_1player_rect = self.game_1player.get_rect()
        game_1player_rect.centerx = screen.get_rect().centerx
        game_1player_rect.centery = 220
        game_2player_rect = self.game_2player.get_rect()
        game_2player_rect.centerx = screen.get_rect().centerx
        game_2player_rect.centery = 380
        game_1button = screen.blit(self.game_1player, game_1player_rect)
        game_2button = screen.blit(self.game_2player, game_2player_rect)
        game_mashmode_rect = self.game_mashmode.get_rect()
        game_mashmode_rect.centerx = screen.get_rect().centerx
        game_mashmode_rect.centery = 220
        game_timemode_rect = self.game_timemode.get_rect()
        game_timemode_rect.centerx = screen.get_rect().centerx
        game_timemode_rect.centery = 380
        mashmode_button = screen.blit(self.game_mashmode, game_mashmode_rect)
        timemode_button = screen.blit(self.game_timemode, game_timemode_rect)
        back_button = screen.blit(self.game_back, (15, 15))
        info_button = screen.blit(self.game_info, (15, 15))
        info_list = [
        "TIME 1P: Hit SPACE the moment it says 'FIRE!'",
        "TIME 2P: P1 hit S/P2 hit K the moment it says 'FIRE!'",
        "MASH 1P: Continuously hit SPACE while it says 'MASH!'",
        "MASH 2P: Continuously P1 hit S/P2 hit K while it says 'MASH!'"
        ]
        while self.running:
            mx, my = pygame.mouse.get_pos()

            gungame.event_getter(self)
            screen.blit(self.background, (0, 0))
            gungame.animations(self)

            if self.game_mode == None:
                if mashmode_button.collidepoint((mx, my)):
                    if self.click:
                        self.game_mode = "mashmode"
                        self.click = False
                elif timemode_button.collidepoint((mx, my)):
                    if self.click:
                        self.game_mode = "timemode"
                        self.click = False
                elif info_button.collidepoint((mx, my)):
                    if self.click:
                        self.game_mode = "infomode"
                        self.click = False
                info_button = screen.blit(self.game_info, (15, 15))
                mashmode_button = screen.blit(self.game_mashmode, game_mashmode_rect)
                timemode_button = screen.blit(self.game_timemode, game_timemode_rect)
            elif self.game_mode != "infomode":
                back_button = screen.blit(self.game_back, (15, 15))
                if back_button.collidepoint((mx, my)):
                    if self.click:
                        self.game_mode = None
                        self.click = False
                game_1button = screen.blit(self.game_1player, game_1player_rect)
                game_2button = screen.blit(self.game_2player, game_2player_rect)
                if game_1button.collidepoint((mx, my)):
                    self.player_mode = 1
                    if self.click:
                        if self.game_mode == "timemode":
                            pygame.mixer.music.load("Mexican Standoff.mp3")
                            pygame.mixer.music.play(-1, 0, 3000)
                            gungame.one_won_juan(self)
                        else:
                            pygame.mixer.music.load("Mexican Standoff.mp3")
                            pygame.mixer.music.play(-1, 0, 3000)
                            gungame.one_guna_juan(self)
                elif game_2button.collidepoint((mx, my)):
                    self.player_mode = 2
                    if self.click:
                        if self.game_mode == "timemode":
                            pygame.mixer.music.load("Mexican Standoff.mp3")
                            pygame.mixer.music.play(-1, 0, 3000)
                            gungame.one_won_one(self)
                        else:
                            pygame.mixer.music.load("Mexican Standoff.mp3")
                            pygame.mixer.music.play(-1, 0, 3000)
                            gungame.one_guna_one(self)
            else:
                back_button = screen.blit(self.game_back, (15, 15))
                if back_button.collidepoint((mx, my)):
                    if self.click:
                        self.game_mode = None
                        self.click = False
                if self.game_mode == "infomode":
                    for info_num in range(len(info_list)):
                        info_text = info_font.render(info_list[info_num], True, (0, 0, 0))
                        info_text_rect = info_text.get_rect()
                        info_text_rect.centerx = screen.get_rect().centerx
                        info_text_rect.centery = info_num*30+150
                        screen.blit(info_text, info_text_rect)


            pygame.display.flip()
            clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    game = gungame()
    game.run()