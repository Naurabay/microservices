import time
import random
from sql_queries import create_table, insert_flight
from arrivals import Arrivals
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        insert_flight(
            conn,
            Arrivals(
                destination=random.choice(["Dubai", "Warsaw", "Istanbul", "Almaty","Aktau","Moscow","Antalya","Shymkent","Astana","Kazan"]),
                flight=random.choice(["KC 123", "KC 456", "LO 789", "FZ 101", "IQ 112", "FV 113", "TK 114", "KCX 115", "DV 116", "KC 117"]),
                airline=random.choice(["Kazakhstan Airlines", "LOT Polish Airlines", "FlyArstan", "Turkish Airlines", "Kuwait Airways", "Air Astana", "Delta Air Lines", "SCAT airlines", "Qatar Airways"]),
                terminal=random.randint(1, 2),
            )
        )
        print("Inserted")
        time.sleep(3)
