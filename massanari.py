def column_range(start, stop, increment):
    """
    0-indexed generator that returns a range of column names for easy iteration.
    :param start: column index at which you begin iterating
    :param stop: column index at which you want to stop iterating
    :param increment:
    :return: list of strings
    """
    char = start
    while char < stop + 1:
        yield column_name(char + 1)
        char += increment

def column_name(col):
    """
    1-indexed function that, given a column number, returns
    the Excel column name.
    :param col: the column you want to return
    :return: string
    """
    excelCol = str()
    div = col

    while div:
        (div, mod) = divmod(div - 1, 26)
        excelCol = chr(mod + ord('A')) + excelCol

    return excelCol

def cell_name(row, col):
    """
    0-indexed function that, given a row and column number,
    returns the Excel cell name.

    :param row: row index
    :param col: column index
    :return: string
    """

    return column_name(col + 1) + str(row +1)

