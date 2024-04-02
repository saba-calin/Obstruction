import unittest


from Obstruction.repository.repository import Repository
from Obstruction.repository.score_repository import ScoreRepository
from Obstruction.services.services import Services
from Obstruction.domain.board import Board


class Tests(unittest.TestCase):
    def test_get_board(self):
        """
        This function tests the get_board function
        :return: None
        """

        self.__repository = Repository(Board())
        board = self.__repository.get_board()
        self.assertEqual(board[1][1], " ")

    def test_get_cell(self):
        """
        This function tests the get_cell function
        :return: None
        """

        self.__repository = Repository(Board())
        cell = self.__repository.get_cell(1, 1)
        self.assertEqual(cell, " ")

    def test_place_symbol(self):
        """
        This function tests the place_symbol function
        :return: None
        """

        self.__repository = Repository(Board())
        self.__repository.place_symbol(1, 1, "x")
        self.assertEqual(self.__repository.get_cell(1, 1), "x")

    def test_get_human_score(self):
        """
        This function tests the get_human_score function
        :return: None
        """

        self.__score_repository = ScoreRepository()
        current_score = self.__score_repository.get_human_score()
        self.assertEqual(self.__score_repository.get_human_score(), current_score)

    def test_increment_human_score(self):
        """
        This function tests the increment_human_score function
        :return: None
        """

        self.__score_repository = ScoreRepository()
        current_score = self.__score_repository.get_human_score()
        self.__score_repository.increment_human_score()
        self.assertEqual(self.__score_repository.get_human_score(), current_score + 1)

    def test_get_computer_score(self):
        """
        This function tests the get_computer_score function
        :return: None
        """

        self.__score_repository = ScoreRepository()
        current_score = self.__score_repository.get_computer_score()
        self.assertEqual(self.__score_repository.get_computer_score(), current_score)

    def test_increment_computer_score(self):
        """
        This function tests the increment_computer_score function
        :return: None
        """

        self.__score_repository = ScoreRepository()
        current_score = self.__score_repository.get_computer_score()
        self.__score_repository.increment_computer_score()
        self.assertEqual(self.__score_repository.get_computer_score(), current_score + 1)

    def test_get_board_(self):
        """
        This function tests the get_board function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        board = self.__services.get_board()
        self.assertEqual(board[1][1], " ")

    def test_play_computer_move(self):
        """
        This function tests the play_computer_move function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.__services.play_move(1, 1, "x")
        self.__services.play_move(1, 3, "o")
        self.__services.play_move(4, 1, "x")
        self.__services.play_move(5, 5, "o")
        self.__services.play_computer_move("x")
        self.assertEqual(self.__services.get_cell(3, 4), "x")

    def test_minimax(self):
        """
        This function tests the minimax function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.assertEqual(self.__services.minimax(False, self.__services.get_depth()),
                         0)
        self.__services.play_move(1, 1, "x")
        self.__services.play_move(1, 3, "o")
        self.__services.play_move(4, 1, "x")
        self.__services.play_move(5, 5, "o")
        self.assertEqual(self.__services.minimax(False, self.__services.get_depth()), -1)

    def test_get_number_of_empty_cells(self):
        """
        This function tests the get_number_of_empty_cells function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.assertEqual(self.__services.get_number_of_empty_cells(), 36)

    def test_get_depth(self):
        """
        This function tests the get_depth function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.assertEqual(self.__services.get_depth(), 2)
        self.__services.play_move(1, 1, "x")
        self.__services.play_move(4, 4, "o")
        self.assertEqual(self.__services.get_depth(), 3)
        self.__services.play_move(3, 3, "x")
        self.assertEqual(self.__services.get_depth(), 100)

    def test_play_move(self):
        """
        This function tests the play_move function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.__services.play_move(1, 1, "x")
        self.assertEqual(self.__services.get_cell(1, 1), "x")

    def test_block_neighbouring_cells(self):
        """
        This function tests the block_neighbouring_cells function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.__services.block_neighbouring_cells(1, 1)
        self.assertEqual(self.__services.get_cell(0, 0), "-")

    def test_unblock_neighbouring_cells(self):
        """
        This function tests the unblock_neighbouring_cells function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.__services.block_neighbouring_cells(1, 1)
        self.__services.place_symbol(2, 2, "x")
        self.__services.unblock_neighbouring_cells(1, 1)
        self.assertEqual(self.__services.get_cell(0, 0), " ")

    def test_is_empty_cell(self):
        """
        This function tests the is_empty_cell function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.assertEqual(self.__services.is_empty_cell(1, 1), True)
        self.__services.play_move(1, 1, "x")
        self.assertEqual(self.__services.is_empty_cell(1, 1), False)

    def test_is_board_full(self):
        """
        This function tests the is_board_full function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.assertEqual(self.__services.is_board_full(), False)
        self.__services.play_move(1, 1, "x")
        self.__services.play_move(1, 4, "o")
        self.__services.play_move(4, 1, "x")
        self.__services.play_move(4, 4, "o")
        self.assertEqual(self.__services.is_board_full(), True)

    def test_get_human_score_(self):
        """
        This function tests the get_human_score function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        current_score = self.__services.get_human_score()
        self.assertEqual(self.__services.get_human_score(), current_score)

    def test_get_computer_score_(self):
        """
        This function tests the get_computer_score function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        current_score = self.__services.get_computer_score()
        self.assertEqual(self.__services.get_computer_score(), current_score)

    def test_increment_human_score_(self):
        """
        This function tests the increment_human_score function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        current_score = self.__services.get_human_score()
        self.__services.increment_human_score()
        self.assertEqual(self.__services.get_human_score(), current_score + 1)

    def test_increment_computer_score_(self):
        """
        This function tests the increment_computer_score function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        current_score = self.__services.get_computer_score()
        self.__services.increment_computer_score()
        self.assertEqual(self.__services.get_computer_score(), current_score + 1)

    def test_get_cell_(self):
        """
        This function tests the get_cell function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.assertEqual(self.__services.get_cell(1, 1), " ")

    def test_place_symbol_(self):
        """
        This function tests the place_symbol function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.__services.place_symbol(1, 1, "x")
        self.assertEqual(self.__services.get_cell(1, 1), "x")

    def test_is_in_board(self):
        """
        This function tests the is_in_board function
        :return: None
        """

        self.__services = Services(Repository(Board()))
        self.assertEqual(self.__services.is_in_board(1, 1), True)
        self.assertEqual(self.__services.is_in_board(6, 6), False)
