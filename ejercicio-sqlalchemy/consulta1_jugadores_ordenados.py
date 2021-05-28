from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

from genera_tablas import Mundial2018

engine = create_engine("sqlite:///mundial2018.db")

Session = sessionmaker(bind=engine)
session = Session()

# Ordenar a los jugadores por numero de gols
goles = session.query(Mundial2018).order_by(Mundial2018.goals.desc()).all()

for g in goles:
    print(g)

