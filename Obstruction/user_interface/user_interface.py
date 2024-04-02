from Obstruction.services.services import Services
from Obstruction.repository.repository import Repository
from Obstruction.domain.board import Board


class UserInterface:
    def __init__(self):
        self.__game_manager = Services(Repository(Board()))

    def start(self):
        while True:
            self.__print_menu()
            option = input(">")

            try:
                if option == "y":
                    self.__print_board()
                    self.__play_human_move()
                elif option == "n":
                    self.__play_computer_move()
                elif option == "exit":
                    exit()
                elif option == "1":
                    self.__print_board()
                else:
                    raise Exception("Error: Invalid input!")
                self.__init__()

            except Exception as exception:
                print(str(exception))

    def __play_human_move(self):
        if self.__game_manager.is_board_full() == True:
            self.__print_winner("computer")
            return

        while True:
            print("")
            x = int(input("X = "))
            y = int(input("Y = "))

            if self.__game_manager.is_in_board(x, y) and self.__game_manager.is_empty_cell(x, y):
                self.__game_manager.play_move(x, y, "o")
                self.__print_board()
                self.__play_computer_move()
                break
            else:
                print("Error: Invalid coordinates!")

    def __play_computer_move(self):
        if self.__game_manager.is_board_full() == True:
            self.__print_winner("human")
            return

        x, y = self.__game_manager.play_computer_move("x")
        print("")
        print("Computer placed at coordinates ", x, y)

        self.__print_board()
        self.__play_human_move()

    def __print_winner(self, winner):
        if winner == "human":
            self.__game_manager.increment_human_score()
        else:
            self.__game_manager.increment_computer_score()

        print("")
        print("The " + winner + " has won")
        print("The score is:")
        print(self.__game_manager.get_human_score(), "for the human")
        print(self.__game_manager.get_computer_score(), "for the computer")

    @staticmethod
    def __print_menu():
        print("")
        print("Would you like to play the first move? (y/n)")
        print("Type \"exit\" to close the game.")

    def __print_board(self):
        board = self.__game_manager.get_board()
        full_line = "#########################"
        gaped_line = "# - # - # - # - # - # - #"

        print("")
        print(full_line)
        for i in range(6):
            new_line = ""
            cnt = 0
            for char in gaped_line:
                if char == '-':
                    new_line += board[i][cnt]
                    cnt += 1
                else:
                    new_line += char
            print(new_line)

            if i != 5:
                print(full_line)
        print(full_line)
