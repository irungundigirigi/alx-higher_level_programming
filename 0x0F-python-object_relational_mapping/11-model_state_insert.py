#!/usr/bin/python3

"""
This script lists all State objects from `hbtn_0e_6_usa` db
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
        Get states from database
    """
    
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print('{0}'.format(new_state.id))
    session.close()
