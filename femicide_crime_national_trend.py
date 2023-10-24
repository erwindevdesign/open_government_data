import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import psutil

memory_usage_initial = psutil.Process().memory_info().rss
start = time.time()

plt.style.use("seaborn-pastel")
fig, ax = plt.subplots(figsize=(12, 6)) 
data = pd.read_csv(
    "data/transformed_data/data.csv",
    encoding="utf-8",
)
required_columns = ['Año', 'Subtipo de delito',         
                    'Sexo', "Enero", "Febrero", 
                    "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
                    'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']  
data_required = data[required_columns]

filter_by_crime = data[data_required['Subtipo de delito'] == 'Feminicidio']
filter_femicide = filter_by_crime.drop(columns=['Subtipo de delito'])

filter_by_sex = filter_femicide[filter_femicide['Sexo'] == 'Mujer']
filter_sex_int = filter_by_sex.drop(columns=['Sexo'])

filter_by_sex.set_index('Año', inplace=True)

year_sum = filter_sex_int.groupby('Año').sum().astype(int)

data_year_sum = {}
data_month_dict = {}

for año in year_sum.index:
	data_año = year_sum.loc[año]
	valores = data_año.sum(axis=0).tolist()
	data_year_sum[año] = valores

for año in year_sum.index:
    data_año = year_sum.loc[año]
    valores = data_año.tolist()
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    mes_dict = {meses[i]: valores[i] for i in range(len(meses))}
    data_month_dict[año] = mes_dict

# Configura el espaciado entre meses y años en el eje x
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

años = list(data_year_sum.keys())
años = años[:-1]
num_años = len(años)
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
x_positions = list(range(num_años * 12))
y_values = []
colores = ['gray'] * (num_años * 12)
for año in años:
    valores = data_month_dict[año].values()
    y_values.extend(valores)
    for i, valor in enumerate(valores):
        if valor > 100:
            colores[i + (años.index(año) * 12)] = 'r'
        if valor < 30:
            colores[i + (años.index(año) * 12)] = 'g'

# Crea el gráfico de línea
plt.figure(figsize=(12, 6))
plt.plot(x_positions, y_values, marker='o', linestyle='--' )

for x, y, color in zip(x_positions, y_values, colores):
    plt.plot(x, y, marker='o', linestyle='--', color=color)


# Configura el eje x y sus etiquetas
plt.xticks(range(0, num_años * 12, 12), años)  # Etiquetas de años en el eje x
plt.xlabel('Year', color='gray', fontsize='12',)

# Configura el eje y y su etiqueta
plt.ylabel('Count', color='gray', fontsize='12',)

# Título del gráfico
plt.title('ALLEGED FEMICIDE CRIMES: NATIONAL TREND', color='gray', fontsize='14',)

# Agregar números en los puntos azules
for x, y in zip(x_positions, y_values):
    plt.text(x, y, str(y), ha='left', va='bottom', fontsize=8.5,  color='gray')

end = time.time()
memory_usage_final = psutil.Process().memory_info().rss

print(f"RAM used to read dataset: {(memory_usage_final - memory_usage_initial) / (1024 ** 2):.2f} MB")
print(f"Elapsed time to read dataset: {end - start:.2f} min")
plt.grid(True)
plt.show()