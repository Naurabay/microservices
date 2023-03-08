from sqlalchemy import create_engine
from arrivals import Arrivals
from sql_queries import start_boarding,insert_flight,get_arrivals,delay,delete_arrived
def test_service1(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    arrival = Arrivals(
             destination="Test destination",
             flight='test_flight',
             airline="test_airline",
             terminal=2,
         )
    
    insert_flight(conn, arrival)
    arrivals = get_arrivals(conn)
    assert len(arrivals) == 4
    arrival = arrivals[-1]
    assert arrival.destination == 'Test destination'

    start_boarding(conn)
    arrivals = get_arrivals(conn)
    for arrival in arrivals:
        if arrival.status == "On Time":
            assert arrival.terminal == 1
         

    
    delay(conn)
    arrivals = get_arrivals(conn)
    for arrival in arrivals:
        if arrival.destination == "Dubai" or arrival.destination == "Warsaw":
            assert arrival.status == "Delayed"

    delete_arrived(conn)
    arrivals = get_arrivals(conn)
    for arrival in arrivals:
        if arrival.status == "On Time":
            assert False


   