import time
from sql_queries import create_table, delay
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        delay(conn)
        print("We're sorry for the delay")
        time.sleep(20)
