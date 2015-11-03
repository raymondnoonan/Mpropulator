class Tab(openpyxl.Sheet):
        
    def __init__(self, tables):
        self.tables = tables
        self.tab_name = tab_name        
        
    def overlap(self):
        # deal with it        
        # a change by SRM
        
    def write_all(self):
        for table in self.tables:
            table.write()
 
