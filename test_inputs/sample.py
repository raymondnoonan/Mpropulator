# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 19:51:59 2015

@author: FSolleza
"""

import sys
import os
sys.path.append(r"Path/to/containing/folder")  
#%%
import MPropulator as mpr

#%%
mpr.populate(shell_xls="newshell.xlsx", output_xls="test4.xlsx", config="csvs/blah.csv")

