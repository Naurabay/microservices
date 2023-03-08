import time
from sql_queries import create_table, start_boarding
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        start_boarding(conn)
        print("Boarding has  started ")
        time.sleep(20)
