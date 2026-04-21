# %%
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # result = sales.groupby(by='product_id').filter(lambda x: (x['sale_date'].min() >= pd.to_datetime('2019-01-01')) & (x['sale_date'].max() <= pd.to_datetime('2019-03-31')))
    # result = product.loc[product['product_id'].isin(result['product_id'])][['product_id', 'product_name']]
    # return result
    sales=sales.groupby('product_id')['sale_date'].agg(['min','max']).reset_index()
    print(sales)
    # sales=sales[(sales['min']>='2019-01-01')&(sales['max']<='2019-03-31')]
    # result=pd.merge(sales,product,on='product_id',how='inner')[['product_id','product_name']]
    # return result

data = [[1, 'S8', 1000], [2, 'G4', 800], [3, 'iPhone', 1400]]
product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype({'product_id':'Int64', 'product_name':'object', 'unit_price':'Int64'})
data = [[1, 1, 1, '2019-01-21', 2, 2000], [1, 2, 2, '2019-02-17', 1, 800], [2, 2, 3, '2019-06-02', 1, 800], [3, 3, 4, '2019-05-13', 2, 2800]]
sales = pd.DataFrame(data, columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype({'seller_id':'Int64', 'product_id':'Int64', 'buyer_id':'Int64', 'sale_date':'datetime64[ns]', 'quantity':'Int64', 'price':'Int64'})

sales_analysis(product, sales)
# %%
