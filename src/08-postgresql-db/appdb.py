
import pandas as pd
from sqlalchemy import create_engine

# Establish a connection to your PostgreSQL database
# Replace 'username', 'password', 'hostname', 'port', and 'database_name' with your actual credentials
# engine = create_engine('postgresql://username:password@hostname:port/database_name')

dbport = 5432
database_name = 'postgres'
db_username = 'postgres'
db_password = 'postgres'
db_hostname ='localhost'

engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_hostname}:{dbport}/{database_name}')

# Query to fetch data from a table
query = "SELECT * FROM customers c"

# Read data from PostgreSQL into a pandas DataFrame
df = pd.read_sql(query, engine)

# Close the database connection
engine.dispose()

# Display the DataFrame
print(df)

