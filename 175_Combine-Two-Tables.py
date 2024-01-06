/* Write your T-SQL query statement below */

SELECT a.FirstName, a.LastName, b.City, b.State
FROM Person a 
LEFT JOIN Address b
ON a.PersonId = b.PersonId


# Exercise II:
# Jan 6, 2024
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result_df = pd.merge(person, address, on='personId', how='left')
    result_df = result_df[['firstName', 'lastName', 'city', 'state']]
    return result_df