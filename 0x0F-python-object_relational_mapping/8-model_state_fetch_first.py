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
    state = session.query(State).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print("Nothing")
