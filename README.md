# corCoDa-for-python
A translation of the corCoDa.r package (in robCompositions) for use in python. Only necessary changes were made for it to work in Python.
---
Original Author: Petra Kynclova

Original Script: https://rdrr.io/cran/robCompositions/man/corCoDa.html

Original package: https://CRAN.R-project.org/package=robCompositions

---
## Requirements:
- Pandas
- Numpy
- math (built into Python)

## Install:

Put the script (corCoDa.py file) into the same folder as your current workspace/python file and import it with "import corCoDa" in the beginning of your file. 
````
import corCoDa
````
Or paste the whole function into the beginning of your .py file.
## Usage:
The function accepts both Pandas dataframes and Numpy arrays!

After you have imported it can be run with:
````
# if imported - where df is your original dataframe/array
df_new = corCoDa.corCoDa(df)
````


where df is your original dataframe/array and df_new is a new dataframe with the output from the function.
The function accepts Pandas dataframes or Numpy arrays

If you have pasted the whole function in the beginning of your file you run it with:
````
# if pasted - where df is your original dataframe/array
df_new = corCoDa(df)
````

If no argument is given the default is a Pearson correlation calculcation. To choose Spearman or Kendall use:
```
# Spearman calculation
df_new = corCoDa.corCoDa(df, method="spearman")

# Kendall calculation
df_new = corCoDa.corCoDa(df, method="kendall")
```
### Limitations:
- WARING! there is a bug where sometimes spearman (and probably kendall/perason with other data) will produce a NaN value in the resulting array! The original code converts it to 0.0 but this version will produce an NaN. This is probably a bug in the original code.
- Can only do Pearson/Spearman/Kendall correlation calculations
- The input must be a Pandas dataframe or Numpy array
- There can be no 0/NaN/string/negative values in the dataframe/array
- There must be more than 2 columns in the dataframe/array

## Acknowledgements:
The original author for this function is Petra Kynclova and the robCompositions team! I have only translated it to Python.

Tested working on 18.10.2024 with:
- Python 3.11.0
- Pandas 2.0.3
- Numpy 1.24.4


