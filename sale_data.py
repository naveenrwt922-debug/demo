import mysql.connector


conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password ="MeraNaya@789#",
    database="school_db"
)
cursor=conn.cursor()

print("Database connected successfully!")
cursor.execute("select * from students limit 5")
for row in cursor.fetchall():
    print(row)
    conn.close