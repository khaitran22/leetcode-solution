# %%
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(customers, orders, how='left', left_on='id', right_on='customerId', suffixes=('_c', '_o'))
    result = result.loc[result['id_o'].isnull()]['name'].to_frame(name='Customers')
    print(result)

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})
find_customers(customers, orders)
# %%
