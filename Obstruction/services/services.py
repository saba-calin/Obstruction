from Obstruction.repository.score_repository import ScoreRepository


class Services:
    def __init__(self, repository):
        """
        This is the __init__ function
        :param repository: an object of type Repository
        """

        self.__repository = repository
        self.__score_repository = ScoreRepository()
        self.__current_player = None

    def get_board(self):
        """
        This function gets and returns the board
        :return: a matrix representing the board
        """

        return self.__repository.get_board()

    def play_computer_move(self, symbol):
        """
        This function plays the most favourable move for the computer
        :param symbol: a char representing the symbol corresponding to the computer
        :return: the coordinates of the cell in which the computer placed its symbol
        """

        best_score = -0x3f3f3f3f
        x = None
        y = None

        for i in range(6):
            for j in range(6):
                if self.__repository.get_cell(i, j) == " ":
                    self.__repository.place_symbol(i, j, "x")
                    self.block_neighbouring_cells(i, j)

                    self.__current_player = "human"
                    score = self.minimax(False, self.get_depth())

                    self.__repository.place_symbol(i, j, " ")
                    self.unblock_neighbouring_cells(i, j)

                    if score > best_score:
                        best_score = score
                        x = i
                        y = j

        self.play_move(x, y, symbol)
        return x, y

    def minimax(self, maximizing_player, depth):
        """
        This function computes the most favourable move for the computer
        :param maximizing_player: a bool representing whether the current player is maximizing of minimizing
        :param depth: an integer representing the depth at which the backtracking function will go in depth
        :return: an integer representing the outcome
        """

        if depth == 0:
            return 0
        if self.is_board_full() == True:
            if self.__current_player == "computer":
                return -1
            else:
                return 1

        if maximizing_player == True:
            max_eval = -0x3f3f3f3f
            for i in range(6):
                for j in range(6):
                    if self.__repository.get_cell(i, j) == " ":
                        self.__repository.place_symbol(i, j, "x")
                        self.block_neighbouring_cells(i, j)

                        self.__current_player = "human"
                        eval = self.minimax(False, depth - 1)

                        self.__repository.place_symbol(i, j, " ")
                        self.unblock_neighbouring_cells(i, j)
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = 0x3f3f3f3f
            for i in range(6):
                for j in range(6):
                    if self.__repository.get_cell(i, j) == " ":
                        self.__repository.place_symbol(i, j, "o")
                        self.block_neighbouring_cells(i, j)

                        self.__current_player = "computer"
                        eval = self.minimax(True, depth - 1)

                        self.__repository.place_symbol(i, j, " ")
                        self.unblock_neighbouring_cells(i, j)
                        min_eval = min(min_eval, eval)
            return min_eval

    def get_number_of_empty_cells(self):
        """
        This function computes and returns the number of empty cells on the board
        :return: an integer representing the number of empty cells
        """

        cnt = 0
        for i in range(6):
            for j in range(6):
                if self.__repository.get_cell(i, j) == " ":
                    cnt += 1
        return cnt

    def get_depth(self):
        """
        This function computes and returns the depth at which the backtracking function will do in depth
        :return: an integer representing the depth at which the backtracking function will go in depth
        """

        cells = self.get_number_of_empty_cells()
        if cells > 20:
            return 2
        elif cells > 16:
            return 3
        else:
            return 100

    def play_move(self, x, y, symbol):
        """
        This function play a move by placing a symbol inside a cell and blocking all the neighbouring cells
        :param x: an integer representing the x coordinate
        :param y: an integer representing the y coordinate
        :param symbol: a char representing the symbol that will be placed inside a cell
        :return: None
        """

        self.__repository.place_symbol(x, y, symbol)
        self.block_neighbouring_cells(x, y)

    def block_neighbouring_cells(self, x, y):
        """
        This function blocks all the cells (sets them to "-") that are in the immediate vicinity of a given cell
        :param x: an integer representing the x coordinate
        :param y: an integer representing the y coordinate
        :return: None
        """

        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [1, 1, 0, -1, -1, -1, 0, 1]

        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if self.is_in_board(new_x, new_y) == True and self.__repository.get_cell(new_x, new_y) == " ":
                self.__repository.place_symbol(new_x, new_y, "-")

    def unblock_neighbouring_cells(self, x, y):
        """
        This function unblocks all the cells (sets them to " ") that are in the immediate vicinity of a given cell
        :param x: an integer representing the x coordinate
        :param y: an integer representing the y coordinate
        :return: None
        """

        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [1, 1, 0, -1, -1, -1, 0, 1]

        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if self.is_in_board(new_x, new_y) == True and self.__repository.get_cell(new_x, new_y) == "-":
                self.__repository.place_symbol(new_x, new_y, " ")

        for i in range(6):
            for j in range(6):
                if self.__repository.get_cell(i, j) == "o" or self.__repository.get_cell(i, j) == "x":
                    self.block_neighbouring_cells(i, j)

    def is_empty_cell(self, x, y):
        """
        This function checks whether a cell is empty
        :param x: an integer representing the x coordinate
        :param y: an integer representing the y coordinate
        :return: True if the cell is empty (equal to " ") and False otherwise
        """

        return self.__repository.get_cell(x, y) == " "

    def is_board_full(self):
        """
        This function checks whether the board is full
        :return: True if the board is full and False otherwise
        """

        board = self.__repository.get_board()
        for i in range(6):
            for j in range(6):
                if board[i][j] == " " or board[i][j] == "h" or board[i][j] == "t":
                    return False
        return True

    def get_human_score(self):
        """
        This function gets and returns the score of the human
        :return: an integer representing the score of the human
        """

        return self.__score_repository.get_human_score()

    def get_computer_score(self):
        """
        This function gets and returns the score of the computer
        :return: an integer representing the score of the computer
        """

        return self.__score_repository.get_computer_score()

    def increment_human_score(self):
        """
        This function increments the score of the human
        :return: None
        """

        self.__score_repository.increment_human_score()

    def increment_computer_score(self):
        """
        This function increments the score of the computer
        :return: None
        """

        self.__score_repository.increment_computer_score()

    def get_cell(self, x, y):
        """
        This function returns the symbol inside a given cell
        :param x: an integer representing the x coordinate
        :param y: an integer representing the y coordinate
        :return: a char representing the symbol inside a cell
        """

        return self.__repository.get_cell(x, y)

    def place_symbol(self, x, y, symbol):
        """
        This function places a symbol in a cell
        :param x: an integer representing the x coordinate
        :param y: an integer representing the y coordinate
        :param symbol: a char representing the symbol that will be placed in a cell
        :return: None
        """

        self.__repository.place_symbol(x, y, symbol)

    @staticmethod
    def is_in_board(x, y):
        """
        This function checks whether a cell is inside the 6x6 board
        :param x: an integer representing the x coordinate
        :param y: an integer representing the y coordinate
        :return: True if both x and y are between 0 and 5 and False otherwise
        """

        return x >= 0 and y >= 0 and x < 6 and y < 6
