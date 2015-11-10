import string


def column_range(start, stop, skip_columns=None):
    """0-indexed function that returns a list of Excel column names, except
    for skip_columns

    :param start: column index at which you begin iterating
    :param stop: column index at which you want to stop iterating
    :param skip_columns: column NAMES you'd like to skip
    :return: list of Excel column names
    """
    if skip_columns is None:
        skip_columns = []

    if start < 0:
        raise ValueError("Start must be >= 0")
    if stop < 0:
        raise ValueError("Stop must be >= 0")

    return [column_name(i + 1) for i in range(start, stop)
            if column_name(i + 1) not in skip_columns]


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


def col_to_number(col):
    """0-indexed function that, given a column name, returns
    the number of that column in excel.

    col: string consisting of Excel column name
    return: int that corresponds to excel column name

    col_to_number("A") => 0
    col_to_number("AB") => 28
    """
    if type(col) != str:
        raise ValueError("Input was not a string")
    elif not col:
        raise ValueError("Input was empty string")

    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
        else:
            raise ValueError("Input had characters other than ASCII letters")
    num -= 1
    assert num >= 0
    return num


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
