import psycopg2.extras
import os
# from dotenv import load_dotenv, find_dotenv



# load_dotenv(find_dotenv()) # Load the .env file.

# # Fetch variables from the .env file.
# account_username = os.getenv("ACCOUNT_USERNAME")
# account_password = os.getenv("ACCOUNT_PASSWORD")

# Define your PostgreSQL connection parameters
host = "localhost"  # Replace with your PostgreSQL server's hostname or IP address
port = "5432"  # Replace with your PostgreSQL server's port
user = "william"  # Replace with your PostgreSQL username
password = "d@FF#mEsc5ZyMJCPtzQgqthHGXvshM^F@4S9!*Fjd@ULVof!mff4Ar%Jmd^WGL7kDd3Ve&J4z!2F@R@pbBTb&CYNYWSdpvP8LGRdBcqE6ci#VmL@Hn8!STo&@qy!!c@D"  # Replace with your PostgreSQL password
database = "exchanges_data"  # Replace with your PostgreSQL database name
table_name = "BybitTrades"  # Replace with your table name

# Create the initial PostgreSQL connection
connection = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)
cursor = connection.cursor()