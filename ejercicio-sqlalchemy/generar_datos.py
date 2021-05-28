from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importación de la clase con las tablas
from genera_tablas import Mundial2018
import csv

engine = create_engine("sqlite:///mundial2018.db")

Session = sessionmaker(bind=engine)
session = Session()
# Leer el documento
with open('./data/mundial2018.csv', encoding="utf-8") as mundial2018_csv:
    df = csv.reader(mundial2018_csv, delimiter='|', skipinitialspace=True)
    # Saltar el encabezado
    next(df)
    # Generación del Insert into
    for column in df:
        registros = Mundial2018(numero = int(column[0]), fifa_display_name=column[1],
            country = column[2], last_name = column[3], first_name = column[4],
            shirt_name = column[5], pos = column[6], height = int(column[7]),
            caps = int(column[8]), goals = int(column[9]))
        # Agregado del la información a la sesión
        session.add(registros)

# Push de los datos
session.commit()
