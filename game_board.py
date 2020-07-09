from random import choice, randint
from functions import *
from time import sleep


class GameBoard:
    TIE_POSITION = {"X", "O"}

    def __init__(self, user1_name=None, user2_name=None, size=3):
        """
        Gets an existing board or creating a new one,
        gets the size of new board, default is 3,
        gets two users of the game
        :param user1_name: represents the name of the first user
        :type user1_name: str
        :param user2_name: represents the name of the second user
        :type user2_name: str
        :param size: size of board
        :type size: int
        """

        if user1_name is None:
            self._user1 = {"name": "user1", "symbol": "X", "score": 0, "start": True}
        else:
            self._user1 = {"name": user1_name, "symbol": "X", "score": 0, "start": True}

        if user2_name is None:
            self._user2 = {"name": "user1", "symbol": "O", "score": 0, "start": False}
        else:
            self._user2 = {"name": user2_name, "symbol": "O", "score": 0, "start": False}

        self._size = size
        self._board = [[' '] * self._size for i in range(self._size)]
        self._left_moves = self._size ** 2

    # get functions:
    def get_board(self):
        """
        Return the list that represents the game
        :return: list of the game
        :rtype: list
        """
        return self._board

    def get_left_moves(self):
        """
        :return: the left moves
        :rtype: int
        """
        return self._left_moves

    def get_scores(self):
        """
        :return: list of 2 - first is user1 score and second is user2 score
        :rtype: list
        """
        return [self._user1["score"], self._user2["score"]]

    def get_user1(self):
        """
        :return: user1
        :rtype: dict
        """
        return self._user1

    def get_user2(self):
        """
        :return: user2
        :rtype: dict
        """
        return self._user2

    def get_size(self):
        """
        :return: the board's size
        :rtype: int
        """
        return self._size

    def get_users(self):
        """
        :return: list that consists of the 2 users of the game(users are dictionaries)
        :rtype: list
        """
        return [self._user1, self._user2]

    def get_starting_player(self):
        """
        :return: the user that started the current game
        :rtype: dict
        """
        if self._user1["start"]:
            return self._user1
        return self._user2

    def get_empty_positions_coordination_list(self):
        """
        :return: a list of of the coordination(coordination is list of row and column)
                 of all the empty cells in the board
        :rtype: list
        """
        empty_cells = []
        for row_index, row in enumerate(self._board):
            for column_index, cell in enumerate(row):
                if cell == ' ':
                    empty_cells.append([row_index, column_index])

        return empty_cells

    def get_columns(self):
        """
        Returns the columns
        :return: list which represents the columns of the board
        :rtype: list
        """
        list_length = self._size
        columns = []
        for n in range(list_length):
            column = []
            for row in self._board:
                column.append(row[n])
            columns.append(column)

        return columns

    def get_diagonals(self):
        """
        Returns the diagonals
        :return: list which represents the diagonals of the board
        :rtype: list
        """
        diagonal1 = []
        diagonal2 = []
        list_length = self._size - 1
        board = self._board
        for increasing_number, row in enumerate(board):
            diagonal1.append(row[increasing_number])
            diagonal2.append(row[list_length - increasing_number])

        return [diagonal1, diagonal2]

    def show_board(self):
        """
        :return: a string that represents the board visually
        :rtype: str
        """

        s = ""
        for i, row in enumerate(self._board):
            if i == self._size:
                s += "| " + "| ".join(row) + "|"
                return s
            s += "| " + "| ".join(row) + "|\n" + "-" * (self._size * 3 + 1) + "\n"

        return s

    def describe_board(self):
        """
        This function return a string that can show a user what are the numbers he can use to mark the board
        :return: a string that shows a board with the numbers of each cell
        :rtype: str
        """
        s = ""
        board = [list(map(lambda x: x + self._size*i, [1, 2, 3])) for i in range(self._size)]
        for i, row in enumerate(board):
            if i == self._size:
                s += "| " + "| ".join(map(str, row)) + "|"
                return s
            s += "| " + "| ".join(map(str, row)) + "|\n" + "-" * (self._size * 3 + 1) + "\n"

        return s

    def set_user1_start(self):
        """
        Sets user1 to be the starting player
        :return: None
        """
        self._user1["start"] = True
        self._user2["start"] = False

    def set_user2_start(self):
        """
        sets user2 to be the starting player
        :return: None
        """
        self._user2["start"] = True
        self._user1["start"] = False

    def set_starter(self, user):
        """
        Gets a user and make him the starter, unless he already is
        :param user: the user needed to be changed
        :type user: dict
        :return: None
        """
        if self._user1 == user:
            self.set_user1_start()

        if self._user2 == user:
            self.set_user2_start()

    def set_random_starter(self):
        """
        Pick a user randomly and sets him as the starting user of the board
        :return: None
        """
        starter = choice([self._user1, self._user2])
        self.set_starter(starter)

    def switch_user(self, user):
        """
        Gets a current user and returns the other user in the game
        :param user: the current user
        :type user: dict
        :return: the other user
        :rtype: dict
        """
        if user == self.get_user1():
            return self._user2

        return self._user1

    def start_game(self):
        """
        Picks a random user to start, and prints the string that represents the board.
        The function prints out these steps for the user
        :return: None
        """
        self.set_random_starter()
        print("I am randomly choosing who starts")
        sleep(1)
        print(self.get_starting_player()["name"], "starts!")
        sleep(1)
        print(self.show_board())

    def restart_game(self):
        """
        Cleans the board, and start a new game using the function 'start_game'
        :return: None
        """
        self.clean_board()
        self.start_game()

    # Marking the board
    def mark_board_cell(self, row_index, column_index, user):
        """
        Marks the board with the user's decision and decrease the left moves by one
        :param row_index: the row_index of the coordination that the user wants to mark
        :type row_index: int
        :param column_index: the column_index of the coordination that the user wants to mark
        :type column_index: int
        :param user: the user that makes the move
        :type user: dict
        :return: None
        """
        self._board[row_index][column_index] = user["symbol"]
        self._left_moves -= 1

    def remove_board_cell(self, row_index, column_index):
        """
        marks a cell to ' ' - an empty cell, and increase the left moves by one
        :param row_index: the row_index of the coordination that wanted to be removed
        :type row_index: int
        :param column_index: the column_index of the coordination that wanted to be removed
        :type column_index: int
        :return: None
        """
        self._board[row_index][column_index] = ' '
        self._left_moves += 1

    def clean_board(self):
        """
        brings the board to a clean position - all cells equal to ' ' and left_moves to 9
        :return: None
        """
        for row_index, row in enumerate(self._board):
            for column_index, cell in enumerate(row):
                if cell != ' ':
                    self.remove_board_cell(row_index, column_index)

    # Validations and conversions
    def convert_position_to_row_and_column(self, position):
        """
        Gets a position on the board(1-9)
        Return a list of 2 parameters - 0: row, 1: column of the game_board's position
        :param position: A desired position in the game_board
        :type position: int
        :return: a list of 2 parameters - 0: row, 1: column of the game_board's position
        :rtype: list
        """
        board_length = self.get_size()
        row = int((position - 1) // board_length)
        column = int((position - 1) % board_length)

        return [row, column]

    def convert_position_to_value(self, position):
        """
        Return the value of the position in the game_board's board
        :param position: the desired position to mark
        :type position: int
        :return: the value of the game_board board's position
        :rtype: str
        """
        coordination = self.convert_position_to_row_and_column(position)
        row = coordination[0]
        column = coordination[1]

        return self.get_board()[row][column]

    def valid_number(self, position):
        """
        Checks if the number is valid for use,
        if it's an integer, between 1-9 and not already occupied on board
        :param position: the inputted number from the user
        :type position: str or int
        :return: True if the number is valid, False otherwise
        :rtype: bool
        """
        # Validates it is an integer
        if isinstance(position, str):
            position = position.strip()
            # Validate it's int
            if not position.isdigit():
                print("The position is not an integer, try again")
                return False

        # Validate it's in the board's range
        position = int(position)
        if not 10 > position > 0:
            print("The position is not in range, try again")
            return False

        # Validates the position isn't occupied
        position_value = self.convert_position_to_value(position)
        if position_value != ' ':
            print("Board is occupied, try again")
            return False

        return True

    # Board status checks - winner / tie / game over
    def is_winner(self, user):
        """
        Checks if a given user won the game
        which can happen if in one of the rows, columns, diagonals,
        occupied with 3 of his symbol
        :param user: the user we want to check whether he won or not
        :type user: dict
        :return: True if he won, False otherwise
        :rtype: bool
        """

        # rows check:
        for row in self._board:
            if set(row) == {user["symbol"]}:
                return True

        # columns check
        for column in self.get_columns():
            if set(column) == {user["symbol"]}:
                return True

        # diagonals check
        diagonals = self.get_diagonals()
        for diagonal in diagonals:
            if set(diagonal) == {user["symbol"]}:
                return True

        return False

    def is_tie(self):
        """
        checks if the game is a tie
        A tie is when both users have less left moves, than must moves to win
        (if a user has more left moves than must moves, game is not tie)
        :return: True if the game is tied, False otherwise
        :rtype: bool
        """
        for user in self.get_users():
            if user["start"]:
                user_left_moves = self._left_moves // 2 + self._left_moves % 2
            else:
                user_left_moves = self._left_moves // 2

            # Checks if there is not a tie in the rows
            for row in self._board:
                if {user["symbol"], ' '} == set(row) or {' '} == set(row):
                    if user_left_moves >= len(list(filter(lambda x: x == ' ', row))):
                        return False

            # Checks if there is not a tie in the columns
            for column in self.get_columns():
                if {user["symbol"], ' '} == set(column) or {' '} == set(column):
                    if user_left_moves >= len(list(filter(lambda x: x == ' ', column))):
                        return False

            # Checks if there is not a tie in the diagonals
            for diagonal in self.get_diagonals():
                if {user["symbol"], ' '} == set(diagonal) or {' '} == set(diagonal):
                    if user_left_moves >= len(list(filter(lambda x: x == ' ', diagonal))):
                        return False

        return True

    def game_over_for_user(self, user):
        """
        Tells us if the game is over due to a tie or a win
        :param user: the user to check whether he won
        :type user: dict
        :return: True if the game is over + corresponding message, False otherwise
        :rtype: bool
        """
        # Checks if there is a winner
        if self.is_winner(user):
            print(user["name"], " won !")
            if user == self._user1:
                self._user1["score"] += 2
            else:
                self._user2["score"] += 2

            return True

        # Checks if there is a tie
        if self.is_tie():
            print("It seems like a tie game !")
            for user in self.get_users():
                user["score"] += 1
            return True

        return False

    # user / computer moves
    def user_move(self, user, position):
        """
        Makes the move of the player:
        * gets a valid number
        * update the board
        * show the board
        * run checks if the game is over
        * return True if the game isn't over
        :param position: the desired position to mark
        :type position: str
        :param user: the user that made the move
        :type user: dict
        :return: True if the game should continue, False otherwise
        :rtype: bool
        """
        coordination = self.convert_position_to_row_and_column(int(position))
        self.mark_board_cell(coordination[0], coordination[1], user)
        print(self.show_board())

        # checks the board status if it is needed
        if self.get_left_moves() <= 4:
            if self.game_over_for_user(user):
                return False

        return True

    def computer_move(self, user):
        """
        Makes a move for the computer
        :param user: the user of the computer
        :type user: dict
        :return: True if the game should continue, False otherwise
        :rtype: bool
        """
        print("Computer's move!")

        # if it is the first move of the game
        if self.get_left_moves() == 9:
            position = randint(1, 9)
            coordination = self.convert_position_to_row_and_column(position)
            self.mark_board_cell(coordination[0], coordination[1], user)
            print(self.show_board())
            return True

        else:
            # Gets from minimax the best move that minimax chose
            coordination = self.minimax(user)
            # if he gets a win for sure he will print it
            if coordination[2] == 1:
                print("I think you are going to lose")
                sleep(0.5)
            self.mark_board_cell(coordination[0], coordination[1], user)
            sleep(0.5)
            print(self.show_board())

            # checks the board status if it is needed
            if self.get_left_moves() <= 4:
                if self.game_over_for_user(user):
                    return False

            return True

    # functions for Minimax algorithm
    def check_game_is_over(self):
        """
        checks the board's status - if there is a win or a tie
        :return: True if one of the users won or the game is a tie, False otherwise
        :rtype: bool
        """
        if self.get_left_moves() > 4:
            return False

        for user in self.get_users():
            if self.is_winner(user):
                return True

        if self.is_tie():
            return True

        return False

    def evaluate(self):
        """
        This function assumes that the game is over,
        and checks if the computer won or the user won
        :return: 1 if  the computer won, -1 if the user won, 0 if non of them won (should be a tie)
        :rtype: int
        """
        for user in self.get_users():
            if self.is_winner(user):
                if user["name"] == "Computer":
                    return 1
                else:
                    return -1

        return 0

    # The algorithm of the computer's decisions
    def minimax(self, user):
        """
        A recursive function that checks what are the best moves that the computer can do,
        based on the assumption the the opponent plays optimally as well.
        finally it picks a random move from the optimal moves and returns it.
        :param user: the user that his best move is required
        :type user: dict
        :return: list of 3 elements - the row_index, the column_index, the expected final game position
        :rtype: list
        """
        optimal_scores = []

        # Computer is seeking to 1 and user is seeking to -1
        if user["name"] == "Computer":
            best = [-1, -1, -1]
        else:
            best = [-1, -1, 1]

        # Final recursive position - checks the board status and returns the value accordingly
        if self.check_game_is_over():
            value = self.evaluate()
            return [-1, -1, value]

        # Runs on each cell of the board to check his expected final position
        for empty_cell in self.get_empty_positions_coordination_list():
            x, y = empty_cell[0], empty_cell[1]
            # Marks the board with the next move
            self.mark_board_cell(x, y, user)
            # Calls the function based on the marked board
            score = self.minimax(self.switch_user(user))
            # Unmarks the board after final evaluation
            self.remove_board_cell(empty_cell[0], empty_cell[1])
            # Insert the position of the evaluated position
            score[0], score[1] = x, y

            # If the evaluated position is better than previous ones for the computer it is kept
            if user["name"] == "Computer":
                # Computer seeks to value of 1
                if score[2] >= best[2]:
                    best = score
                    optimal_scores.append(best)
                    # Keeps only the best optional positions
                    optimal_scores = list(
                        filter(lambda only_best: only_best[2] == find_maximal_value(optimal_scores)[2],
                               optimal_scores))

            # If the evaluated position is better than previous ones for the user it is kept
            else:
                # user seeks to value of -1
                if score[2] <= best[2]:
                    best = score
                    optimal_scores.append(best)
                    # Keeps only the best optional positions
                    optimal_scores = list(
                        filter(lambda only_best: only_best[2] == find_minimum_value(optimal_scores)[2],
                               optimal_scores))

        # Randomly picks one of the best optional moves
        best = choice(optimal_scores)
        return best
