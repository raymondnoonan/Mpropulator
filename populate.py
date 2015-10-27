# TODO:

def populate(...):
    tabs = parse_config(...)
    workbook = MPRWorkbook()
    for tab in tabs:
        tab.write_all(...)
    workbook.save

def parse_config(...):
    tabs_to_return = []    
    for row in config_file:
        new_tab = Tab()
        new_tab.start_cell = ...
        ...
        tabs_to_return.append(new_tab)
    return tabs_to_return
    
class Table(object):

    def __init__(self, <config_information>):
        <initialize config attributes>
        skip_rows
        skip_columns
        start_cell (aka first_cell)
        csv_startcell        
        csv
        last_cell          
          
    def write(self):
        # deal with it
             
class Tab(openpyxl.Sheet):
        
    def __init__(self, tables):
        self.tables = tables
        self.tab_name = tab_name        
        
    def overlap(self):
        # deal with it        
        
    def write_all(self):
        for table in self.tables:
            table.write()
    
class MPRWorkbook(openpyxl.workbook):
    def __init__(self):
        pass

# Create config class?
# No- it's just data storage

# Parse config file
# skip_rows

# Read in CSV(s) of data
# Write to Excel
