# Exercise I:
# Jan 6, 2024

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_df = employee.sort_values(by='salary', ascending=False)
    salary_unique = sorted_df['salary'].unique()
    nth_salary = salary_unique[N-1] if len(salary_unique) >= N else np.nan 

    if N < 1:
        nth_salary = np.nan
    res_df = pd.DataFrame({'getNthHighestSalary({})'.format(N): [nth_salary]})

    return res_df