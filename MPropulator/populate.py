import helpers
import pandas as pd
import openpyxl
import os
import string
from writetab import write_tab
from readConfig import readConfig
import validations as vd


def populate(config, shell_xls, output_xls=None):
    """Populates an Excel spreadsheet from a shell.

    config: string of CSV file address containing config file
    shell_xls: string of XLSX file address containing Excel shell
    output_xls: string of XLSX file address for output file
                if output_xls is not specified, overwrite shell_xls
    """

    # We temporarily change paths to config
    # file path (that's where all the output ought to be
    origPath = os.getcwd()
    configPath = os.path.dirname(config)

    os.chdir(configPath)

    # Read in all our inputs
    workbook = openpyxl.load_workbook(shell_xls)
    parsed_config = readConfig(configPath['file'])
    vd.validate_tabs(parsed_config)

    for enum, table in parsed_config.iterrows():
        if table['ignore'] is not True:
            sheet = workbook.get_sheet_by_name(table['tabname'])

            csv_startcell = table['csv_startcell']
            csv_start_row = int(csv_startcell.translate(None, string.letters))
            csv_start_col = csv_startcell.translate(None, string.digits)

            if not os.path.isfile(table['csv']):
                error = "Could not find the file %s. Make sure your config is"
                "in the same location as your output " % table['csv']
                raise ValueError(error)

            table_data = pd.read_csv(table['csv'], skiprows=csv_start_row-1)

            csv_start_col = helpers.col_to_number(csv_start_col)
            num_cols = table_data.shape[1]
            cols_to_drop = [x for x in range(0, num_cols - csv_start_col)]

            table_data.drop(table_data.columns[cols_to_drop], axis=1,
                            inplace=True)

            write_tab(sheet, table_data, table['tab_startcell'],
                      table['skiprows'], table['skipcols'])

    workbook.save(output_xls)

    # change back to old path
    os.chdir(origPath)
