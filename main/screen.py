import pygame
import config
import player

class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH,config.SCREEN_HEIGHT))
        self.smallfont = pygame.font.SysFont("comicsansms",25)
        self.medfont = pygame.font.SysFont("comicsansms",50)
        self.largefont = pygame.font.SysFont("comicsansms",85)
        self.player = player.Player()


    def menu_menu(self):
        self.message_to_screen("Owl Survivor",config.BLACK,-150,size = "large")
        self.button("Play",525,450,150,75,(255,0,255),(255,255,0),"play")



    def text_object(self,text,color,size = "small"):
        if size == "small":
            textSurface = self.smallfont.render(text,True, color)
        if size == "medium":
            textSurface = self.medfont.render(text,True,color)
        if size == "large":
            textSurface = self.largefont.render(text,True,color)

        return textSurface, textSurface.get_rect()

    def text_to_button(self,msg,color,b_x,b_y,b_w,b_h,size = "small"):
        textSurf,textRect = self.text_object(msg,color,size)
        textRect.center = ((b_x + (b_w/2)),b_y+(b_h/2))
        self.screen.blit(textSurf,textRect)

    def message_to_screen(self,msg,color,y_displace = 0, size ="small"):
        textSurf,textRect = self.text_object(msg,color,size)
        textRect.center = (int(config.SCREEN_WIDTH/2),int(config.SCREEN_HEIGHT/2)+y_displace)
        self.screen.blit(textSurf,textRect)

    def button(self,text, x, y, width, height, inactive_color, active_color, action = None):
            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            if x + width > cur[0] > x and y + height > cur[1] > y:
                pygame.draw.rect(self.screen, active_color,(x,y,width,height))
                if click [0] == 1 and action != None:
                    if action == "quit":
                        pygame.quit()
                    if action == "controls":
                        self.game_controls()
                    if action == "play":
                        config.PLAY = True

                    if action == "main":
                        self.menu_menu()
            else:
                pygame.draw.rect(self.screen, inactive_color,(x,y,width,height))

            self.text_to_button(text,config.BLACK,x,y,width,height)

    def update(self):
        self.screen.fill(config.BLUE)
        # self.menu()
        pygame.display.update()