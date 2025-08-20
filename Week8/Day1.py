# what is pandas in python?
# pandas is the library in python which is used to interact with large amount of data at the time of data analysis.
# It can be used to create, update, delete the data using pandas

# If you don't have pandas installed you can use:- pip install pandas to install pandas

# import pandas as pd
# var = pd.DataFrame({"num1":[1,2,3,4],"num2":[5,6,7,8]})
# var["add"] = var["num1"] + var["num2"]
# var["sub"] = var["num2"] - var["num1"]
# var["mul"] = var["num1"] * var["num2"]
# print(var)

# data = pd.read_csv("productData.csv")
# print(data[50:65:2])
# print(data.head(60+10))
# print(data.tail(80-10))

# d = data["Category"]
# l = [x for x in d]
# print(len(set(l)))

# f = data["Brand"]
# for i in f:
#     if str(i).startswith("K"):
#         print(i)


