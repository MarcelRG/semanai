import pandas as pd
import np as numpy
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26)) 
df = pd.DataFrame({'col1':ser1,'col2':ser2})
df.head()