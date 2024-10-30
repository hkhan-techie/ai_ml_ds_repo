# import panda_examples as pd
#
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
#
# myvar = pd.DataFrame(mydataset)
#
# print(myvar)

import pandas as pd

print(pd.__version__)

# import panda_examples as pd

# a list of strings
x = ['Python', 'Pandas']

# Calling DataFrame constructor on list
df = pd.DataFrame(x)
print(df)


mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

## Pandas Series

## Create a simple Pandas Series from a list:
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[1])

## Create your own labels
a = [1, 7, 2]

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)
print(myvar["y"])

## Create a simple Pandas Series from a dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

# Create a Series using only data from "day1" and "day2":
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

# Create a DataFrame from two Series
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

## Pandas Dataframes implementation

#Create a simple Pandas DataFrame:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)

# Pandas use the loc attribute to return one or more specified row(s)
#Return row 0:
#refer to the row index:
print(df.loc[0])

#Return row 0 and 1:
#use a list of indexes:
print(df.loc[[0, 1]])