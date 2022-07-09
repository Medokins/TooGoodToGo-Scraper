import pygame

pygame.init()
WINDOW_SIZE = (1000, 1000)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ToGoodToGo - Scrapper")

# example shops list from TgtgClient
shops = [
    "Shop 0",
    "Shop 1",
    "Shop 2",
    "Shop 3",
    "Shop 4",
    "Shop 5",
    "Shop 6",
    "Shop 7",
    "Shop 8",
    "Shop 9",
    "Shop 10",
]

class Menu:
    def __init__(self, shops):
        # x and y position of mouse for buttons
        self.x = 0
        self.y = 0

        # running state
        self.running = True

        # available shops list
        self.shops = shops

        # pressable buttons
        self.buttons = []

        # chosen buttons
        self.chosen = []
        # chosen stores names
        self.chosen_stores = []

        # cooldown
        self.cooldown = 100
        self.last = pygame.time.get_ticks()

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

        if len(self.shops) <= 15:
            x_spacing = WINDOW_SIZE[0] / 2
        else:
            x_spacing = WINDOW_SIZE[0] / 4

        y_spacing = 120
        counter = 0

        for shop in self.shops:
            if shop not in self.chosen_stores:
                text_color = (3, 232, 252)
            else:
                text_color = (19, 191, 36)
        

            temp = font.render(shop, False, text_color, (26,26,26))
            tempRect = temp.get_rect()
            tempRect.center = (x_spacing, y_spacing)
            screen.blit(temp, tempRect)
            self.buttons.append(tempRect)
            y_spacing += 50
            counter += 1

            if counter == 16:
                y_spacing = 120
                x_spacing = WINDOW_SIZE[0] / 4 * 3


        offset = 8

        for text in self.buttons:
            if text in self.chosen:
                outline_color = (19, 191, 36)
            else:
                outline_color = (3, 232, 252)
            #top horizontal lines
            pygame.draw.line(screen, color = outline_color,\
                            start_pos = (text.bottomleft[0] - offset, text.topleft[1] - offset),\
                            end_pos = (text.bottomright[0] + offset, text.topleft[1] - offset))
            #bottom horizontal lines
            pygame.draw.line(screen, color = outline_color,\
                            start_pos = (text.bottomleft[0] - offset, text.bottomleft[1] + offset),\
                            end_pos = (text.bottomright[0] + offset, text.bottomleft[1] + offset))
            #left vertical lines
            pygame.draw.line(screen, color = outline_color,\
                            start_pos = (text.bottomleft[0] - offset, text.topleft[1] - offset),\
                            end_pos = (text.bottomleft[0] - offset, text.bottomleft[1] + offset))
            #right vertical lines
            pygame.draw.line(screen, color = outline_color,\
                            start_pos = (text.bottomright[0] + offset, text.topright[1] - offset),\
                            end_pos = (text.bottomright[0] + offset, text.bottomright[1] + offset))
                            
        pygame.display.update()

def runMenu(shops):
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
                        now = pygame.time.get_ticks()
                        if now - menu.last >= menu.cooldown:
                            menu.last = now
                            if button not in menu.chosen:
                                menu.chosen.append(button)
                                menu.chosen_stores.append(shops[menu.buttons.index(button)])
                            else:
                                menu.chosen.remove(button)
                                menu.chosen_stores.remove(shops[menu.buttons.index(button)])

                if menu.x > 436 and menu.x < 565 and menu.y > 932 and menu.y < 968:
                    menu.running = False
                    pygame.quit()

            try:
                menu.draw_menu()
            except:
                pass
            
    return menu.chosen_stores