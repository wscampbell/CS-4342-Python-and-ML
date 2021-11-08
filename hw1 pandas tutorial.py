# Pandas is a really great Python library for manipulating data
# It uses a custom data type called a Dataframe
# You can install the Pandas library via the Command Prompt using:
# 'pip install pandas'
import pandas as pd

# Matplotlib is a Python library for generating plots
# Can be installed using 'pip install matplotlib' in Command Prompt
import matplotlib.pyplot as plt

# This will load Auto.csv into a Dataframe object
data = pd.read_csv("Auto.csv")

# This will let you see the first 5 lines of data
print(data.head())

# This will print out the datatype of a column
# print(data["cylinders"].dtype)

# These lines will generate a scatter plot of the two specified columns
x = data["cylinders"]
y = data["mpg"]
# plt.scatter(x, y)
# plt.xlabel('cylinders')
# plt.ylabel('mpg')
# plt.show()

# This code will remove '?' from the horsepower column
# It will also change the datatype of the column to integer
# This is necessary because the presence of the '?' causes the datatype to be 'object'
# This causes the values to be compared incorrectly, so we need to convert it to int
hp = data[data["horsepower"] != '?']["horsepower"]
print(hp)
hp = pd.to_numeric(hp)
print(hp.dtype)


