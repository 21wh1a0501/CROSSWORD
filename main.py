import pygame, sys
from button import Button
from grid import main

#intialize all imported pygame module
pygame.init()
#loading and playing sounds
pygame.mixer.init()
sound_effect = pygame.mixer.Sound('cswd_audio.mp3')
sound_effect.play()
#set volume
sound_effect.set_volume(0.5)
#to set screen dimensions
SCREEN = pygame.display.set_mode((1280, 720))
#caption and background
pygame.display.set_caption("CROSSWORD")
BG = pygame.image.load("back_1.png")
icon = pygame.image.load('cswd_icon.png')
pygame.display.set_icon(icon)

#function to set font
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("cswd_text.otf", size)

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()#to get mouse position
        BG1 = pygame.image.load("back_3.png")
        SCREEN.blit(BG1, (0, 0))
        #fill screen background with the respective color
        #render - this creates a new Surface with the specified text rendered on it.
        #options -rect  selects rectangle and current position
        OPTIONS_TEXT = get_font(45).render("INSTRUCTIONS", True, "Black")#this creates a new Surface with the specified text rendered on it.
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 50))
        OPTIONS_TEXT1 = get_font(25).render("*A crossword puzzle solver is being implemented here.", True, "Black")
        OPTIONS_RECT1 = OPTIONS_TEXT1.get_rect(center=(640, 200))
        OPTIONS_TEXT2 = get_font(25).render("*You will be asked to enter the puzzle's rows and columns.", True, "Black")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(640, 250))
        OPTIONS_TEXT3 = get_font(25).render("*Then program prompts to enter strings one at a time of column size", True, "Black")
        OPTIONS_RECT3 = OPTIONS_TEXT3.get_rect(center=(640, 300))
        OPTIONS_TEXT4 = get_font(25).render("*After each puzzle is solved, you will be prompted to continue or exit. ", True, "Black")
        OPTIONS_RECT4 = OPTIONS_TEXT4.get_rect(center=(640, 350))
        OPTIONS_TEXT5 = get_font(25).render("*If you choose to continue, you can enter a new puzzle to be solved.", True, "Black")
        OPTIONS_RECT5 = OPTIONS_TEXT5.get_rect(center=(640, 400))
        OPTIONS_TEXT6 = get_font(25).render("*If you choose to exit, the program will terminate.", True, "Black")
        OPTIONS_RECT6 = OPTIONS_TEXT6.get_rect(center=(640, 450))
        #copy contents to screen
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(OPTIONS_TEXT1, OPTIONS_RECT1)
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        SCREEN.blit(OPTIONS_TEXT3, OPTIONS_RECT3)
        SCREEN.blit(OPTIONS_TEXT4, OPTIONS_RECT4)
        SCREEN.blit(OPTIONS_TEXT5, OPTIONS_RECT5)
        SCREEN.blit(OPTIONS_TEXT6, OPTIONS_RECT6)
        #Button imported from the module button
        OPTIONS_BACK = Button(image=pygame.image.load("previous.png"), pos=(620, 560),
                              text_input="", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_BACK.update(SCREEN)#updates the screen with back button

        for event in pygame.event.get():#iterate through all events of pygame
            if event.type == pygame.QUIT:#when user clicks on quit button of window
                pygame.quit()#shut down all pygame library
                sys.exit()#terminates the interpreter
            if event.type == pygame.MOUSEBUTTONDOWN:#event representing whih button is clicked
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):#if back button is clicked
                    main_menu()#goes through the homepage

        pygame.display.update()#updates the screen

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))#set background

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("CROSSWORD", True, "#ff9033")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 200))

        PLAY_BUTTON = Button(image=pygame.image.load("play.png"), pos=(470, 480),
                             text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("question.png"), pos=(620, 480),
                                text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("delete.png"), pos=(770, 480),
                             text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:#generates three buttons on screen
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()