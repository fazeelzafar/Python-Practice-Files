import psycopg2

# Establishing connection with db
dbConn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password",
    port="your_port"
)

# Creating a cursor object to interact
cur = dbConn.cursor()
cursor_obj = dbConn.cursor()

# Example SQL Query
cursor_obj.execute("SELECT * FROM your_table")

# Fetching all rows that we got after executing above query
rows = cursor_obj.fetchall()

# Printing all the fetched rows
for row in rows:
    print(row)

# Closing the cursor and connection
cursor_obj.close()
dbConn.close()