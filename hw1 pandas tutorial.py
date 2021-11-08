import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Auto.csv")


# print(data["cylinders"].dtype)

x = data["cylinders"]
y = data["mpg"]
# plt.scatter(x, y)
# plt.xlabel('cylinders')
# plt.ylabel('mpg')
# plt.show()


hp = data[data["horsepower"] != '?']["horsepower"]
print(hp)
# data["horsepower"] = pd.to_numeric(data["horsepower"])
# print(data["horsepower"].dtype)


