from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import column, integer, string, foreignkey

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
    pos = Column(String)
    height = Column(Integer)
    caps = Column(Integer)
    goals = Column(Integer)
    def __repr__(self):
        return "numero: %s \n fifa_display_name: %f \n country: %s \n last_name: %s"\
                " \n first_name: %s \n pos: %s \n height: %f \n caps: %f \n"\
                " goals: %s \n\n" % (sel.numero, self.fifa_display_name,
                        self.country, )

Base.metada.create_all(engine)
