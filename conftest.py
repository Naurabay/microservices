from typing import Generator
import pytest
from sqlalchemy import Connection, create_engine
from arrivals import Arrivals
from testcontainers.postgres import PostgresContainer

from sql_queries import create_table, insert_flight


@pytest.fixture()
def postgres_container1() -> Generator[PostgresContainer, None, None]:
     with PostgresContainer(image="postgres:latest") as container:
         container.start()
         yield container


@pytest.fixture()
def postgres_container() -> PostgresContainer:
     container = PostgresContainer(image="postgres:latest")
     container.start()
     return container


@pytest.fixture()
def postgres_url(postgres_container: PostgresContainer) -> str:
     engine = create_engine(postgres_container.get_connection_url())
     conn = engine.connect()

     create_table(conn)
     return postgres_container.get_connection_url()


@pytest.fixture(scope="function")
def conn_with_data(postgres_container: PostgresContainer) -> str:
     engine = create_engine(postgres_container.get_connection_url())
     conn = engine.connect()

     create_table(conn)
     arrivals = [
         Arrivals(
             destination="Dubai1",
             flight='KC 123',
             airline="Air Astana",
             terminal=2,
         ),
         Arrivals(
             destination="Warsaw2",
             flight='LO 789',
             airline="Kazakhstan Airlines",
             terminal=1,
         ),
         Arrivals(
            
             destination="FZ 101",
             flight='KSX 123',
             airline="FlyArstan",
             terminal=1,
         ),
               
     ]
     for flight in arrivals:
         insert_flight(conn, flight)
     return postgres_container.get_connection_url()