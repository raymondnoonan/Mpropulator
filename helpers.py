def column_range(start, stop, increment, chunk=1):
    """0-indexed generator that returns a list of Excel column names. After
    every :chunk columns, the range skips over :increment columns.

    :param start: column index at which you begin iterating
    :param stop: column index at which you want to stop iterating
    :param chunk: size of each set of columns before an increment will occur
    :param increment: number of columns you want to skip per iteration
    :return: list of Excel column names
    """
    assert isinstance(start, int), 'Start must be int'
    assert isinstance(stop, int), 'Stop must be int'
    assert isinstance(increment, int), 'Increment must be int'

    assert start >= 0, 'Start must be >= 0'
    assert stop >= 0, 'Stop must be >= 0'
    assert start < stop, 'Start must be less than stop'

    # TODO: There must be a more pythonic way to implement chunks...
    char = start
    counter = 1
    while char < stop + 1:
        if counter == chunk:
            char += increment
            counter = 0
        else:
            char += 1
            counter += 1
        yield column_name(char + 1)


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