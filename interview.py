
import pandas as pd

# data = {"Name" : ['Alice' , 'Bob' , 'Charlie'] ,
#         "Age" : [25,30,35],
#         "City" : ["new york" , "los angeles" , 'chicago']    
#         }

# df = pd.DataFrame(data)

# # basic data analysis
# print(df.describe())

df1 = pd.DataFrame({
    "Key" : ['A' , 'B' , 'C'],
    'Value' : [1,2,3]
})

df2 = pd.DataFrame({
    'Key' : ['B' , 'C' , 'D'],
    'Value' : [4,5,6]
})

merged_df = pd.merge(df1 , df2 , on = 'Key' , how = 'inner')
print(merged_df)