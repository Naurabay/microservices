import time
from sql_queries import create_table, get_arrivals
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        arrivals = get_arrivals(conn)
        print("-------------------- >>")
        for arrival in arrivals:
            print(arrival)
        print("-------------------- <<")
        time.sleep(5)
