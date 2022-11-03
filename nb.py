#Name:Vailantan Fernandes TE_COMPS_A 9197 BATCH_C

import pandas as pd

df = pd.read_csv('data_8.csv')

df['Outlook'].replace(['Rainy', 'Overcast','Sunny'],
                        [0, 1,2], inplace=True)

df['Temp'].replace(['Hot', 'Mild','Cool'],
                        [0, 1,2], inplace=True)

df['Humidity'].replace(['Normal', 'High'],
                        [0, 1], inplace=True)

df['Windy'].replace(['f', 't'],
                        [0, 1], inplace=True)

df['Play'].replace(['no', 'yes'],
                        [0, 1], inplace=True)

arr = df.to_numpy()


mp = dict()#two key  for yes and no
for i in range(len(arr)):
    row = arr[i]
    y = row[-1] #y key yes or no 1 or 0
    if (y not in mp):
        mp[y] = list() # mp[y] ka value
    mp[y].append(row)
for label in mp:
    print(label)
    for row in mp[label]:
        print(row)

test = [2,1,0,1] #tuple

probYes = 1
count = 0
total = 0
for row in arr:
    if(row[-1] == 1):
        count+=1
    total+=1
print("Total yes: "+str(count)+" / "+str(total))
probYes *= count/total
for i in range(len(test)):
    count = 0
    total = 0
    for row in mp[1]:
        if(test[i] == row[i]):
            count += 1
        total += 1
    print('for feature '+str(i+1))
    print(str(count)+" / "+str(total))
    probYes *= count/total
probNo = 1
count = 0
total = 0
for row in arr:
    if(row[-1] == 0):
        count+=1
    total+=1
probNo *= count/total
print("Total no: "+str(count)+" / "+str(total))
for i in range(len(test)):
    count = 0
    total = 0
    for row in mp[0]:
        if(test[i] == row[i]):
            count += 1
        total += 1
    print('for feature '+str(i+1))
    print(str(count)+" / "+str(total))
    probNo *= count/total

print(probYes)
print(probNo)

prob = probYes/(probYes+probNo)
print("Probability of playing golf: "+str(prob*100)+"%")