import re

# List of validations
# Validate config file function
# Validate populate input (just pull from the validations at start of populate
# 

def validate_input(config, shell_xls, output_xls)

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


######################################
# Validations for config data
######################################

def validate_tabs(config):
    tabSet = set(config['tabname'])
    wbSheetList = workbook.get_sheet_names()
    wbSheetSet = set(wbSheetList)
    assert len(wbSheetList) == len(wbSheetSet)
    if not tabSet.issubset(wbSheetSet):
        raise ValueError("There are Tabs in your config"
                         "that are not in the shell")

def validate_cellname(cellname):
	# This pattern will match from cell A1 to ZZ999
	pattern = re.compile("[a-z]{1,2}[1-9][0-9]{0,2}", re.IGNORECASE)
	match = re.search(pattern, cellname)
	if not match:
		raise ValueError("{} is not a valid cell name".format(cell))

# do we need this given that it's also being checked in readConfig.py?
def validate_skiprows(skiprows_data):
	if not isinstance(skiprows_data, list):
		raise ValueError("error in {}: skiprows must be in list form".format(skiprows_data))
	else:

#TODO: fill in
def validate_skipcols(skipcols_data):

def validate_ignore(ignore_value):
	# What is the correct way to denote missing data?
	if ignore_value is None:
		return
	else if ignore_value.lower() != "true":
		raise ValueError('values in ignore column must be empty or "true"')

#TODO
def overlap(tab):


def validate_config(config):
	# apply all row-level validations
	config['csv_startcell'].map(lambda x: validate_cellname(x))
	config['tab_startcell'].map(lambda x: validate_cellname(x))
	config['skiprows'].map(lambda x: validate_skiprows(x))
	config['skipcols'].map(lambda x: validate_skipcols(x))
	config['ignore'].map(lambda x: validate_ignore(x))


