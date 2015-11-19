from MPropulator import helpers
import string


def write_tab(sheet, table_data, xls_startcell, skiprows, skipcols):
    """Writes the data for a particular table to the corresponding
    Excel spreadsheet.

    sheet: openpyxl worksheet to which you're writing
    table_data: pandas data frame containing data to write
    xls_startcell: cell in the sheet at which you will begin writing
    skiprows: list of rows in Excel spreadsheet to skip
    skipcols: list of columns in Excel spreadsheet to skip
    """
    num_rows = table_data.shape[0]
    num_cols = table_data.shape[1]

    # We subtract one to remain 0-indexed
    start_row = int(xls_startcell.translate(None, string.ascii_letters)) - 1
    start_col = helpers.col_to_number(xls_startcell.translate(None,
                                                              string.digits))

    num_skipcols = [helpers.col_to_number(col) for col in skipcols]

    total_rows = start_row + num_rows + len(skiprows)
    table_rows_to_write = [row for row in range(start_row, total_rows) if
                           row not in skiprows]

    total_cols = start_col + num_cols + len(skipcols)
    table_cols_to_write = [col for col in range(start_col, total_cols) if
                           col not in num_skipcols]

    for row_idx, row in enumerate(table_rows_to_write):
        for col_idx, col in enumerate(table_cols_to_write):
            current_cell = helpers.cell_name(row, col)

            value = table_data.iloc[row_idx, col_idx]
            try:
                value = float(value)
            except ValueError:
                pass

            sheet[current_cell].value = value
