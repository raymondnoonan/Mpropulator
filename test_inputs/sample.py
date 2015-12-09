# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 19:51:59 2015

@author: FSolleza
"""

import sys
import os
sys.path.append(r"C:\Users\fsolleza\Desktop\Projects\Mpropulator")  
#%%
import MPropulator as mpr

#%%
os.chdir(r"C:\Users\fsolleza\Desktop\Projects\Mpropulator\test_inputs")
mpr.populate(shell_xls="newshell.xlsx", output_xls="test4.xlsx", config="csvs/blah.csv")

