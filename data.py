import pandas as pd

df = []
for i in range(3):
    df.append(pd.read_csv('data/daily_sales_data_'+str(i)+'.csv'))
    df[i] = df[i][df[i]['product'] == 'pink morsel']

combined_df= pd.concat([df[0], df[1], df[2]], ignore_index=True)
combined_df['price'] = combined_df['price'].str.replace('$', '')
combined_df['price'] = pd.to_numeric(combined_df['price'])
#print(combined_df.head())
combined_df['sales'] = combined_df['quantity'] * combined_df['price']
combined_df = combined_df.drop(['product' , 'quantity', 'price'], axis=1)
print(combined_df.head())
combined_df.to_csv('output.csv', index=False)
