#!/usr/bin/python3
""" script to list all states objects """
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm.session import sessionmaker, Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    index = 0
    for state in session.query(State).filter(State.name == (sys.argv[4],)):
        if state:
            print('{}'.format(state.id))
            index = 1
    if not index:
        print("Not found")
