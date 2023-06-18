#!/usr/bin/python3
""" Changes the name of a State object from the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)

    query = session.query(State).filter(State.id == 2)
    for q in query:
        q.name = 'New Mexico'
    session.commit()
