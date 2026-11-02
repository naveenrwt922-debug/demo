import mysql.connector
import time

HOST = "localhost"
USER = "root"
PASSWORD = "MeraNaya@789#"
DATABASE = "airline_database"

BATCH_SIZE = 10000


def connect():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        connection_timeout=60,
        autocommit=True
    )


conn = connect()
cursor = conn.cursor()

cursor.execute("SELECT MIN(flight_id), MAX(flight_id) FROM flights")
min_id, max_id = cursor.fetchone()

print(f"Flight ID range: {min_id} -> {max_id}")

current_id = min_id

while current_id <= max_id:

    end_id = current_id + BATCH_SIZE

    try:
        if not conn.is_connected():
            print("Reconnecting...")
            conn = connect()
            cursor = conn.cursor()

        print(f"Updating {current_id} -> {end_id}")

        sql = """
        UPDATE flights
        SET
            flight_date = STR_TO_DATE(
                CONCAT(year, '-', month, '-', day),
                '%Y-%m-%d'
            ),
            dep_hour = FLOOR(scheduled_departure / 100) % 24
        WHERE flight_id >= %s
          AND flight_id < %s
          AND flight_date IS NULL
        """

        cursor.execute(sql, (current_id, end_id))

        print(f"Updated: {cursor.rowcount} rows")

        current_id = end_id

    except mysql.connector.Error as e:

        print("Connection/query error:", e)
        print("Retrying in 5 seconds...")

        try:
            conn.close()
        except:
            pass

        time.sleep(5)

        conn = connect()
        cursor = conn.cursor()


cursor.close()
conn.close()

print("================================")
print("UPDATE COMPLETED")
print("================================")