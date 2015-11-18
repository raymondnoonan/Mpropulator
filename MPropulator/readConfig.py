import pandas as pd
import os
from MPropulator import validations as vd
import ipdb

def readConfig(config):
    '''
    Reads in the config file as a dataframe
    and validates the inputs and outputs of
    this file.

    args:   config is the path to the config file csv
    output: pandas dataframe that is a parsed and prepped
            config file.
    '''

    ipdb.set_trace()
    vd.validateConfigPath(config)

    parseConfig = pd.read_csv(config)
    #parseConfig.fillna("", inplace=True)

    # users enter rows to skip as 1,2,3,4 and cols to skip as A,B,C
    # we need to parse these into lists
    split = str.split
    def splitFunc(val):
        arr = split(str(val).strip(" "),",")
        arr = [x for x in arr if x != 'nan']
        return arr
    #splitFunc = lambda x: split(str(x).strip(" "), ",")

    def assertList(x):
        assert(isinstance(x,list))

    parseConfig['skiprows'] = map(splitFunc, parseConfig['skiprows'])
    parseConfig['skipcols'] = map(splitFunc, parseConfig['skipcols'])

    map(assertList, parseConfig['skiprows'])
    map(assertList, parseConfig['skipcols'])

    # in addition, for the skiprows, we want these as ints, not strings
    def makeInt(array):
        intArray = [int(x) for x in array]
        return intArray

    try:
        parseConfig['skiprows'] = map(makeInt, parseConfig['skiprows'])
    except:
        raise ValueError("Cannot convert some values in skiprows to ints")

    parseConfig['ignore'].fillna(False, inplace=True)

    vd.validateConfigRead(parseConfig)
    return parseConfig



