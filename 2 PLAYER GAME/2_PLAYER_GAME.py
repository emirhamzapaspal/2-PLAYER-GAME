import pygame

class Button:
    def __init__(self,text,width,height,pos,elevation):

        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]


        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#354B5E'

        self.text_surf = gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):

        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color,self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect,border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77' 

pygame.init()

width = 1000
height = 700
font = pygame.font.SysFont("arialblack",40)
font2 = pygame.font.SysFont("arialblack",20)
game_over = False
gui_font = pygame.font.Font(None,30)
a = " "
started = False
credits = False
p1score = 0
p2score = 0

screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)

player = pygame.image.load("player.png")
player_pos = player.get_rect()
player_pos.topleft = (100,70)

button1 = Button('Start',200,40,(410,300),6)
button2 = Button('Credits',200,40,(410,400),6)
button3 = Button('Quit',200,40,(410,500),6)
button4 = Button('Exit',100,20,(800,600),6)


player2 = pygame.image.load("player2.png")
player2_pos = player.get_rect()
player2_pos.topleft = (900,550)

running = True
while running == True:

    yazi = font.render(str(a) + " PLAYER WON, Press R To Restart",True,(255,255,255))
    yazi_pos = yazi.get_rect()
    yazi_pos.topleft = (80,200)

    yazi2 = font.render("EMİR HAMZA PASPAL",True,(255,255,255))
    yazi2_pos = yazi2.get_rect()
    yazi2_pos.topleft = (300, 200)

    yazi3 = font.render("2 PLAYER GAME",True,(255,255,255))
    yazi3_pos = yazi3.get_rect()
    yazi3_pos.topleft = (320,100)

    p1scoretext = font2.render(str(p1score),True,(255,255,255))
    p1scoretext_pos = p1scoretext.get_rect()
    p1scoretext_pos.topleft = (player_pos.x + 30, player_pos.y - 20)

    p2scoretext = font2.render(str(p2score),True,(255,255,255))
    p2scoretext_pos = p2scoretext.get_rect()
    p2scoretext_pos.topleft = (player2_pos.x + 30, player2_pos.y - 20)

    p1sword = pygame.image.load("p1sword.png")
    p1sword_pos = p1sword.get_rect()
    p1sword_pos.topleft = (player_pos.x + 15, player_pos.y + 10)

    p1swordattack = pygame.image.load("p1swordattack.png")
    p1swordattack_pos = p1sword.get_rect()
    p1swordattack_pos.topleft = (player_pos.x + 20, player_pos.y + 8)

    p2sword = pygame.image.load("p2sword.png")
    p2sword_pos = p2sword.get_rect()
    p2sword_pos.topleft = (player2_pos.x - 10, player2_pos.y + 5)

    p2swordattack = pygame.image.load("p2swordattack.png")
    p2swordattack_pos = p1sword.get_rect()
    p2swordattack_pos.topleft = (player2_pos.x - 10, player2_pos.y + 5)

    screen.fill((100,100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    if started == False:
        if credits == False:
            screen.blit(yazi3, yazi3_pos)
            button1.draw()
            button2.draw()
            button3.draw()
        else:
            screen.blit(yazi2, yazi2_pos)
            if button4.pressed:
                credits = False
                button2.pressed = False
        if button1.pressed:
            started = True
        if button2.pressed:
            button4.draw()
            credits = True
        if button3.pressed:
            pygame.quit()
    else:
        keys = pygame.key.get_pressed()
        if game_over == False:
            screen.blit(p1scoretext, p1scoretext_pos)
            screen.blit(p2scoretext, p2scoretext_pos)
            if keys[pygame.K_w]:
                player_pos.y -= 2
            if keys[pygame.K_s]:
                player_pos.y += 2
            if keys[pygame.K_a]:
                player_pos.x -= 2
            if keys[pygame.K_d]:
                player_pos.x += 2
            if keys[pygame.K_e]:
                screen.blit(p1swordattack, p1swordattack_pos)
                if p1swordattack_pos.colliderect(player2_pos):
                    if p1score != 10:
                        p1score += 1
                        player_pos.topleft = (100,70)
                        player2_pos.topleft = (900,550)
                    if p1score == 10:
                        game_over = True
                        a = "GREEN"

            else:
                if game_over == False:
                    screen.blit(p1sword, p1sword_pos)
            
            if keys[pygame.K_UP]:
                player2_pos.y -= 2
            if keys[pygame.K_DOWN]:
                player2_pos.y += 2
            if keys[pygame.K_LEFT]:
                player2_pos.x -= 2
            if keys[pygame.K_RIGHT]:
                player2_pos.x += 2
            if keys[pygame.K_SPACE]:
                screen.blit(p2swordattack, p2swordattack_pos)
                if p2swordattack_pos.colliderect(player_pos):
                    if p2score != 10:
                        p2score += 1
                        player_pos.topleft = (100,70)
                        player2_pos.topleft = (900,550)
                    if p2score == 10:
                        game_over = True
                        a = "RED"
            else:
                screen.blit(p2sword, p2sword_pos)
        if game_over == False:
            screen.blit(player, player_pos)
            screen.blit(player2, player2_pos)
        else:
            screen.blit(yazi,yazi_pos)
            if keys[pygame.K_r]:
                p1score = 0
                p2score = 0
                game_over = False
                player_pos.topleft = (100,70)
                player2_pos.topleft = (900,550)
    pygame.display.update()