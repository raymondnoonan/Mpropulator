import pandas as pd
import os
import validations as vd

def readConfig(config):
    '''
    Reads in the config file as a dataframe
    and validates the inputs and outputs of
    this file.

    args:   config is the path to the config file csv
    output: pandas dataframe that is a parsed and prepped
            config file.
    '''

    vd.validateConfigPath(config)

    parseConfig = pd.read_csv(config)

    # users enter rows to skip as 1,2,3,4 and cols to skip as A,B,C
    # we need to parse these into lists
    split = str.split
    splitFunc = lambda x: split(x, ",")
    parseConfig['skiprows'] = map(splitFunc, parseConfig['skiprows'])
    parseConfig['skipcols'] = map(splitFunc, parseConfig['skipcols'])
    parseConfig['skiprows'].map(lambda x: assert(isinstance(x, list)))
    parseConfig['skipcols'].map(lambda x: assert(isinstance(x, list)))

    # in addition, for the skiprows, we want these as ints, not strings
    def makeInt(array):
        intArray = map(int, array)
        return intArray

    try:
        parseConfig['skiprows'] = map(makeInt, parseConfig['skiprows'])
    except:
        raise ValueError("Cannot convert some values in skiprows to ints")

    parseConfig['ignore'].fillna(False, inplace=True)

    vd.validateConfigRead(parseConfig)
    return parseConfig



