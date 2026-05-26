import pandas as pd

# Increase 2 times the salary of employees
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"]*2
    return employees