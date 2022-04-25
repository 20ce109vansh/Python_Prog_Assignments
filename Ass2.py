from re import A
import statistics
import pandas as pd
a=list(map(int,input().split(' ')))
sr = pd.Series(a)
mean = sr.mean()
median = sr.median()
mode = sr.mode()
stdeviation = sr.std(axis=0, skipna=True)
print(sr.min(),' ',sr.max(),' ',mean,' ',stdeviation,' ',statistics.variance(sr))
