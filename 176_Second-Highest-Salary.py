/* Write your T-SQL query statement below */

SELECT DISTINCT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) 
                FROM Employee)


# Exercise II:
# Jan 6, 2024
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_df = employee.sort_values(by='salary', ascending=False)
    if len(sorted_df) > 1:
        res = sorted_df['salary'].iloc[1]
    else:
        res = np.nan
    res_df = pd.DataFrame({'SecondHighestSalary': [res]})
    return res_df
