#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """lists all State objects from the database hbtn_0e_6_usa"""

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(url.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    # HERE: no SQL query, only objects!
    flag = 0
    for state in session.query(State.id).filter(State.name == argv[4]):
            print(state.id)
            flag = 1

    if flag == 0:
        print("Not found")

    session.close()
