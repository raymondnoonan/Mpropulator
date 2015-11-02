import os
from parseConfig import parseConfig
from MPRWorkbook import MPRWorkbook 

def populate(shellPath, configPath, outPath):
    """
    populates shellPath with files as outlined in
    config file at configPath. Saves outPath
    """

    if !os.path.isfile(shellPath):
        raise ValueError("shellPath is not a file!")

    if !os.path.isfile(configPath):
        raise ValueError("configPath is not a file!")

    if !os.path.isfile(outPath):
        raise ValueError("outPath is not a file!")

    if shellPath == outPath:
        err = "shellPath will be overwritten with outPath"
        raise ValueError(err)


    tabs = parse_config(configPath)
    workbook = MPRWorkbook(shellPath)
    
    
    for tab in tabs:
        tab.write_all(...)
    workbook.save
           
   

