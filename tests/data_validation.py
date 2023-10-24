import pandas as pd

try:
    data = pd.read_csv("data/raw_data/data_victims.csv",
                     encoding="latin1",
                     usecols=["Año", "Subtipo de delito", "Sexo",
                             "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
                     header=0)
except FileNotFoundError:
    print("El archivo de datos no existe.")
except UnicodeDecodeError:
    print("El archivo de datos no está codificado en UTF-8.")
except ValueError:
    print("El archivo de datos contiene datos no válidos.")
