# %%
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merge = pd.merge(employee, employee, how='inner', left_on='managerId', right_on='id')
    result = merge.loc[merge['salary_x'] > merge['salary_y']]
    result = result[['name_x']].rename({'name_x': 'Employee'}, axis='columns')
    return result

data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})
find_employees(employee)