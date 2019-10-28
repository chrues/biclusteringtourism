import pandas as pd

file = input("Enter file name: ")
df = pd.read_csv(file+'.csv', engine="python")

cat_df1 = df.select_dtypes(include=['object']).copy()

for i in range(1,len(cat_df1.columns)):
    print(cat_df1.columns[i])
    df.drop(cat_df1.columns[i], axis = 1, inplace = True)

df.to_csv(file + '_withoutCategories.csv')