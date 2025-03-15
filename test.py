import pandas as pd

 
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

 
print(df)
df1= pd.read_excel("EPA-2024.xlsx")
print(df1.head())