import helpers
import pandas as pd
import openpyxl
import os
import string
import re
import warnings
from writetab import write_tab
from read_config import read_config


def populate(config, shell_xls, output_xls=None):
    """Populates an Excel spreadsheet from a shell.

    config: string of CSV file address containing config file
    shell_xls: string of XLSX file address containing Excel shell
    output_xls: string of XLSX file address for output file
                if output_xls is not specified, overwrite shell_xls
    """
    # TODO: move to validate populate input function
    if not os.path.isfile(config):
        raise ValueError("config file not found")
    if not os.path.isfile(shell_xls):
        raise ValueError("shell not found")

    if output_xls is None:
        warnings.warn("output_xls is not specified -"
                      "this function is overwriting shell_xls")
        output_xls = shell_xls

    pathReg = re.compile("(.+)(\/.+\..+$)")
    path = pathReg.findall(output_xls)
    path = path[0][0]
    if not os.path.isdir(path):
        raise ValueError("Output paths not found")

    workbook = openpyxl.load_workbook(shell_xls)

    parsed_config = read_config(config)

    # Todo Validate Config File Function
    parsed_config['ignore'].fillna(False, inplace=True)
    tabSet = set(parsed_config['tabname'])

    wbSheetList = workbook.get_sheet_names()
    wbSheetSet = set(wbSheetList)
    assert len(wbSheetList) == len(wbSheetSet)
    if not tabSet.issubset(wbSheetSet):
        raise ValueError("There are Tabs in your config"
                         "that are not in the shell")

    for enum, table in parsed_config.iterrows():
        if table['ignore'] is not True:
            sheet = workbook.get_sheet_by_name(table['tabname'])

            csv_startcell = table['csv_startcell']
            csv_start_row = int(csv_startcell.translate(None, string.letters))
            csv_start_col = csv_startcell.translate(None, string.digits)

            table_data = pd.read_csv(table['csv'], skiprows=csv_start_row-1)

            csv_start_col = helpers.col_to_numer(csv_start_col)
            num_cols = table_data.shape[1]
            cols_to_drop = [x for x in range(0, num_cols - csv_start_col)]

            table_data.drop(table_data.columns[cols_to_drop], axis=1,
                            inplace=True)

            write_tab(sheet, table_data, table['tab_startcell'],
                      table['skiprows'], table['skipcols'])

    workbook.save(output_xls)
