import pandas as pd

df = pd.read_csv("prac/df1.csv")
total = len(df)

tempArr =[]
ds =[]

for i in range(0, total):
    temp = df["List of items"][i].split(",")
    for j in range(0, len(temp)) :
        tempArr.append(temp[j])
    ds.append(tempArr)
    temp = []
# print (ds)

init = []

for arr in ds :
    for item in arr :
        if(item not in init) :
            init.append(item)

print(init)



