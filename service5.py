import time
from sql_queries import create_table, delete_arrived
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        delete_arrived(conn)
        print("Deleted")
        time.sleep(37)
