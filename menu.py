import pygame

pygame.init()
WINDOW_SIZE = (1000, 1000)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ToGoodToGo - Scrapper")

# example shops list from TgtgClient
shops = [
    "ONUTS",
    "GREEN CAFFE NERO RAKOWICKA (KRK)",
    "Kawiarnia INDIVIDUAL",
    "Delecta & Olimp Axis",
    "Danone & Olimp Axis",
    "Olimp Axis",
    "PiCaffe",
    "Costa Coffee Kraków Galeria Krakowska",
    "GREEN CAFFE NERO GALERIA KRAKOWSKA (KRK)",
    "North Fish Galeria Krakowska Poziom -1",
    "Grycan",
    "Boho Cafe",
    "Starbucks Krakow Palac Wolodkowiczow",
    "Carrefour Galeria Krakowska (poziom +1)",
    "North Fish Galeria Krakowska Poziom +1",
    "Cynamon"
]

class Menu:
    def __init__(self, shops):
        # x and y position of mouse for buttons
        self.x = 0
        self.y = 0

        # running state
        self.running = True

        # continue button
        self.continue_button = False

        # available shops list
        self.shops = shops

        # pressable butons
        self.buttons = []


    def draw_menu(self):
        # set color to bg of menu
        screen.fill((26,26,26))

        # set font
        font = pygame.font.SysFont('Sans', 32)

        header = font.render('Choose Your favourite shops', False, (3, 232, 252), (26,26,26))
        continue_button = font.render('Continue', False, (3, 232, 252), (26,26,26))

        headerRect = header.get_rect()
        headerRect.center = (WINDOW_SIZE[0] / 2, 50)
        continueRect = continue_button.get_rect()
        continueRect.center = (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] - 50)

        screen.blit(header, headerRect)
        screen.blit(continue_button, continueRect)

        font = pygame.font.SysFont('Calibri', 24)
        spacing = 120
        for shop in self.shops:
            temp = font.render(shop, False, (3, 232, 252), (26,26,26))
            tempRect = temp.get_rect()
            tempRect.center = (WINDOW_SIZE[0] / 2, spacing)
            screen.blit(temp, tempRect)
            self.buttons.append(tempRect)
            spacing += 50

        offset = 8
        for text in self.buttons:
            #top horizontal lines
            pygame.draw.line(screen, color=(3, 232, 252),\
                            start_pos = (text.bottomleft[0] - offset, text.topleft[1] - offset),\
                            end_pos = (text.bottomright[0] + offset, text.topleft[1] - offset))
            #bottom horizontal lines
            pygame.draw.line(screen, color=(3, 232, 252),\
                            start_pos = (text.bottomleft[0] - offset, text.bottomleft[1] + offset),\
                            end_pos = (text.bottomright[0] + offset, text.bottomleft[1] + offset))
            #left vertical lines
            pygame.draw.line(screen, color=(3, 232, 252),\
                            start_pos = (text.bottomleft[0] - offset, text.topleft[1] - offset),\
                            end_pos = (text.bottomleft[0] - offset, text.bottomleft[1] + offset))
            #right vertical lines
            pygame.draw.line(screen, color=(3, 232, 252),\
                            start_pos = (text.bottomright[0] + offset, text.topright[1] - offset),\
                            end_pos = (text.bottomright[0] + offset, text.bottomright[1] + offset))
        pygame.display.update()

menu = Menu(shops)

while menu.running:
    menu.x, menu.y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu.running = False
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in menu.buttons:
                if menu.x > button.left and menu.x < button.right and menu.y > button.top and menu.y < button.bottom:
                    print(shops[menu.buttons.index(button)])

        try:
            menu.draw_menu()
        except:
            print("pygame.error: display Surface quit")