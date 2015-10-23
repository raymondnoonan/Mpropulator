# MPropulator Meeting notes #

## 10/23/2015 - Kickoff ##

RSF agreed that at first, this would be a tool for programmers. In the future they would like it to implement a GUI for researchers.

They drafted an initial implementation to look something like this:

```python
import ExcelPopulator
	
# Timestamp on file name
# default argument of timestamp = true to indicate whether timestamp would be included in file name
ExcelPopulator.populate("file.xls", config="blah.csv", timestamp=True)
ExcelPopulator.create_config("file.xlsx", ignoretabs = [""],
                         tab_names_same_as_csv = True)
```

`ExcelPopulator.create_config` would create a semi-filled in Excel file that the programmer would then complete. See `config.csv` for an example.

At their next meeting, they agreed to divy up the tasks.