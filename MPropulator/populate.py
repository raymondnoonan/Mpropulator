import helpers
import pandas as pd
import openpyxl
import ast
import string
import os
import re
import warnings

from readConfig import readConfig

def populate(config, shell_xls, output_xls=None):
    """Populates an Excel spreadsheet from a shell.

    config: string of CSV file address containing config file
    shell_xls: string of XLSX file address containing Excel shell
    output_xls: string of XLSX file address for output file
                if output_xls is not specified, overwrite shell_xls
    """
    # TODO: move to validate populate input function
    if not os.path.isfile(config):
        raise ValueError("config not found, make sure your paths are defined as a raw string literal (e.g. r'your\path.csv') ");
    if not os.path.isfile(shell_xls):
        raise ValueError("shell not found, make sure your paths are defined as a raw string literal (e.g. r'your\path.csv')" );

    if output_xls == None:
        warnings.warn("output_xls is not specified - this function is overwriting shell_xls")
        output_xls = shell_xls
    else:
        outputPath = sepPath(output_xls)

        if not os.path.isdir(outputPath['path']):
            raise ValueError("Output path not found, make sure your paths are defined as a raw string literal (e,g. r'your\path.csv')");


    # We temporarily change paths to config file path (that's where all the output ought to be
    tempPath = os.getcwd()
    configPath = sepPath(config)

    os.chdir(configPath['path'])

    # Read in all our inputs
    workbook = openpyxl.load_workbook(shell_xls)
    parsed_config = readConfig(configPath['file'])

    # Validate the tabs in the parsed config file
    tabSet = set(parse_config['tabname'])
    wbSheetList = workbook.get_sheet_names()
    wbSheetSet = set(wbSheetNames)
    assert len(wbSheetList) == len(wbSheetSet)
    if not tabset.issubset(wbSheetSet):
        raise ValueError("There are Tabs in your config that are not in the shell")

    for enum, table in parsed_config.iterrows():
        if table['ignore'] is not True:
            sheet = workbook.get_sheet_by_name(table['tabname'])

            csv_startcell = table['csv_startcell']
            csv_start_row = int(csv_startcell.translate(None,string.letters))
            csv_start_col = csv_startcell.translate(None, string.digits)

            if not os.path.isfile(table['csv']):
                error = "Could not find the file %s. Make sure your config is in the same location as your output " % table['csv']
                raise ValueError(error)

            table_data = pd.read_csv(table['csv'], skiprows=csv_start_row-1)

            csv_start_col = helpers.col_to_numer(csv_start_col)
            num_cols = table_data.shape[1]
            cols_to_drop = [x for x in range(0, num_cols - csv_start_col)]

            table_data.drop(table_data.columns[cols_to_drop], axis=1,
                            inplace=True)

            write_tab(sheet, table_data, table['tab_startcell'],
                      table['skiprows'], table['skipcols'])

    workbook.save(output_xls)

def sepPath(path):
    '''
    Separates out filename from path.
    Args:   path must be a raw string literal (e.g. r'this\is\your\path.csv')
    Return: a dict list {path:"this\\is\\your",file:'\\path.csv'}
    '''
    pathReg = re.compile("(.+)(\\\\)(.+\..+$)")
    parts = pathReg.findall(path)
    returnDict = {"path": parts[0][0], "file": parts[0][2]}

    return returnDict









