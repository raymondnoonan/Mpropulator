# MPropulator Meeting notes #

## 10/23/2015 - Kickoff ##

RSF agreed that at first, this would be a tool for programmers. In the future they would like it to implement a GUI for researchers.

They drafted an initial implementation to look something like this:

```python
<<<<<<< HEAD
import sys
sys.path.append('N:/library_folder')
import MPropulator
	
# Timestamp on file name
# default argument of timestamp = true to indicate whether timestamp would be included in file name
MPropulator.create_config(config="config.csv", tab_names_same_as_csv = True) # optional shell for config file
MPropulator.populate(shell="shell.xlsx", output="out.xlsx", config="config.csv", timestamp=True)

=======
import ExcelPopulator
	
# Timestamp on file name
# default argument of timestamp = true to indicate whether timestamp would be included in file name
ExcelPopulator.populate("file.xls", config="blah.csv", timestamp=True)
ExcelPopulator.create_config("file.xlsx", ignoretabs = [""],
                         tab_names_same_as_csv = True)
>>>>>>> 52641d7f321d3481e762271f16c60ffe4eaddd76
```

`ExcelPopulator.create_config` would create a semi-filled in Excel file that the programmer would then complete. See `config.csv` for an example.

<<<<<<< HEAD
At their next meeting, they agreed to divy up the tasks.

## 10/26/2015 ##

import ExcelPopulator
import ExcelPopulator.populate


--
Library
	MPropulator
		| __init__.py
		| create_config.py
		| populate.py
		| tab.py






=======
At their next meeting, they agreed to divy up the tasks.
>>>>>>> 52641d7f321d3481e762271f16c60ffe4eaddd76
