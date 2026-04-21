# %%
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = person.groupby(by='email').count().reset_index()
    result = result.loc[result['id'] > 1]['email'].to_frame()
    return result

data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})
duplicate_emails(person)
# %%
