class ScoreRepository:
    def __init__(self):
        """
        This is the __init__ function
        """

        self.__path = "../repository/score.txt"

    def get_human_score(self):
        """
        This function gets and returns the score from the file
        :return: an integer representing the score of the human
        """

        f = open(self.__path, "r")
        lines = f.readlines()
        f.close()
        return int(lines[0])

    def increment_human_score(self):
        """
        This function increments the score saved to a file of the human
        :return: None
        """

        f = open(self.__path, "r")
        lines = f.readlines()
        f.close()

        human_score = int(lines[0])
        computer_score = int(lines[1])
        human_score += 1

        f = open(self.__path, "w")
        f.write(str(human_score) + "\n")
        f.write(str(computer_score))
        f.close()

    def get_computer_score(self):
        """
        This function gets and returns the score from the file
        :return: an integer representing the score of the computer
        """

        f = open(self.__path, "r")
        lines = f.readlines()
        f.close()
        return int(lines[1])

    def increment_computer_score(self):
        """
        This function increments the score saved to a file of the computer
        :return: None
        """

        f = open(self.__path, "r")
        lines = f.readlines()
        f.close()

        human_score = int(lines[0])
        computer_score = int(lines[1])
        computer_score += 1

        f = open(self.__path, "w")
        f.write(str(human_score) + "\n")
        f.write(str(computer_score))
        f.close()
