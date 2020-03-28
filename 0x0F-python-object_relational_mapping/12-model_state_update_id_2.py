#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """changes the name of a State object from the database hbtn_0e_6_usa"""

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(url.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    # HERE: no SQL query, only objects!
    get_objetc = session.query(State).get(2)

    get_objetc.name = 'New Mexico'
    session.commit()

    session.close()
