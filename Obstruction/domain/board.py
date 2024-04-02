class Board:
    def __init__(self):
        """
        This is the __init__ function
        """

        self.__board = [[" " for _ in range(6)] for __ in range(6)]

    def get_board(self):
        """
        This function returns the board at the current state
        :return: a matrix representing the board
        """

        return self.__board

    def get_cell(self, x, y):
        """
        This function gets and returns the symbol of a specific cell
        :param x: an integer representing the x coordinate
        :param y: an integer representing the y coordinate
        :return: a char representing the symbol of the cell
        """

        return self.__board[x][y]

    def place_symbol(self, x, y, symbol):
        """
        This function places a symbol in a desired cell
        :param x: an integer representing the x coordinate
        :param y: an integer representing the y coordinate
        :param symbol: a char representing the symbol that will be placed inside the cell
        :return: None
        """

        self.__board[x][y] = symbol
