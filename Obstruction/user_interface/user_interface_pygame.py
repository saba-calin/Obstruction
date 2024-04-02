import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # Hiding the welcome message when starting up the game
import pygame
import time

from Obstruction.services.services import Services
from Obstruction.repository.repository import Repository
from Obstruction.domain.board import Board


class UserInterfacePygame:
    def __init__(self):
        self.__services = Services(Repository(Board()))
        self.__current_player = "human"

        pygame.init()
        pygame.font.init()
        self.__screen = None

        self.__background_color = (46, 204, 113)
        self.__line_color = (127, 140, 141)

        self.__draw_board(True)

    def start(self):
        self.__manage_start_screen()

        self.__draw_board(True)
        while True:
            if self.__current_player == "computer":
                pygame.display.update()
                self.__play_computer_move()

            pos = pygame.mouse.get_pos()
            x = pos[1] // 125
            y = pos[0] // 125
            self.__update_hover(x, y)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.__current_player == "human":
                    pos = event.pos
                    x = pos[1] // 125
                    y = pos[0] // 125
                    self.__play_human_move(x, y)

            pygame.display.update()

            if self.__services.is_board_full() == True:
                if self.__current_player == "human":
                    self.__manage_winner("computer")
                else:
                    self.__manage_winner("human")

    def __manage_start_screen(self):
        self.__init__()
        chosen = False
        yes_rect = pygame.Rect(300, 250, 100, 50)
        no_rect = pygame.Rect(300, 350, 100, 50)
        exit_rect = pygame.Rect(275, 450, 150, 50)

        while True and chosen == False:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_rect.collidepoint(event.pos) == True:
                        self.__current_player = "human"
                        chosen = True
                    elif no_rect.collidepoint(event.pos) == True:
                        self.__current_player = "computer"
                        chosen = True
                    elif exit_rect.collidepoint(event.pos) == True:
                        pygame.quit()
                        exit()

            self.__display_start_screen(yes_rect, no_rect, exit_rect)
            pygame.display.update()

    def __display_start_screen(self, yes_rect, no_rect, exit_rect):
        self.__screen.fill((155, 89, 182))
        text_color = (44, 62, 80)
        rect_color = (22, 160, 133)

        font = pygame.font.SysFont("Comic Sans MS", 30)
        welcome_text = font.render("Welcome to Obstruction!", False, text_color)
        play_text = font.render("Would you like to play first?", False, text_color)
        yes_text = font.render("Yes", False, text_color)
        no_text = font.render("No", False, text_color)
        exit_text = font.render("Exit game", False, text_color)

        pygame.draw.rect(self.__screen, rect_color, yes_rect)
        pygame.draw.rect(self.__screen, rect_color, no_rect)
        pygame.draw.rect(self.__screen, rect_color, exit_rect)

        self.__screen.blit(welcome_text, (200, 50))
        self.__screen.blit(play_text, (180, 150))
        self.__screen.blit(yes_text, (325, 250))
        self.__screen.blit(no_text, (325, 350))
        self.__screen.blit(exit_text, (280, 450))

    def __manage_end_screen(self, winner):
        chosen = False
        yes_rect = pygame.Rect(300, 400, 100, 50)
        no_rect = pygame.Rect(300, 500, 100, 50)

        while True and chosen == False:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_rect.collidepoint(event.pos) == True:
                        self.start()
                    elif no_rect.collidepoint(event.pos) == True:
                        pygame.quit()
                        exit()

            self.__display_end_screen(winner, yes_rect, no_rect)
            pygame.display.update()

    def __display_end_screen(self, winner, yes_rect, no_rect):
        self.__screen.fill((155, 89, 182))
        text_color = (44, 62, 80)
        rect_color = (22, 160, 133)

        font = pygame.font.SysFont("Comic Sans MS", 30)
        winner_text = font.render("The " + winner + " has won", False, text_color)
        score_text = font.render("The score is:", False, text_color)
        human_score = font.render(str(self.__services.get_human_score()) + " for the human",
                                  False, text_color)
        computer_score = font.render(str(self.__services.get_computer_score()) + " for the computer",
                                     False, text_color)
        play_again_text = font.render("Would you like to play again?", False, text_color)
        yes_text = font.render("Yes", False, text_color)
        no_text = font.render("No", False, text_color)

        pygame.draw.rect(self.__screen, rect_color, yes_rect)
        pygame.draw.rect(self.__screen, rect_color, no_rect)

        self.__screen.blit(winner_text, (200, 50))
        self.__screen.blit(score_text, (200, 150))
        self.__screen.blit(human_score, (200, 200))
        self.__screen.blit(computer_score, (200, 250))
        self.__screen.blit(play_again_text, (200, 350))
        self.__screen.blit(yes_text, (325, 400))
        self.__screen.blit(no_text, (325, 500))

    def __play_human_move(self, x, y):
        self.__clear_hover()

        if self.__services.is_empty_cell(x, y):
            self.__services.play_move(x, y, "o")
            self.__draw_board(False)
            self.__current_player = "computer"

    def __play_computer_move(self):
        self.__clear_hover()

        self.__services.play_computer_move("x")
        self.__draw_board(False)
        self.__current_player = "human"

    def __manage_winner(self, winner):
        if winner == "human":
            self.__services.increment_human_score()
        else:
            self.__services.increment_computer_score()

        time.sleep(2)
        self.__manage_end_screen(winner)

    def __update_hover(self, x, y):
        # Cleaning up the last update
        self.__clear_hover()

        # Updating the hover
        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [1, 1, 0, -1, -1, -1, 0, 1]
        for i in range(6):
            for j in range(6):
                for k in range(8):
                    new_x = x + dx[k]
                    new_y = y + dy[k]
                    if (self.__services.is_in_board(new_x, new_y) == True and
                            self.__services.get_cell(new_x, new_y) == " " and
                            self.__services.get_cell(x, y) == " "):
                        self.__services.place_symbol(new_x, new_y, "h")

        if self.__services.get_cell(x, y) == " ":
            self.__services.place_symbol(x, y, "t")

        # Drawing the updated board
        self.__draw_board(False)

    def __clear_hover(self):
        for i in range(6):
            for j in range(6):
                if self.__services.get_cell(i, j) == "h":
                    self.__services.place_symbol(i, j, " ")
                elif self.__services.get_cell(i, j) == "t":
                    self.__services.place_symbol(i, j, " ")

    def __draw_board(self, canInitialize):
        if canInitialize == True:
            self.__initialize_board()

        self.__screen.fill(self.__background_color)
        self.__draw_lines()
        self.__draw_shapes()

    def __initialize_board(self):
        self.__screen = pygame.display.set_mode((750, 750))  # Setting the width and height of the screen
        self.__screen.fill(self.__background_color)  # Setting the background color
        pygame.display.set_caption("Obstruction")  # Setting the caption

    def __draw_lines(self):
        pygame.draw.line(self.__screen, self.__line_color, (0, 0), (0, 750), 10)
        pygame.draw.line(self.__screen, self.__line_color, (125, 0), (125, 750), 10)
        pygame.draw.line(self.__screen, self.__line_color, (250, 0), (250, 750), 10)
        pygame.draw.line(self.__screen, self.__line_color, (375, 0), (375, 750), 10)
        pygame.draw.line(self.__screen, self.__line_color, (500, 0), (500, 750), 10)
        pygame.draw.line(self.__screen, self.__line_color, (625, 0), (625, 750), 10)
        pygame.draw.line(self.__screen, self.__line_color, (750, 0), (750, 750), 10)

        pygame.draw.line(self.__screen, self.__line_color, (0, 0), (750, 0), 10)
        pygame.draw.line(self.__screen, self.__line_color, (0, 125), (750, 125), 10)
        pygame.draw.line(self.__screen, self.__line_color, (0, 250), (750, 250), 10)
        pygame.draw.line(self.__screen, self.__line_color, (0, 375), (750, 375), 10)
        pygame.draw.line(self.__screen, self.__line_color, (0, 500), (750, 500), 10)
        pygame.draw.line(self.__screen, self.__line_color, (0, 625), (750, 625), 10)
        pygame.draw.line(self.__screen, self.__line_color, (0, 750), (750, 750), 10)

    def __draw_shapes(self):
        board = self.__services.get_board()
        for i in range(6):
            for j in range(6):
                if board[i][j] == 'o':
                    self.__draw_circle(i, j)
                elif board[i][j] == 'x':
                    self.__draw_cross(i, j)
                elif board[i][j] == "h":
                    self.__draw_hover_cell(i, j)
                elif board[i][j] == "-":
                    self.__draw_obstructed_cell(i, j)
                elif board[i][j] == "t":
                    self.__draw_temporary_symbol(i, j)

    def __draw_circle(self, i, j):
        center = (j * 125 + 125 // 2, i * 125 + 125 // 2)
        pygame.draw.circle(self.__screen, (52, 152, 219), center, 50, 10)

    def __draw_cross(self, i, j):
        start_desc = (j * 125 + 31, i * 125 + 31)
        end_desc = (j * 125 + 125 - 31, i * 125 + 125 - 31)
        pygame.draw.line(self.__screen, (231, 76, 60), start_desc, end_desc, 10)
        start_asc = (j * 125 + 31, i * 125 + 125 - 31)
        end_asc = (j * 125 + 125 - 31, i * 125 + 31)
        pygame.draw.line(self.__screen, (231, 76, 60), start_asc, end_asc, 10)

    def __draw_obstructed_cell(self, i, j):
        pygame.draw.rect(self.__screen, (44, 62, 80), (j * 125 + 5, i * 125 + 5, 120, 120))

    def __draw_hover_cell(self, i, j):
        pygame.draw.rect(self.__screen, (241, 196, 15), (j * 125 + 5, i * 125 + 5, 120, 120))

    def __draw_temporary_symbol(self, i, j):
        center = (j * 125 + 125 // 2, i * 125 + 125 // 2)
        pygame.draw.circle(self.__screen, (241, 196, 15), center, 50, 10)
