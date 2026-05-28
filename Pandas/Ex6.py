import pandas as pd

# Removendo duplicatas da coluna email
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset="email")
    return customers