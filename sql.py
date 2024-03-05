import pandas as pd
import pyodbc

# Database connection parameters
server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'

# Establish connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# SQL query
query = "SELECT * FROM your_table"

# Load data into DataFrame
df = pd.read_sql(query, cnxn)

# Close connection
cnxn.close()

# Display DataFrame
print(df)
