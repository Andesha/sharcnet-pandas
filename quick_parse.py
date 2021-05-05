import pandas as pd

df = pd.read_csv('mpg.tsv', sep='\t')
df = df.dropna()
df['disp_div_cyl'] = df['displacement'].div(df['cylinders'])
df['origin'] = df['origin'].map({1:'NA', 2:'EU', 3:'AS'})
avg_hp = df['horsepower'].mean()
sub_df = df[(df['car_name'].str.contains('ford'))]
sub_df = sub_df[(sub_df['horsepower'] > avg_hp) & (sub_df['model_year'] > 75)]

print(sub_df)
