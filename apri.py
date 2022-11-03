import pandas as pd

df = pd.read_csv("df1.csv")

len(df)

arr=[]
m_arr =[]#main arr

df['List of items'][0].split(",")

for i in range (0,20):
  temp=df['List of items'][i].split(",")
  for j in range (0,len(temp)):
    arr.append(temp[j])
  m_arr.append(arr)
  arr=[]


init = [] #list
for i in m_arr:
    for q in i:
        if(q not in init):
            init.append(q)

print(init)

init=sorted(init)

#Setting minimum support =2

s=2

#Apriori Algorithm

from collections import Counter
c = Counter()
for i in init:
    for d in m_arr:
        if(i in d[1]):
            c[i]+=1
print("C1:")
for i in c:
    print(str([i])+": "+str(c[i]))
print()
l = Counter()
for i in c:
    if(c[i] >= s):
        l[frozenset([i])]+=c[i]
print("L1:")
for i in l:
    print(str(list(i))+": "+str(l[i]))
print()
pl = l
pos = 1
for count in range (2,6):
    nc = set()
    temp = list(l)
    for i in range(0,len(temp)):
        for j in range(i+1,len(temp)):
            t = temp[i].union(temp[j])
            if(len(t) == count):
                nc.add(temp[i].union(temp[j]))
    nc = list(nc)
    c = Counter()
    for i in nc:
        c[i] = 0
        for q in m_arr:
            temp = set(q)
            if(i.issubset(temp)):
                c[i]+=1
    print("C"+str(count)+":")
    for i in c:
        print(str(list(i))+": "+str(c[i]))
    print()
    l = Counter()
    for i in c:
        if(c[i] >= s):
            l[i]+=c[i]
    print("L"+str(count)+":")
    for i in l:
        print(str(list(i))+": "+str(l[i]))
    print()
    if(len(l) == 0):
        break
    pl = l
    pos = count
print("Result: ")
print("L"+str(pos)+":")
for i in pl:
    print(str(list(i))+": "+str(pl[i]))
print()

#Finding the association rules for the subsets

from itertools import combinations
for l in pl:
    c = [frozenset(q) for q in combinations(l,len(l)-1)]
    mmax = 0
    for a in c:
        b = l-a
        ab = l
        sab = 0
        sa = 0
        sb = 0
        for q in m_arr:
            temp = set(q)
            if(a.issubset(temp)):
                sa+=1
            if(b.issubset(temp)):
                sb+=1
            if(ab.issubset(temp)):
                sab+=1
        temp = sab/sa*100
        if(temp > mmax):
            mmax = temp
        temp = sab/sb*100
        if(temp > mmax):
            mmax = temp
        print(str(list(a))+" -> "+str(list(b))+" = "+str(sab/sa*100)+"%")
        print(str(list(b))+" -> "+str(list(a))+" = "+str(sab/sb*100)+"%")

    for a in c:
        b = l-a
        ab = l
        sab = 0
        sa = 0
        sb = 0
        for q in m_arr:
            temp = set(q)
            if(a.issubset(temp)):
                sa+=1
            if(b.issubset(temp)):
                sb+=1
            if(ab.issubset(temp)):
                sab+=1
        temp = sab/sa*100
        
    print()
    print()

# te =TransactionEncoder()
# te_data =te.fit(m_arr).transform(m_arr)
# df = pd.DataFrame(te_data,columns =te.columns_)
# print(df)

# df.to_csv('df.csv')

# df1=apriori(df,min_support=0.01,use_colnames= True)
# print(df1)

# df_ar =association_rules(df1,metric ='confidence',min_threshold=0.5)
# print(df_ar)