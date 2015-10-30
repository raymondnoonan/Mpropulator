import helpers
import pandas as pd
import openpyxl
import ast
import string

def populate(config, shell_xls, output_xls):
    """Populates an Excel spreadsheet from a shell.
    
    config: string of CSV file address containing config file
    shell_xls: string of XLS file address containing Excel shell
    output_xls: string of XLS file address for output file
    
    TODO: skip appropriate columns
    """
    workbook = openpyxl.load_workbook(shell_xls)    
    
    convert_cols = {
    'csv_startcell' : ast.literal_eval, 
    'skiprows' : ast.literal_eval,
    'skipcols' : ast.literal_eval
    }
    
    parsed_config = pd.read_csv(config, converters=convert_cols)
    parsed_config.fillna(False, inplace=True)
    
    for table in parsed_config.iterrows():
        if table['ignore'] is not True:        
            sheet = workbook.get_sheet_by_name(table['tabname'])        
            csv_startcell = table['csv_startcell']
            
            table_data = pd.read_csv(table['csv'], skiprows=csv_startcell[0]) 
            # TODO: skip appropriate columns here            
            
            write_tab(sheet, table_data, table['tab_startcell'], \
                table['skiprows'], table['skipcols'])
        
    workbook.save(output_xls)

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
    
    start_row = int(xls_startcell.translate(None, string.ascii_letters))
    start_col = helpers.col_to_number(xls_startcell.translate(None, string.digits))
    
    num_skipcols = [helpers.col_to_number(col) for col in skipcols]    
    
    rows_to_write = [row for row in range(start_row, start_row + num_rows) if \
        row not in skiprows]
    cols_to_write = [col for col in range(start_col, start_col + num_cols) if \
        col not in num_skipcols]
    
    for row_idx, row in enumerate(rows_to_write):
        for col_idx, col in enumerate(cols_to_write):
            current_cell = helpers.cell_name(row, col)
            
            # This will not work if the numpy data type cannot be converted
            # easily into a native python one.
            sheet[current_cell] = table_data.iloc[row_idx, col_idx].item()
            
    
        