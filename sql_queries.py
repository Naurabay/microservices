from sqlalchemy.engine import Connection
from sqlalchemy import text

from arrivals import Arrivals




def create_table(conn: Connection):
    query = """
    CREATE TABLE IF NOT EXISTS nurai_airport_arrivals (
        id SERIAL PRIMARY KEY,
        destination VARCHAR(20) NOT NULL,
        flight VARCHAR(20) NOT NULL,
        airline VARCHAR(50) NOT NULL,
        terminal INTEGER,
        std DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'On Time'
        )
    """

    conn.execute(text(query))
    conn.commit()


def insert_flight(conn:Connection,arrival: Arrivals):
    query = """
    INSERT INTO nurai_airport_arrivals (destination, flight, airline, terminal)
    VALUES (:destination, :flight, :airline, :terminal)
    """
    conn.execute(
         text(query),
         parameters={
             "destination": arrival.destination,
             "flight": arrival.flight,
             "airline": arrival.airline,
             "terminal": arrival.terminal,
         },
     )
    conn.commit()


def start_boarding(conn: Connection):
    query = "UPDATE nurai_airport_arrivals SET  status='Boarding...' WHERE terminal=2;"
 
    conn.execute(text(query))
    conn.commit()


def delay(conn: Connection):
    query = "UPDATE nurai_airport_arrivals SET status='Delayed' WHERE destination='Dubai' or destination = 'Warsaw';"
   
    conn.execute(text(query))
    conn.commit()

def delete_arrived(conn: Connection):
    query = "DELETE FROM nurai_airport_arrivals WHERE status = 'On Time';"
    conn.execute(text(query))
    conn.commit()

def get_arrivals(conn: Connection) -> list[Arrivals]:
    query = "SELECT * FROM nurai_airport_arrivals;"
    print('query before')
    arrivals =conn.execute(text(query)).fetchall()
    print('query after')
    return [Arrivals(
        id=arrival[0],
        destination=arrival[1],
        flight=arrival[2],
        airline=arrival[3],
        terminal=arrival[4],
        std=arrival[5],
        status=arrival[6],
    ) for arrival in arrivals]
