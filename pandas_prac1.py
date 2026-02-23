import pandas as pd

"""


#series = 1 dimensional array/ data
data=[100,102,103,104,105]
#data=[100.1,102.2,104.0]
#data=["aaa","bb","c"]
#data=[True,False,True]

#series=pd.Series(data,index=["apartment no 1","apartment no 2","apartment no 3"])
series=pd.Series(data,index=["a","b","c","d","e"])
print(series)
print(" - x - ")
#for indexing in series func

print(series.loc["a"])  #returns the value of index "a"
print(" - x - ")

#for editing a element of known label(index)
series.loc["a"]=101
print(series.loc["a"])
print(" - x - ")

#if u want to use the direct indexing (the classic one )
print(series.iloc[0])
print(" - x - ")

print(series[series >= 104])
print(" - x - ")

"""

#complex example using a dict
calories={"day 1":1750,"day 2":2100,"day 3":1700}
series=pd.Series(calories)

series.loc["day 3"]=series.loc["day 3"]+500
print(series[series > 2000])
print(" - x - ")
print(series.loc["day 3"])
print(" - x - ")