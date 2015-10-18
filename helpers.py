def column_range(start, stop, chunk=1, skip=0):
    """0-indexed generator that returns a list of Excel column names. After
    every :chunk columns, the range skips over :increment columns.

    :param start: column index at which you begin iterating
    :param stop: column index at which you want to stop iterating
    :param chunk: how many columns you want before a skip occurs
    :param skip: number of columns you want to skip between chunks
    :return: list of Excel column names
    """
    assert start >= 0, 'Start must be >= 0'
    assert stop >= 0, 'Stop must be >= 0'

    char = start
    counter = 1
    while char < stop:
        yield column_name(char + 1)
        if counter == chunk:
            char += (1 + skip)
            counter = 1
        else:
            char += 1
            counter += 1


def column_name(col):
    """ 1-indexed function that, given a column number, returns
    the Excel column name.

    :rtype : string
    :param col: the column you want to return
    :return: name of the col-th Excel column
    """
    assert isinstance(col, int), 'Column must be int'
    assert col >= 1, 'Column must be >= 1'

    excel_col = str()
    div = col

    while div:
        (div, mod) = divmod(div - 1, 26)
        excel_col = chr(mod + ord('A')) + excel_col

    return excel_col


def cell_name(row, col):
    """ 0-indexed function that, given a row and column number,
    returns the Excel cell name.

    :param row: row index
    :param col: column index
    :return: string
    """
    assert isinstance(row, int), 'Row must be int'
    assert row >= 0, 'Row index must be >= 0'
    assert col >= 0, 'Column index must be >= 0'

    return column_name(col + 1) + str(row + 1)