import re

# List of validations
# Validate config file function
# Validate populate input (just pull from the validations at start of populate


def validate_input(config, shell_xls, output_xls):
    if not os.path.isfile(config):
        raise ValueError("config not found, make sure your paths are defined"
                         "as a raw string literal (e.g. r'your\path.csv') ")
    if not os.path.isfile(shell_xls):
        raise ValueError("shell not found, make sure your paths are defined"
                         "as a raw string literal (e.g. r'your\path.csv')")

    if output_xls is None:
        warnings.warn("output_xls is not specified -"
                      "this function is overwriting shell_xls")
        output_xls = shell_xls
    else:
        outputPath = sepPath(output_xls)

        if not os.path.isdir(outputPath['path']):
            raise ValueError("Output path not found, make sure your"
                             "paths are defined as a raw string literal"
                             "(e,g. r'your\path.csv')")


def validateConfigPath(config):
    '''
    Validates the config path to make sure that it is csv file
    '''
    if not os.path.isfile(config):
        raise ValueError("config file not found")

    if not config.endswith(".csv"):
        raise ValueError("config file is not a csv")


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
        errorVal = ''.join(["column names must be", str(colnames)])
        raise ValueError(errorVal)


######################################
# Validations for config data
######################################

def validate_tabs(config, workbook):
    tabSet = set(config['tabname'])
    wbSheetList = workbook.get_sheet_names()
    wbSheetSet = set(wbSheetList)
    assert len(wbSheetList) == len(wbSheetSet)
    if not tabSet.issubset(wbSheetSet):
        result = false
        raise ValueError("There are Tabs in your config"
                         "that are not in the shell")


def validate_cellname(cellname):
        # This pattern will match from cell A1 to ZZ999
        pattern = re.compile("[a-z]{1,2}[1-9][0-9]{0,2}", re.IGNORECASE)
        match = re.search(pattern, cellname)
        if not match:
                raise ValueError("{} is not a valid cell name".format(cell))


def validate_ignore(ignore_value):
        if not isinstance(ignore_value, bool):
            raise ValueError('values in ignore col must be empty or True')

# TODO
def overlap(tab):
        pass


def validate_config(config, workbook):
    validate_tabs(config, workbook)

    config['csv_startcell'].map(lambda x: validate_cellname(x))
    config['tab_startcell'].map(lambda x: validate_cellname(x))
    config['skiprows'].map(lambda x: validate_skiprows(x))
    config['skipcols'].map(lambda x: validate_skipcols(x))
    config['ignore'].map(lambda x: validate_ignore(x))
