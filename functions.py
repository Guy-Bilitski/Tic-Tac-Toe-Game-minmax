import functools

def find_empty_cell_index(part_of_board):
    """
    returns the index of an empty cell in a list
    :param part_of_board: a list (in this case that represents the row/column/diagonal of the board
    :type part_of_board: list
    :return: the index where the empty cell is located
    :rtype: int
    """
    for index, cell in enumerate(part_of_board):
        if cell == ' ':
            return index


def find_maximal_value(optimal_scores):
    """
    Gets a list of lists of 3 elements
    Returns the biggest value that all the lists have in the third element
    :param optimal_scores: list of lists of 3 elements
    :type optimal_scores: list
    :return: the biggest value (In our case the result of the optimal moves)
    :rtype: int
    """
    return functools.reduce(lambda a, b: a if a[2] >= b[2] else b, optimal_scores)


def find_minimum_value(optimal_scores):
    """
        Gets a list of lists of 3 elements
        Returns the smallest value that all the lists have in the third element
        :param optimal_scores: list of lists of 3 elements
        :type optimal_scores: list
        :return: the smallest value (In our case the result of the optimal moves)
        :rtype: int
        """
    return functools.reduce(lambda a, b: a if a[2] <= b[2] else b, optimal_scores)


