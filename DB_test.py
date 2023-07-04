import mysql.connector

# MYSQL Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    #database="MyTestDB"
)

# Creating a cursor object
cur = con.cursor()

#Database Operations
#CREATE
cur.execute("CREATE DATABASE MyTestDB")

cur.execute("CREATE TABLE Details (ID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(40), age int, phone VARCHAR(14), gender VARCHAR(6))")

cur.execute("DESCRIBE Details")

#INSERT
query = "INSERT INTO details (name, age, phone, gender) VALUES (%s, %s, %s, %s)"
data = [
    ('fazeel', 24, '090078601', 'Male'),
    ('salman', 28, '03331234567', 'Male'),
    ('ayesha', 26, '0800112255', 'Female'),
    ('sadia', 24, '03022555888', 'Female'),
]
cur.executemany(query, data)
con.commit()
#READ
cur.execute("SELECT * from details")

for i in cur:
   print(i)


#UPDATE
cur.execute("UPDATE details SET phone = '+923001234567' where ID = 1")

cur.execute("SELECT * from details")

for i in cur:
   print(i)

#DELETE
cur.execute("DROP DATABASE MyTestDB")

cur.close()
con.close()
