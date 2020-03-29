#!/usr/bin/python3
"""Create the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    """lists all State objects from the database hbtn_0e_6_usa"""

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(url.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    new_data = State(name='California', cities=[City(name='San Francisco')])
    session.add(new_data)
    session.commit()

    session.close()
