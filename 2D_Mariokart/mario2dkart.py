# All audio and images of Mario Kart rightfully belong to Nintendo and involved companies by copyright law or something.
# Media as such has been taken for solely education purposes, I promise.
import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

class kartgame:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((960, 720))
        self.clock = pygame.time.Clock()

        self.player1x = 100
        self.player1y = 200
        self.p1x_velo = 0
        self.p1y_velo = 0
        self.p1_max = 3
        self.slowdown1x = True
        self.slowdown1y = True
        self.x1_start_ticks = 0
        self.y1_start_ticks = 0
        
        self.player2x = 150
        self.player2y = 200
        self.p2x_velo = 0
        self.p2y_velo = 0
        self.p2_max = 3
        self.slowdown2x = True
        self.slowdown2y = True
        self.x2_start_ticks = 0
        self.y2_start_ticks = 0

        self.p1_img = pygame.image.load("mario_topsprite.png")
        self.p1_img = pygame.transform.scale(self.p1_img, (30, 30))
        self.p1rot = pygame.transform.rotate(self.p1_img, 0)
        self.p2_img = pygame.image.load("luigi_topsprite.png")
        self.p2_img = pygame.transform.scale(self.p2_img, (30, 30))
        self.p2rot= pygame.transform.rotate(self.p2_img, 0)

        self.p1_kart = pygame.Rect((self.player1x, self.player1y, 30, 30))
        self.p1_laps = 0
        self.p1_finish = False
        self.p2_kart = pygame.Rect((self.player2x, self.player2y, 30, 30))
        self.p2_laps = 0
        self.p2_finish = False
        self.kart_collide = False

        self.red_colour = 255
        self.green_colour = 0
        self.blue_colour = 0
        self.red_green = False
        self.green_blue = False
        self.blue_red = False
        self.rainbow_colour = [255, 255, 255]

        self.font = pygame.font.SysFont(None, 30)
        self.ready = False
        self.running = True

    def event_getter(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_SPACE:
                    self.ready = True
            elif event.type == pygame.QUIT:
                self.running = False

    def karts(self) -> None:
        p1new_rect = self.p1rot.get_rect(center = self.p1_img.get_rect(center = (self.player1x+15, self.player1y+15)).center)
        p2new_rect = self.p2rot.get_rect(center = self.p2_img.get_rect(center = (self.player2x+15, self.player2y+15)).center)
        self.player1x += self.p1x_velo
        self.player1y += self.p1y_velo
        self.player2x += self.p2x_velo
        self.player2y += self.p2y_velo
        self.screen.blit(self.p1rot, p1new_rect)
        self.screen.blit(self.p2rot, p2new_rect)
        self.p1_kart = pygame.Rect((self.player1x, self.player1y, 30, 30))
        self.p2_kart = pygame.Rect((self.player2x, self.player2y, 30, 30))
        self.kart_collide = pygame.Rect.colliderect(self.p1_kart, self.p2_kart)

        keys = pygame.key.get_pressed()
        if not self.p1_finish:
            if keys[pygame.K_w]:
                    if self.p1y_velo > -self.p1_max:
                        self.p1y_velo -= 0.1
                    else:
                        self.p1y_velo = -self.p1_max
                    self.p1y_velo = round(self.p1y_velo, 2)
                    self.slowdown1y = False
            if keys[pygame.K_s]:
                    if self.p1y_velo < self.p1_max:
                        self.p1y_velo += 0.1
                    else:
                        self.p1y_velo = self.p1_max
                    self.p1y_velo = round(self.p1y_velo, 2)
                    self.slowdown1y = False
            if keys[pygame.K_a]:
                    if self.p1x_velo > -self.p1_max:
                        self.p1x_velo -= 0.1
                    else:
                        self.p1x_velo = -self.p1_max
                    self.p1x_velo = round(self.p1x_velo, 2)
                    self.slowdown1x = False
            if keys[pygame.K_d]:
                if self.p1x_velo < self.p1_max:
                    self.p1x_velo += 0.1
                else:
                    self.p1x_velo = self.p1_max
                self.p1x_velo = round(self.p1x_velo, 2)
                self.slowdown1x = False
        if not self.p2_finish:
            if keys[pygame.K_UP]:
                    if self.p2y_velo > -self.p2_max:
                        self.p2y_velo -= 0.1
                    else:
                        self.p2y_velo = -self.p2_max
                    self.p2y_velo = round(self.p2y_velo, 2)
                    self.slowdown2y = False
            if keys[pygame.K_DOWN]:
                    if self.p2y_velo < self.p2_max:
                        self.p2y_velo += 0.1
                    else:
                        self.p2y_velo = self.p2_max
                    self.p2y_velo = round(self.p2y_velo, 2)
                    self.slowdown2y = False
            if keys[pygame.K_LEFT]:
                    if self.p2x_velo > -self.p2_max:
                        self.p2x_velo -= 0.1
                    else:
                        self.p2x_velo = -self.p2_max
                    self.p2x_velo = round(self.p2x_velo, 2)
                    self.slowdown2x = False
            if keys[pygame.K_RIGHT]:
                if self.p2x_velo < self.p2_max:
                    self.p2x_velo += 0.1
                else:
                    self.p2x_velo = self.p2_max
                self.p2x_velo = round(self.p2x_velo, 2)
                self.slowdown2x = False

        if not keys[pygame.K_w] and not keys[pygame.K_s] or self.p1_finish:
            if not self.slowdown1y:
                self.slowdown1y = True
                self.y1_start_ticks = pygame.time.get_ticks()
            y1_seconds = (pygame.time.get_ticks() - self.y1_start_ticks)/1000
            if y1_seconds > 1:
                self.p1y_velo = 0
            if self.p1y_velo > 0:
                self.p1y_velo -= 0.05
                self.p1y_velo = round(self.p1y_velo, 2)
            elif self.p1y_velo < 0:
                self.p1y_velo += 0.05
                self.p1y_velo = round(self.p1y_velo, 2)
        if not keys[pygame.K_a] and not keys[pygame.K_d] or self.p1_finish:
            if not self.slowdown1x:
                self.slowdown1x = True
                self.x1_start_ticks = pygame.time.get_ticks()
            x1_seconds = (pygame.time.get_ticks() - self.x1_start_ticks)/1000
            if x1_seconds > 1:
                self.p1x_velo = 0
            if self.p1x_velo > 0:
                self.p1x_velo -= 0.05
                self.p1x_velo = round(self.p1x_velo, 2)
            elif self.p1x_velo < 0:
                self.p1x_velo += 0.05
                self.p1x_velo = round(self.p1x_velo, 2)
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] or self.p2_finish:
            if not self.slowdown2y:
                self.slowdown2y = True
                self.y2_start_ticks = pygame.time.get_ticks()
            y2_seconds = (pygame.time.get_ticks() - self.y2_start_ticks)/1000
            if y2_seconds > 1:
                self.p2y_velo = 0
            if self.p2y_velo > 0:
                self.p2y_velo -= 0.05
                self.p2y_velo = round(self.p2y_velo, 2)
            elif self.p2y_velo < 0:
                self.p2y_velo += 0.05
                self.p2y_velo = round(self.p2y_velo, 2)
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] or self.p2_finish:
            if not self.slowdown2x:
                self.slowdown2x = True
                self.x2_start_ticks = pygame.time.get_ticks()
            x2_seconds = (pygame.time.get_ticks() - self.x2_start_ticks)/1000
            if x2_seconds > 1:
                self.p2x_velo = 0
            if self.p2x_velo > 0:
                self.p2x_velo -= 0.05
                self.p2x_velo = round(self.p2x_velo, 2)
            elif self.p2x_velo < 0:
                self.p2x_velo += 0.05
                self.p2x_velo = round(self.p2x_velo, 2)

        if self.p1y_velo != 0 or self.p1x_velo != 0:
            if self.p1x_velo > self.p1y_velo and self.p1x_velo > 0 and self.p1y_velo > -1 and self.p1y_velo < 1:
                self.p1rot = pygame.transform.rotate(self.p1_img, 270)
            if self.p1x_velo < self.p1y_velo and self.p1x_velo < 0 and self.p1y_velo > -1 and self.p1y_velo < 1:
                self.p1rot = pygame.transform.rotate(self.p1_img, 90)
            if self.p1y_velo < self.p1x_velo and self.p1y_velo < 0 and self.p1x_velo > -1 and self.p1x_velo < 1:
                self.p1rot = pygame.transform.rotate(self.p1_img, 0)
            if self.p1y_velo > self.p1x_velo and self.p1y_velo > 0 and self.p1x_velo > -1 and self.p1x_velo < 1:
                self.p1rot = pygame.transform.rotate(self.p1_img, 180)
            if self.p1y_velo >= self.p1_max/3*2 and self.p1x_velo <= self.p1_max/3 and self.p1x_velo >= -self.p1_max/3:
                self.p1rot= pygame.transform.rotate(self.p1_img, 180)
                p1new_rect = self.p1rot.get_rect(center = self.p1_img.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1y_velo <= -self.p1_max/3*2 and self.p1x_velo <= self.p1_max/3 and self.p1x_velo >= -self.p1_max/3:
                self.p1rot= pygame.transform.rotate(self.p1_img, 0)
                p1new_rect = self.p1rot.get_rect(center = self.p1_img.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1x_velo >= self.p1_max/3*2 and self.p1y_velo <= self.p1_max/3 and self.p1y_velo >= -self.p1_max/3:
                self.p1rot= pygame.transform.rotate(self.p1_img, 270)
                p1new_rect = self.p1rot.get_rect(center = self.p1_img.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1x_velo <= -self.p1_max/3 and self.p1y_velo <= self.p1_max/3 and self.p1y_velo >= -self.p1_max/3:
                self.p1rot= pygame.transform.rotate(self.p1_img, 90)
                p1new_rect = self.p1rot.get_rect(center = self.p1_img.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1y_velo > self.p1_max/3 and self.p1x_velo > self.p1_max/3:
                self.p1rot= pygame.transform.rotate(self.p1_img, 225)
                p1new_rect = self.p1rot.get_rect(center = self.p1_img.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1y_velo < -self.p1_max/3 and self.p1x_velo < -self.p1_max/3:
                self.p1rot= pygame.transform.rotate(self.p1_img, 45)
                p1new_rect = self.p1rot.get_rect(center = self.p1_img.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1y_velo < -self.p1_max/3 and self.p1x_velo > self.p1_max/3:
                self.p1rot= pygame.transform.rotate(self.p1_img, 315)
                p1new_rect = self.p1rot.get_rect(center = self.p1_img.get_rect(center = (self.player1x+15, self.player1y+15)).center)
            elif self.p1y_velo > self.p1_max/3 and self.p1x_velo < -self.p1_max/3:
                self.p1rot= pygame.transform.rotate(self.p1_img, 135)
                p1new_rect = self.p1rot.get_rect(center = self.p1_img.get_rect(center = (self.player1x+15, self.player1y+15)).center)
        if self.p2y_velo != 0 or self.p2x_velo != 0:
            if self.p2x_velo > self.p2y_velo and self.p2x_velo > 0 and self.p2y_velo > -1 and self.p2y_velo < 1:
                self.p2rot = pygame.transform.rotate(self.p2_img, 270)
            if self.p2x_velo < self.p2y_velo and self.p2x_velo < 0 and self.p2y_velo > -1 and self.p2y_velo < 1:
                self.p2rot = pygame.transform.rotate(self.p2_img, 90)
            if self.p2y_velo < self.p2x_velo and self.p2y_velo < 0 and self.p2x_velo > -1 and self.p2x_velo < 1:
                self.p2rot = pygame.transform.rotate(self.p2_img, 0)
            if self.p2y_velo > self.p2x_velo and self.p2y_velo > 0 and self.p2x_velo > -1 and self.p2x_velo < 1:
                self.p2rot = pygame.transform.rotate(self.p2_img, 180)
            if self.p2y_velo >= self.p2_max/3*2 and self.p2x_velo <= self.p2_max/3 and self.p2x_velo >= -self.p2_max/3:
                self.p2rot= pygame.transform.rotate(self.p2_img, 180)
                p2new_rect = self.p2rot.get_rect(center = self.p2_img.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2y_velo <= -self.p2_max/3 and self.p2x_velo <= self.p2_max/3 and self.p2x_velo >= -self.p2_max/3:
                self.p2rot= pygame.transform.rotate(self.p2_img, 0)
                p2new_rect = self.p2rot.get_rect(center = self.p2_img.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2x_velo >= self.p2_max/3*2 and self.p2y_velo <= self.p2_max/3 and self.p2y_velo >= -self.p2_max/3:
                self.p2rot= pygame.transform.rotate(self.p2_img, 270)
                p2new_rect = self.p2rot.get_rect(center = self.p2_img.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2x_velo <= -self.p2_max/3*2 and self.p2y_velo <= self.p2_max/3 and self.p2y_velo >= -self.p2_max/3:
                self.p2rot= pygame.transform.rotate(self.p2_img, 90)
                p2new_rect = self.p2rot.get_rect(center = self.p2_img.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2y_velo > self.p2_max/3 and self.p2x_velo > self.p2_max/3:
                self.p2rot= pygame.transform.rotate(self.p2_img, 225)
                p2new_rect = self.p2rot.get_rect(center = self.p2_img.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2y_velo < -self.p2_max/3 and self.p2x_velo < -self.p2_max/3:
                self.p2rot= pygame.transform.rotate(self.p2_img, 45)
                p2new_rect = self.p2rot.get_rect(center = self.p2_img.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2y_velo < -self.p2_max/3 and self.p2x_velo > self.p2_max/3:
                self.p2rot= pygame.transform.rotate(self.p2_img, 315)
                p2new_rect = self.p2rot.get_rect(center = self.p2_img.get_rect(center = (self.player2x+15, self.player2y+15)).center)
            elif self.p2y_velo > self.p2_max/3 and self.p2x_velo < -self.p2_max/3:
                self.p2rot= pygame.transform.rotate(self.p2_img, 135)
                p2new_rect = self.p2rot.get_rect(center = self.p2_img.get_rect(center = (self.player2x+15, self.player2y+15)).center)
        
        if self.player1x <= 0:
            self.player1x = 0
            self.p1x_velo = -self.p1x_velo
        if self.player1x >= 930:
            self.player1x = 930
            self.p1x_velo = -self.p1x_velo
        if self.player1y <= 0:
            self.player1y = 0
            self.p1y_velo = -self.p1y_velo
        if self.player1y >= 690:
            self.player1y = 690
            self.p1y_velo = -self.p1y_velo
        if self.player2x <= 0:
            self.player2x = 0
            self.p2x_velo = -self.p2x_velo
        if self.player2x >= 930:
            self.player2x = 930
            self.p2x_velo = -self.p2x_velo
        if self.player2y <= 0:
            self.player2y = 0
            self.p2y_velo = -self.p2y_velo
        if self.player2y >= 690:
            self.player2y = 690
            self.p2y_velo = -self.p2y_velo

        if self.kart_collide:
            self.x1_start_ticks = pygame.time.get_ticks()
            self.y1_start_ticks = pygame.time.get_ticks()
            self.x2_start_ticks = pygame.time.get_ticks()
            self.y2_start_ticks = pygame.time.get_ticks()
            if self.p1x_velo > self.p2_max:
                self.p1x_velo = self.p2_max
            if self.p1y_velo > self.p2_max:
                self.p1y_velo = self.p2_max
            if self.p2x_velo > self.p1_max:
                self.p2x_velo = self.p1_max
            if self.p2y_velo > self.p1_max:
                self.p2y_velo = self.p1_max
            switch1x = self.p1x_velo
            switch1y = self.p1y_velo
            switch2x = self.p2x_velo
            switch2y = self.p2y_velo
            if self.p1x_velo > 0:
                switch1x = self.p1x_velo + 0.1
            elif self.p1x_velo < 0:
                switch1x = self.p1x_velo - 0.1
            if self.p2x_velo > 0:
                switch2x = self.p2x_velo + 0.1
            elif self.p2x_velo < 0:
                switch2x = self.p2x_velo - 0.1
            if self.p1y_velo > 0:
                switch1y = self.p1y_velo + 0.1
            if self.p1y_velo < 0:
                switch1y = self.p1y_velo - 0.1
            if self.p2y_velo > 0:
                switch2y = self.p2y_velo + 0.1
            if self.p2y_velo < 0:
                switch2y = self.p2y_velo - 0.1
            self.p1x_velo = switch2x
            self.p1y_velo = switch2y
            self.p2x_velo = switch1x
            self.p2y_velo = switch1y

    def colour_change(self) -> None:
        if self.red_colour == 255 and self.green_colour == 0 and self.blue_colour == 0:
            self.red_green = True
            self.green_blue = False
            self.blue_red = False
        if self.red_colour == 0 and self.green_colour == 255 and self.blue_colour == 0:
            self.red_green = False
            self.green_blue = True
            self.blue_red = False
        if self.red_colour == 0 and self.green_colour == 0 and self.blue_colour == 255:
            self.red_green = False
            self.green_blue = False
            self.blue_red = True

        if self.red_green:
            self.red_colour -= 5
            self.green_colour += 5
        elif self.green_blue:
            self.green_colour -= 5
            self.blue_colour += 5
        elif self.blue_red:
            self.blue_colour -= 5
            self.red_colour += 5

        self.rainbow_colour = [self.red_colour, self.green_colour, self.blue_colour]

    def waluigitrack(self) -> None:
        p1_route = ["startpoint"]
        p2_route = ["startpoint"]
        checker_x = 10
        p1_time = 0
        p2_time = 0
        p1_text = self.font.render(f"P1: {p1_time}", True, (178, 0, 0))
        p2_text = self.font.render(f"P2: {p2_time}", True, (178, 0, 0))
        p1_text_rect = p1_text.get_rect()
        p1_text_rect.right = 940
        p2_text_rect = p1_text.get_rect()
        p2_text_rect.right = 940
        p2_text_rect.top = 20
        self.running = True
        while self.running:
            kartgame.event_getter(self)

            self.screen.fill((128, 0, 128))

            pygame.draw.rect(self.screen, (50, 50, 50), (50, 50, 240, 620), 90)
            pygame.draw.rect(self.screen, (128, 0, 128), (200, 50, 90, 620))
            pygame.draw.circle(self.screen, (50, 50, 50), (680, 490), 180, 90)
            pygame.draw.rect(self.screen, (128, 0, 128), (500, 310, 180, 360))
            pygame.draw.rect(self.screen, (178, 178, 0), (200, 580, 480, 90))
            pygame.draw.rect(self.screen, (50, 50, 50), (480, 310, 200, 90))
            pygame.draw.ellipse(self.screen, (50, 50, 50), (430, 50, 260, 260), 90)
            pygame.draw.rect(self.screen, (128, 0, 128), (430, 50, 130, 260))
            pygame.draw.rect(self.screen, (50, 50, 50), (480, 220, 90, 90))
            pygame.draw.rect(self.screen, (50, 50, 50), (200, 50, 360, 90))
            wall_1 = pygame.draw.rect(self.screen, (0, 178, 178), (180, 180, 260, 360), 10)
            wall_2 = pygame.draw.rect(self.screen, (0, 178, 178), (430, 450, 260, 90), 10)
            wall_3 = pygame.draw.rect(self.screen, (0, 178, 178), (430, 180, 140, 10))
            start = pygame.draw.rect(self.screen, (0, 0, 0), (0, 340, 180, 10))
            for i in range(9):
                checker_x = 10
                checker_x += i*20
                pygame.draw.rect(self.screen, (255, 255, 255), (checker_x, 340, 10, 10))

            checkpoint_1 = pygame.Rect(475, 0, 10, 180)
            checkpoint_2 = pygame.Rect(475, 540, 10, 180)


            p1_center = round(self.player1x+15), round(self.player1y+15)
            p2_center = round(self.player2x+15), round(self.player2y+15)
            p1_colour = self.screen.get_at(p1_center)[:3]
            p2_colour = self.screen.get_at(p2_center)[:3]
            if p1_colour == (128, 0, 128):
                self.p1_max = 1.5
            elif p1_colour == (178, 178, 0):
                self.p1_max = 6
            else:
                self.p1_max = 3
            if p2_colour == (128, 0, 128):
                self.p2_max = 1.5
            elif p2_colour == (178, 178, 0):
                self.p2_max = 6
            else:
                self.p2_max = 3


            if self.p1_kart.colliderect(start):
                if p1_route[0] == "checkpoint2":
                    self.p1_laps += 1
                p1_route = []
                p1_route.append("startpoint")
            if self.p1_kart.colliderect(checkpoint_1):
                if p1_route[0] == "startpoint" or p1_route[0] == "checkpoint1":
                    p1_route = []
                    p1_route.append("checkpoint1")
                else:
                    p1_route = []
            if self.p1_kart.colliderect(checkpoint_2):
                if p1_route[0] == "checkpoint1" or p1_route[0] == "checkpoint2":
                    p1_route = []
                    p1_route.append("checkpoint2")
                else:
                    p1_route = []
                    p1_route.append("startpoint")
            if self.p2_kart.colliderect(start):
                if p2_route[0] == "checkpoint2":
                    self.p2_laps += 1
                p2_route = []
                p2_route.append("startpoint")
            if self.p2_kart.colliderect(checkpoint_1):
                if p2_route[0] == "startpoint" or p2_route[0] == "checkpoint1":
                    p2_route = []
                    p2_route.append("checkpoint1")
                else:
                    p2_route = []
            if self.p2_kart.colliderect(checkpoint_2):
                if p2_route[0] == "checkpoint1" or p2_route[0] == "checkpoint2":
                    p2_route = []
                    p2_route.append("checkpoint2")
                else:
                    p2_route = []
                    p2_route.append("startpoint")

            if self.p1_kart.colliderect(wall_1):
                if self.player1x + 15 >= wall_1[0] + wall_1[2]:
                    self.player1x = wall_1[0] + wall_1[2]
                    self.p1x_velo = -self.p1x_velo
                elif self.player1x + 15 <= wall_1[0]:
                    self.player1x = wall_1[0] - 30
                    self.p1x_velo = -self.p1x_velo
                if self.player1y + 15 >= wall_1[1] + wall_1[3]:
                    self.player1y = wall_1[1] + wall_1[3]
                    self.p1y_velo = -self.p1y_velo
                elif self.player1y + 15 <= wall_1[1]:
                    self.player1y = wall_1[1] - 30
                    self.p1y_velo = -self.p1y_velo
            if self.p1_kart.colliderect(wall_2):
                if self.player1x + 15 >= wall_2[0] + wall_2[2]:
                    self.player1x = wall_2[0] + wall_2[2]
                    self.p1x_velo = -self.p1x_velo
                elif self.player1x + 15 <= wall_2[0]:
                    self.player1x = wall_2[0] - 30
                    self.p1x_velo = -self.p1x_velo
                if self.player1y + 15 >= wall_2[1] + wall_2[3]:
                    self.player1y = wall_2[1] + wall_2[3]
                    self.p1y_velo = -self.p1y_velo
                elif self.player1y + 15 <= wall_2[1]:
                    self.player1y = wall_2[1] - 30
                    self.p1y_velo = -self.p1y_velo
            if self.p1_kart.colliderect(wall_3):
                if self.player1x + 15 >= wall_3[0] + wall_3[2]:
                    self.player1x = wall_3[0] + wall_3[2]
                    self.p1x_velo = -self.p1x_velo
                elif self.player1x + 15 <= wall_3[0]:
                    self.player1x = wall_3[0] - 30
                    self.p1x_velo = -self.p1x_velo
                if self.player1y + 15 >= wall_3[1] + wall_3[3]:
                    self.player1y = wall_3[1] + wall_3[3]
                    self.p1y_velo = -self.p1y_velo
                elif self.player1y + 15 <= wall_3[1]:
                    self.player1y = wall_3[1] - 30
                    self.p1y_velo = -self.p1y_velo
            if self.p2_kart.colliderect(wall_1):
                if self.player2x + 15 >= wall_1[0] + wall_1[2]:
                    self.player2x = wall_1[0] + wall_1[2]
                    self.p2x_velo = -self.p2x_velo
                if self.player2x + 15 <= wall_1[0]:
                    self.player2x = wall_1[0] - 30
                    self.p2x_velo = -self.p2x_velo
                if self.player2y + 15 >= wall_1[1] + wall_1[3]:
                    self.player2y = wall_1[1] + wall_1[3]
                    self.p2y_velo = -self.p2y_velo
                if self.player2y + 15 <= wall_1[1]:
                    self.player2y = wall_1[1] - 30
                    self.p2y_velo = -self.p2y_velo
            if self.p2_kart.colliderect(wall_2):
                if self.player2x + 15 >= wall_2[0] + wall_2[2]:
                    self.player2x = wall_2[0] + wall_2[2]
                    self.p2x_velo = -self.p2x_velo
                if self.player2x + 15 <= wall_2[0]:
                    self.player2x = wall_2[0] - 30
                    self.p2x_velo = -self.p2x_velo
                if self.player2y + 15 >= wall_2[1] + wall_2[3]:
                    self.player2y = wall_2[1] + wall_2[3]
                    self.p2y_velo = -self.p2y_velo
                if self.player2y + 15 <= wall_2[1]:
                    self.player2y = wall_2[1] - 30
                    self.p2y_velo = -self.p2y_velo
            if self.p2_kart.colliderect(wall_3):
                if self.player2x + 15 >= wall_3[0] + wall_3[2]:
                    self.player2x = wall_3[0] + wall_3[2]
                    self.p2x_velo = -self.p2x_velo
                if self.player2x + 15 <= wall_3[0]:
                    self.player2x = wall_3[0] - 30
                    self.p2x_velo = -self.p2x_velo
                if self.player2y + 15 >= wall_3[1] + wall_3[3]:
                    self.player2y = wall_3[1] + wall_3[3]
                    self.p2y_velo = -self.p2y_velo
                if self.player2y + 15 <= wall_3[1]:
                    self.player2y = wall_3[1] - 30
                    self.p2y_velo = -self.p2y_velo

            if self.p1_laps == 3:
                if not self.p1_finish:
                    self.p1_finish = True
                    p1_time = pygame.time.get_ticks()/1000
                p1_text = self.font.render(f"P1: {p1_time}", True, (178, 0, 0))
                p1_text_rect = p1_text.get_rect()
                p1_text_rect.right = 940
                self.screen.blit(p1_text, p1_text_rect)
            if self.p2_laps == 3:
                if not self.p2_finish:
                    self.p2_finish = True
                    p2_time = pygame.time.get_ticks()/1000
                p2_text = self.font.render(f"P2: {p2_time}", True, (178, 0, 0))
                p2_text_rect = p2_text.get_rect()
                p2_text_rect.right = 940
                p2_text_rect.top = 20
                self.screen.blit(p2_text, p2_text_rect)

            kartgame.karts(self)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def rainbowtrack(self) -> None:
        p1_route = ["startpoint"]
        p2_route = ["startpoint"]
        self.p1_max = 4.5
        self.p2_max = 4.5
        checker_x = 25
        p1_time = 0
        p2_time = 0
        p1_text = self.font.render(f"P1: {p1_time}", True, (178, 0, 0))
        p2_text = self.font.render(f"P2: {p2_time}", True, (178, 0, 0))
        p1_text_rect = p1_text.get_rect()
        p1_text_rect.right = 940
        p2_text_rect = p1_text.get_rect()
        p2_text_rect.right = 940
        p2_text_rect.top = 20
        self.running = True
        while self.running:
            kartgame.event_getter(self)
            kartgame.colour_change(self)

            self.screen.fill((0, 0, 0))

            pygame.draw.rect(self.screen, self.rainbow_colour, (15, 105, 90, 510))
            pygame.draw.circle(self.screen, self.rainbow_colour, (105, 105), 90)
            pygame.draw.rect(self.screen, (0, 0, 0), (105, 105, 90, 90))
            pygame.draw.rect(self.screen, self.rainbow_colour, (105, 15, 555, 90))
            pygame.draw.circle(self.screen, self.rainbow_colour, (670, 105), 90)
            pygame.draw.rect(self.screen, (0, 0, 0), (570, 105, 90, 90))
            pygame.draw.rect(self.screen, self.rainbow_colour, (660, 105, 100, 150))
            pygame.draw.circle(self.screen, self.rainbow_colour, (660, 255), 100)
            pygame.draw.rect(self.screen, (0, 0, 0), (560, 155, 100, 200))
            pygame.draw.rect(self.screen, self.rainbow_colour, (380, 265, 280, 90))
            pygame.draw.ellipse(self.screen, self.rainbow_colour, (270, 265, 220, 240), 90)
            pygame.draw.rect(self.screen, (0, 0, 0), (380, 355, 110, 150))
            pygame.draw.rect(self.screen, self.rainbow_colour, (380, 415, 425, 90))
            pygame.draw.circle(self.screen, self.rainbow_colour, (105, 605), 90)
            pygame.draw.rect(self.screen, (0, 0, 0), (105, 515, 90, 90))
            pygame.draw.rect(self.screen, self.rainbow_colour, (105, 605, 700, 90))
            pygame.draw.ellipse(self.screen, self.rainbow_colour, (695, 415, 220, 280), 90)
            pygame.draw.ellipse(self.screen, self.rainbow_colour, (695, 415, 220, 280), 90)
            pygame.draw.rect(self.screen, (0, 0, 0), (695, 505, 110, 100))
            start = pygame.draw.rect(self.screen, (178, 0, 0), (15, 340, 90, 10))
            for i in range(4):
                checker_x = 25
                checker_x += i*20
                pygame.draw.rect(self.screen, (255, 255, 255), (checker_x, 340, 10, 10))

            checkpoint_1 = pygame.Rect(475, 0, 10, 180)
            checkpoint_2 = pygame.Rect(475, 540, 10, 180)

            p1_center = round(self.player1x+15), round(self.player1y+15)
            p2_center = round(self.player2x+15), round(self.player2y+15)
            p1_colour = self.screen.get_at(p1_center)[:3]
            p2_colour = self.screen.get_at(p2_center)[:3]
            if p1_colour == (0, 0, 0):
                p1_route = ["starpoint"]
                if self.player2x <= 45:
                    self.player1x = 75
                else:
                    self.player1x = 15
                self.player1y = 360
                self.p1x_velo = 0
                self.p1y_velo = 0
            if p2_colour == (0, 0, 0):
                p2_route = ["startpoint"]
                if self.player1x >= 45:
                    self.player2x = 15
                else:
                    self.player2x = 75
                self.player2y = 360
                self.p2x_velo = 0
                self.p2y_velo = 0


            if self.p1_kart.colliderect(start):
                if p1_route[0] == "checkpoint2":
                    self.p1_laps += 1
                p1_route = []
                p1_route.append("startpoint")
            if self.p1_kart.colliderect(checkpoint_1):
                if p1_route[0] == "startpoint" or p1_route[0] == "checkpoint1":
                    p1_route = []
                    p1_route.append("checkpoint1")
                else:
                    p1_route = []
            if self.p1_kart.colliderect(checkpoint_2):
                if p1_route[0] == "checkpoint1" or p1_route[0] == "checkpoint2":
                    p1_route = []
                    p1_route.append("checkpoint2")
                else:
                    p1_route = []
                    p1_route.append("startpoint")
            if self.p2_kart.colliderect(start):
                if p2_route[0] == "checkpoint2":
                    self.p2_laps += 1
                p2_route = []
                p2_route.append("startpoint")
            if self.p2_kart.colliderect(checkpoint_1):
                if p2_route[0] == "startpoint" or p2_route[0] == "checkpoint1":
                    p2_route = []
                    p2_route.append("checkpoint1")
                else:
                    p2_route = []
            if self.p2_kart.colliderect(checkpoint_2):
                if p2_route[0] == "checkpoint1" or p2_route[0] == "checkpoint2":
                    p2_route = []
                    p2_route.append("checkpoint2")
                else:
                    p2_route = []
                    p2_route.append("startpoint")

            if self.p1_laps == 3:
                if not self.p1_finish:
                    self.p1_finish = True
                    p1_time = pygame.time.get_ticks()/1000
                p1_text = self.font.render(f"P1: {p1_time}", True, (178, 0, 0))
                p1_text_rect = p1_text.get_rect()
                p1_text_rect.right = 940
                self.screen.blit(p1_text, p1_text_rect)
            if self.p2_laps == 3:
                if not self.p2_finish:
                    self.p2_finish = True
                    p2_time = pygame.time.get_ticks()/1000
                p2_text = self.font.render(f"P2: {p2_time}", True, (178, 0, 0))
                p2_text_rect = p2_text.get_rect()
                p2_text_rect.right = 940
                p2_text_rect.top = 20
                self.screen.blit(p2_text, p2_text_rect)

            kartgame.karts(self)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def mariotrack(self) -> None:
        p1_route = ["startpoint"]
        p2_route = ["startpoint"]
        checker_x = 10
        p1_time = 0
        p2_time = 0
        p1_text = self.font.render(f"P1: {p1_time}", True, (178, 0, 0))
        p2_text = self.font.render(f"P2: {p2_time}", True, (178, 0, 0))
        p1_text_rect = p1_text.get_rect()
        p1_text_rect.right = 940
        p2_text_rect = p1_text.get_rect()
        p2_text_rect.right = 940
        p2_text_rect.top = 20
        self.running = True
        while self.running:
            kartgame.event_getter(self)

            self.screen.fill((0, 178, 0))

            pygame.draw.rect(self.screen, (50, 50, 50), (50, 50, 860, 620), 90)
            walls = pygame.draw.rect(self.screen, (178, 0, 0), (180, 180, 600, 360), 20)
            start = pygame.draw.rect(self.screen, (0, 0, 0), (0, 340, 180, 10))
            for i in range(9):
                checker_x = 10
                checker_x += i*20
                pygame.draw.rect(self.screen, (255, 255, 255), (checker_x, 340, 10, 10))

            checkpoint_1 = pygame.Rect(475, 0, 10, 180)
            checkpoint_2 = pygame.Rect(475, 540, 10, 180)

            p1_center = round(self.player1x+15), round(self.player1y+15)
            p2_center = round(self.player2x+15), round(self.player2y+15)
            p1_colour = self.screen.get_at(p1_center)[:3]
            p2_colour = self.screen.get_at(p2_center)[:3]
            if p1_colour == (0, 178, 0):
                self.p1_max = 1.5
            else:
                self.p1_max = 3
            if p2_colour == (0, 178, 0):
                self.p2_max = 1.5
            else:
                self.p2_max = 3

            
            if self.p1_kart.colliderect(start):
                if p1_route[0] == "checkpoint2":
                    self.p1_laps += 1
                p1_route = []
                p1_route.append("startpoint")
            if self.p1_kart.colliderect(checkpoint_1):
                if p1_route[0] == "startpoint" or p1_route[0] == "checkpoint1":
                    p1_route = []
                    p1_route.append("checkpoint1")
                else:
                    p1_route = []
            if self.p1_kart.colliderect(checkpoint_2):
                if p1_route[0] == "checkpoint1" or p1_route[0] == "checkpoint2":
                    p1_route = []
                    p1_route.append("checkpoint2")
                else:
                    p1_route = []
                    p1_route.append("startpoint")
            if self.p2_kart.colliderect(start):
                if p2_route[0] == "checkpoint2":
                    self.p2_laps += 1
                p2_route = []
                p2_route.append("startpoint")
            if self.p2_kart.colliderect(checkpoint_1):
                if p2_route[0] == "startpoint" or p2_route[0] == "checkpoint1":
                    p2_route = []
                    p2_route.append("checkpoint1")
                else:
                    p2_route = []
            if self.p2_kart.colliderect(checkpoint_2):
                if p2_route[0] == "checkpoint1" or p2_route[0] == "checkpoint2":
                    p2_route = []
                    p2_route.append("checkpoint2")
                else:
                    p2_route = []
                    p2_route.append("startpoint")
            
            if self.p1_kart.colliderect(walls):
                if self.player1x + 15 >= walls[0] + walls[2]:
                    self.player1x = walls[0] + walls[2]
                    self.p1x_velo = -self.p1x_velo
                elif self.player1x + 15 <= walls[0]:
                    self.player1x = walls[0] - 30
                    self.p1x_velo = -self.p1x_velo
                if self.player1y + 15 >= walls[1] + walls[3]:
                    self.player1y = walls[1] + walls[3]
                    self.p1y_velo = -self.p1y_velo
                elif self.player1y + 15 <= walls[1]:
                    self.player1y = walls[1] - 30
                    self.p1y_velo = -self.p1y_velo
            if self.p2_kart.colliderect(walls):
                if self.player2x + 15 >= walls[0] + walls[2]:
                    self.player2x = walls[0] + walls[2]
                    self.p2x_velo = -self.p2x_velo
                if self.player2x + 15 <= walls[0]:
                    self.player2x = walls[0] - 30
                    self.p2x_velo = -self.p2x_velo
                if self.player2y + 15 >= walls[1] + walls[3]:
                    self.player2y = walls[1] + walls[3]
                    self.p2y_velo = -self.p2y_velo
                if self.player2y + 15 <= walls[1]:
                    self.player2y = walls[1] - 30
                    self.p2y_velo = -self.p2y_velo

            if self.p1_laps == 3:
                if not self.p1_finish:
                    self.p1_finish = True
                    p1_time = pygame.time.get_ticks()/1000
                p1_text = self.font.render(f"P1: {p1_time}", True, (178, 0, 0))
                p1_text_rect = p1_text.get_rect()
                p1_text_rect.right = 940
                self.screen.blit(p1_text, p1_text_rect)
            if self.p2_laps == 3:
                if not self.p2_finish:
                    self.p2_finish = True
                    p2_time = pygame.time.get_ticks()/1000
                p2_text = self.font.render(f"P2: {p2_time}", True, (178, 0, 0))
                p2_text_rect = p2_text.get_rect()
                p2_text_rect.right = 940
                p2_text_rect.top = 20
                self.screen.blit(p2_text, p2_text_rect)

        
            kartgame.karts(self)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def run(self) -> None:
        track = None
        self.running = True
        textline1 = self.font.render("It's a kart game, 3 laps around the course.", True, (255, 255, 255))
        textline1_rect = textline1.get_rect()
        textline1_rect.centerx = 480
        textline1_rect.centery = 315
        textline2 = self.font.render("Whoever completes it faster wins!", True, (255, 0, 0))
        textline3 = self.font.render("WASD for Mario, Arrow Keys for Luigi. Click SPACE to start.", True, (255, 255, 255))
        textline3_rect = textline3.get_rect()
        textline3_rect.centerx = 480
        textline3_rect.centery = 405
        while self.running:
            kartgame.event_getter(self)
            self.screen.blit(textline1, textline1_rect)
            self.screen.blit(textline2, (textline2.get_rect(center = self.screen.get_rect().center)))
            self.screen.blit(textline3, textline3_rect)
            if self.ready:
                self.running = False
                track = random.randrange(0, 3)

            pygame.display.flip()
            self.clock.tick(60)
        print(track)
        if track == 0:
            pygame.mixer.music.load("Waluigi Pinball - Mario Kart DS - Super Smash Bros. Ultimate.mp3")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            self.player1x = 110
            self.player1y = 360
            self.player2x = 50
            self.player2y = 360
            kartgame.waluigitrack(self)
        elif track == 1:
            pygame.mixer.music.load("SNES music Super Mario Kart  - Rainbow Road.mp3")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            self.player1x = 15
            self.player1y = 360
            self.player2x = 75
            self.player2y = 360
            kartgame.rainbowtrack(self)
        elif track == 2:
            pygame.mixer.music.load("Super Mario Kart Music (SNES) - Mario Circuit.mp3")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            self.player1x = 110
            self.player1y = 360
            self.player2x = 50
            self.player2y = 360
            kartgame.mariotrack(self)

if __name__ == "__main__":
    game = kartgame()
    game.run()