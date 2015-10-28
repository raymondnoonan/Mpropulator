# MPropulator #
The Pro MPR Populator!

A simple module to help programmers populate Excel worksheets with CSVs of data.

The currently proposed implementation will work like this:

1. Users will create a `config.csv` specifying each table's corresponding tab, rows and columns to skip, start cell, etc. Users can use the `create_config` helper function to create a blank config file. See `config.csv` for an example.
2. Users call the `populate` function, specifying the table shell, output file name, and config file to populate the Excel worksheet with the CSVs. The `populate` function will map the CSV to the Excel worksheet cell-by-cell -- the CSV value in the first row and first column will be put in the corresponding Excel start cell, the CSV value in the first row and second column will be put in the cell one to the right of the Excel start cell, and so on.

```python
import sys
sys.path.append('N:/library_folder')
import MPropulator

# Step 1.
# Optional -- creates a blank config file with name "myconfig.csv"
#    config: name of the config file you're creating
#    tab_names_same_as_csv: will automatically fill in 
MPropulator.create_config(config="myconfig.csv", tab_names_same_as_csv = True) # optional shell for config file

# Step 2. User fills in config file manually

# Step 3. User runs populate function
#    shell: name of the table shell you're referencing
#    output: name of your output file
#    config: name of the config file you're using
#    timestamp: whether you want the timestamp to be affixed to the name (defaults to True)
MPropulator.populate(shell="shell.xlsx", output="out.xlsx", config="myconfig.csv", timestamp=True)
```