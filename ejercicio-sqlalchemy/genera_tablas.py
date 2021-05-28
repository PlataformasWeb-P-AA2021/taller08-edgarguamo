from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String

# se importa información del archivo configuracion
engine = create_engine("sqlite:///mundial2018.db")
Base = declarative_base()

class Mundial2018(Base):
    __tablename__ = 'mundial2018'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    fifa_display_name  = Column(String)
    country = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    shirt_name = Column(String)
    pos = Column(String)
    height = Column(Integer)
    caps = Column(Integer)
    goals = Column(Integer)
    def __repr__(self):
        return " numero: %.0f \n fifa_display_name: %s \n country: %s \n last_name: %s"\
                " \n first_name: %s \n shirt_name: %s \n pos: %s \n height: %.2f \n caps: %.0f \n"\
                " goals: %.0f \n\n" % (self.numero, self.fifa_display_name,
                        self.country, self.last_name, self.first_name,
                        self.shirt_name, self.pos, self.height, self.caps,
                        self.goals)

Base.metadata.create_all(engine)
