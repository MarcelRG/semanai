import pandas as pd

#1
ser1 = pd.Series([1,2,3,4,5])
ser2 = pd.Series([4,5,6,7,8])
In1 = pd.Index(ser1)
In2 = pd.Index(ser2)
In = In1.difference(In2)
print(pd.Series(list(In)))

#2
df1 = pd.DataFrame(ser1)
df2 = pd.DataFrame(ser2)
merge = pd.DataFrame({'A': ser1, 'B': ser2})
merge

#3
print((df1.merge(df2, how = 'inner')))

#4
result = ser1.isin(ser2)
print(result)
print(ser1[~result])

#5
arr = list(range(7*5))
mat = np.reshape(arr, [7,5])
mat = pd.DataFrame(mat)
mat

#6
words = ['how', 'to', 'kick', 'ass']
wser = pd.Series(words)
print(wser.str.capitalize())

#7
p = pd.Series([1,2,3,4,5,6,7,8,9,10])
q = pd.Series([10,9,8,7,6,5,4,3,2,1])
res = np.linalg.norm(np.array(p) - np.array(q))
res