import re
import os
import warnings

# List of validations
# Validate config file function
# Validate populate input (just pull from the validations at start of populate


def validate_input(config, shell_xls, output_xls):
    if not os.path.isfile(config):
        raise ValueError("Config not found, make sure your paths are defined"
                         "as a raw string literal (e.g. r'your\path.csv') ")
    if not os.path.isfile(shell_xls):
        raise ValueError("shell not found, make sure your paths are defined"
                         "as a raw string literal (e.g. r'your\path.csv')")

    if output_xls is None:
        warnings.warn("Output_xls is not specified -"
                      "this function is overwriting shell_xls")
        output_xls = shell_xls
    else:
        outputPath = os.path.dirname(output_xls)

        if not os.path.isdir(outputPath):
            raise ValueError("Output path not found, make sure your"
                             "paths are defined as a raw string literal"
                             "(e,g. r'your\path.csv')")


def validateConfigPath(config):
    '''
    Validates the config path to make sure that it is csv file
    '''
    if not os.path.isfile(config):
        raise ValueError("Config file not found")

    if not config.endswith(".csv"):
        raise ValueError("Config file is not a csv")


def validateConfigRead(config):
    '''
    Validates the columns of the config file to make sure they are
    properly named.

    Makes sure the values of the columns are also in order
    '''

    cols = config.columns
    colnames = ['tabname',
                'csv',
                'csv_startcell',
                'tab_startcell',
                'skiprows',
                'skipcols',
                'ignore']

    # check the column names
    if not cols == colnames:
        errorVal = ''.join(["Column names must be", str(colnames)])
        raise ValueError(errorVal)

    checkFile = os.path.isfile
    # TODO check that each of the csv files exist


######################################
# Validations for config data
######################################

def validate_tabs(config, workbook):
    tabSet = set(config['tabname'])
    wbSheetList = workbook.get_sheet_names()
    wbSheetSet = set(wbSheetList)
    assert len(wbSheetList) == len(wbSheetSet)
    if not tabSet.issubset(wbSheetSet):
        error = "There are Tabs in your config that are not in the shell"
        return (False, error)
    return (True, "")


def validate_cellname(cellname, error_string):
    # This pattern will match from cell A1 to ZZ999
    pattern = re.compile("[a-z]{1,2}[1-9][0-9]{0,2}", re.IGNORECASE)
    match = re.search(pattern, cellname)
    if not match:
            error = "{} is not a valid cell name".format(cellname)
            return (False, error)
    return (True, "")
        
def validate_skiprows(skiprows_value, error_string):
    if skiprows_value and not all(isinstance(x, int) for x in skiprows_value):
        error = "{}: All values in skiprows must be integers".format(skiprows_value)
        return (False, error)
    return (True, "")
    
def validate_skipcols(skipcols_value, error_string):
    pattern = re.compile("[a-z]{1,2}", re.IGNORECASE)
    if skipcols_value and not all(re.search(pattern, x) for x in skipcols_value):
        error = "{}: All values in skiprows must be column names".format(skipcols_value)
        return (False, error)
    return (True, "")

def validate_ignore(ignore_value, error_string):
    if not isinstance(ignore_value, bool):
        error = '{}: Values in ignore col must be empty or True'.format(ignore_value)
        return (False, error)
    return (True, "")

# TODO
def overlap(tab):
    pass


def validate_config(config, workbook):
    errors = []
    
    (okay, error) = validate_tabs(config, workbook)
    if not okay:
        errors.append(error)
        
    errors.extend(myhelper(config['csv_startcell'], validate_cellname))
    errors.extend(myhelper(config['tab_startcell'], validate_cellname))
    errors.extend(myhelper(config['skiprows'], validate_skiprows))
    errors.extend(myhelper(config['skipcols'], validate_skipcols))
    errors.extend(myhelper(config['ignore'], validate_ignore))
    
    if errors:
        raise ValueError("\n".join(errors))
    
def myhelper(col, func):
    result = col.map(lambda x: func(x))
    resultlist = [r for okay, r in result if not okay]
    return resultlist
