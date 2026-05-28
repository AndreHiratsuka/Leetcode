import pandas as pd
# Rename columns
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    col = ["student_id", "first_name", "last_name", "age_in_years"]
    students.columns = col
    return students