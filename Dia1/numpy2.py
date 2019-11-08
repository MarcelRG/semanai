import streamlit as st
import pandas as pd
import numpy as np
import time
import uber_display
from scipy import stats

"# Numpy and Pandas Tutorial"
"### Semana i 2019"
"Made in Streamlit"

if st.checkbox('Show Uber Data'):
    st.subheader('Uber data data')
    uber_display.main()

"""# Numpy exercises  """

"- **Show numpy version**"
version = np.__version__
result = "Numpy version : {}".format(version)

#Answer
result

"- **Create the array :** "
"   *[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]*"

#Answer
result = np.array([0,1,2,3,4,5,6,7,])
"Answer"
result


"- **Select the cell located in row 2 column 2 from this array**"

arr = np.array(([21, 22, 23], [11, 22, 33], [43, 77, 89]))
"*Array*"
arr

#Answer
result = arr[1][1]
result

"- **Select the column with index 0**"
arr = np.array(([21, 22, 23], [11, 22, 33], [43, 77, 89]))
arr

#Answer
result = arr.T[0]
result

"- **Extract all the odd numbers in the next array**"
"   *[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]*"

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr = arr[arr % 2 == 1 ]
result = arr
result

"""- **Replace de odd numbers with negative numbers in the next array**"""
"   *[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]*"

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#Answer
l = []
for x in range(len(arr)):
    if(arr[x] % 2 == 1):
        l.append(-arr[x])
    else:
        l.append(arr[x])
result = l
result

"- **Reshape the next array from 1D to 2D**"
"   *[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]*"
arr = np.arange(10)
#Answer
arr = arr.reshape([2,5])
result = arr
result

"- **Compute euclidian distance between A and B **"
"A"
a = np.array([1,2,3,4,5])
a
"B"
b = np.array([4,5,6,7,8])
b
#Answer
result = np.linalg.norm(a-b)
result

"- **Find the most frequent value of petal length (3rd column) in the [iris dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)**"
def downloadIrisDataset():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='object')
    return iris
"*Dataset*"
iris = downloadIrisDataset()
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
#Answer
moda = stats.mode(iris.T[2])
result = moda[0][0]
result