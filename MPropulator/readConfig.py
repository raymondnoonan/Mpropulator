import helpers
import pandas as pd
import openpyxl
import ast
import string
import os
import re
import warnings


def readConfig(config):
    '''
    Reads in the config file as a dataframe
    and validates the inputs and outputs of
    this file.

    arg:    config is the path to the config file csv
    output: pandas dataframe that is a parsed and prepped
            config file.
    '''

    validateConfigPath(config)

    parseConfig = pd.read_csv(config);


    # users enter rows to skip as 1,2,3,4 and cols to skip as A,B,C
    # we need to parse these into lists
    split = str.split
    splitFunc = lambda x: split(x,",")
    parseConfig['skiprows'] = map(splitFunc, parseConfig['skiprows'])
    parseConfig['skipcols'] = map(splitFunc, parseConfig['skipcols'])

    # in addition, for the skiprows, we want these as ints, not strings
    def makeInt(array):
        intArray = map(int,array)
        return intArray

    try:
        parseConfig['skiprows'] = map(makeInt, parseConfig['skiprows'])
    except:
        raise ValueError("Cannot convert some values in skiprows to ints")

    parseConfig['ignore'].fillna(False, inplace=True)

    validateConfigRead(parseConfig)
    return parseConfig



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

    cols = config.columns;
    colNames = ['tabname',
                'csv',
                'csv_startcell',
                'tab_startcell',
                'skiprows',
                'skipcols',
                'ignore']

    # check the column names
    if not cols == colNames:
        errorVal = ''.join(["column names must be", str(colnames)])
        raise ValueError(errorVal)

    checkFile = os.path.isfile;
    # TODO check that each of the csv files exist






