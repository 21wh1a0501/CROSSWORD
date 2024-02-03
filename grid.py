import pygame
import sys
from root import *
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
#background
BG = pygame.image.load("back_1.png")
#to set font
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("cswd_text.otf", size)
#to draw crossword
def draw_board(screen, puzzle, squaresize):
    r = len(puzzle)
    c = len(puzzle[0])
    for i in range(r):
        for j in range(c):
            if puzzle[i][j] == '*':
                pygame.draw.rect(screen, BLACK, (j * squaresize, i * squaresize, squaresize, squaresize))
            else:
                pygame.draw.rect(screen, WHITE, (j * squaresize, i * squaresize, squaresize, squaresize), 1)
            pygame.draw.rect(screen, BLACK, (j * squaresize, i * squaresize, squaresize, squaresize), 1)
            font = pygame.font.SysFont('Arial', 20)
            text = font.render(puzzle[i][j], True, BLACK)
            text_rect = text.get_rect(center=(j * squaresize + squaresize // 2, i * squaresize + squaresize // 2))
            screen.blit(text, text_rect)
#to prompt rows and columns
def ask(SCREEN, prompt1, prompt2):
    """Ask the user for the number of rows and columns and return them as integers."""
    font = pygame.font.SysFont('Arial', 60)
    row_answer = ""
    column_answer = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if row_answer and column_answer:
                        return int(row_answer), int(column_answer)
                elif event.key == pygame.K_BACKSPACE:
                    if column_answer:
                        column_answer = column_answer[:-1]
                    elif row_answer:
                        row_answer = row_answer[:-1]
                elif event.unicode.isdigit():
                    if not row_answer:
                        row_answer += event.unicode
                    else:
                        column_answer += event.unicode
        SCREEN.blit(BG, (0, 0))
        row_prompt = font.render(prompt1 + " " + row_answer, True, "#cd5c5c")
        SCREEN.blit(row_prompt, (200, 200))
        column_prompt = font.render(prompt2 + " " + column_answer, True, "#cd5c5c")
        SCREEN.blit(column_prompt, (200, 300))
        pygame.display.update()


def draw_clues(screen, across_clues, down_clues):
    font = pygame.font.SysFont('Arial', 35)
    clue_color = (178,34,34)
    text_color = BLACK
    x1_offset = 900
    y1_offset = 50
    x_offset = 700
    y_offset = 50
    clue_spacing = 50
    #for across
    text_across = get_font(35).render("Across", True, "#008080")
    across_rect = text_across.get_rect(center=(700, 20))
    screen.blit(text_across, across_rect)
    for i, (clue_number, clue_text) in enumerate(across_clues):
        clue_label = '{}. '.format(clue_number)
        clue_text_label = font.render(clue_label, True, clue_color)
        clue_text_label_rect = clue_text_label.get_rect()
        clue_text_label_rect.topleft = (x_offset, y_offset + i * clue_spacing)
        screen.blit(clue_text_label, clue_text_label_rect)
        text_label = font.render(clue_text, True, text_color)
        text_label_rect = text_label.get_rect()
        text_label_rect.topleft = (clue_text_label_rect.right, clue_text_label_rect.top)
        screen.blit(text_label, text_label_rect)
    #for down
    text_down = get_font(35).render("Down", True, "#008080")
    down_rect = text_down.get_rect(center=(900, 20))
    screen.blit(text_down, down_rect)
    for i, (clue_number, clue_text) in enumerate(down_clues):
        clue_label = '{}.'.format(clue_number)
        clue_text_label = font.render(clue_label, True, clue_color)
        clue_text_label_rect = clue_text_label.get_rect()
        clue_text_label_rect.topleft = (x1_offset, y1_offset + i * clue_spacing)
        screen.blit(clue_text_label, clue_text_label_rect)
        text_label = font.render(clue_text, True, text_color)
        text_label_rect = text_label.get_rect()
        text_label_rect.topleft = (clue_text_label_rect.right, clue_text_label_rect.top)
        screen.blit(text_label, text_label_rect)

    pygame.display.flip()


def get_puzzle_from_user(SCREEN):
    """Prompt the user to enter the puzzle and return it as a list of strings."""
    # Get number of rows and columns from user
    rows, columns = ask(SCREEN, "Enter the number of rows: ", "Enter the number of columns: ")

    puzzle = []
    BG = pygame.image.load("back_2.png")

    input_box_width = 400
    input_box_height = 50
    input_box_margin = 10
    input_box_x = 150
    input_box_y = 100

    # Create a text input box for each row
    input_boxes = []
    for i in range(int(rows)):
        rect = pygame.Rect(input_box_x, input_box_y + i * (input_box_height + input_box_margin), input_box_width, input_box_height)
        input_boxes.append(rect)

    # Handle user input for each row
    row_inputs = ['' for _ in range(int(rows))]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for i, box in enumerate(input_boxes):
                    if box.collidepoint(pygame.mouse.get_pos()):
                        if event.key == pygame.K_BACKSPACE:
                            row_inputs[i] = row_inputs[i][:-1]
                        elif len(row_inputs[i]) < int(columns) and (event.unicode.isalpha() or event.unicode == "*"):
                            row_inputs[i] += event.unicode
                if event.key == pygame.K_RETURN:
                    puzzle = row_inputs.copy()
                    break

        # Draw the text input boxes and user input for each row
        SCREEN.blit(BG, (0, 0))
        font = pygame.font.SysFont('Arial', 40)
        prompt = font.render("ENTER THE CROSSWORD", True, "#191970")
        SCREEN.blit(prompt, (400, 20))
        for i, box in enumerate(input_boxes):
            pygame.draw.rect(SCREEN, WHITE, box, 2)
            font = pygame.font.SysFont('Arial', 40)
            input_text = font.render(row_inputs[i], True, "#b22222")
            SCREEN.blit(input_text, (box.x + 5, box.y + 5))
            prompt = font.render("Row %d:  " % (i + 1), True, "#191970")
            SCREEN.blit(prompt, (input_box_x - 100, box.y + 5))

        pygame.display.update()

        if puzzle:
            break

    return puzzle




def main():
    # Initialize pygame
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    BG = pygame.image.load("back_2.png")

    # Set title of screen
    pygame.display.set_caption("Crossword Puzzle")

    # Load the puzzle from a file
    puzzle_input = get_puzzle_from_user(screen)

    # Parse the puzzle input into a 2D list
    puzzle = puzzle_input

    # Get the dimensions of the puzzle
    r = len(puzzle)
    c = len(puzzle[0])

    # Copy the matrix and number the squares
    copy = copymatrix1(r, c, puzzle)

    # Get the across and down clues
    across_clues = across1(r, c, puzzle, copy)
    down_clues = down1(r, c, puzzle, copy)

    # Set the size of the squares on the puzzle
    squaresize = min(400 // r, 400 // c)

    # Loop until the user clicks the close button
    done = False
    clock = pygame.time.Clock()
    # Initialize the selected square to the upper left corner
    selected_row = 0
    selected_col = 0

    # Initialize the user input string
    user_input = ''

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_row = max(selected_row - 1, 0)
                elif event.key == pygame.K_DOWN:
                    selected_row = min(selected_row + 1, r - 1)
                elif event.key == pygame.K_LEFT:
                    selected_col = max(selected_col - 1, 0)
                elif event.key == pygame.K_RIGHT:
                    selected_col = min(selected_col + 1, c - 1)
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.unicode.isalpha() and len(user_input) < 20:
                    user_input += event.unicode.upper()
        # --- Game logic should go here

        # --- Drawing code should go here
        screen.blit(BG, (0, 0))
        draw_board(screen, puzzle, squaresize)
        draw_clues(screen, across_clues, down_clues)

        # Draw a highlight around the selected square
        pygame.draw.rect(screen, (255, 0, 0),
                         (selected_col * squaresize, selected_row * squaresize, squaresize, squaresize), 3)

        # Draw the user input string
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(user_input, True, BLACK)
        text_rect = text.get_rect(
            center=(selected_col * squaresize + squaresize // 2, selected_row * squaresize + squaresize // 2))
        screen.blit(text, text_rect)
        clock.tick(60)



