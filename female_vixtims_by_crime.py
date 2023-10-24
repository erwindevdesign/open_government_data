import matplotlib.pyplot as plt
import pandas as pd
import time
import psutil

memory_usage_initial = psutil.Process().memory_info().rss
start = time.time()

plt.style.use("seaborn-pastel")
fig, ax = plt.subplots()  

data = pd.read_csv(
    "data/transformed_data/data.csv",
    encoding="utf-8",
    header=0
)
required_columns = ['Año', 'Subtipo de delito','Sexo', "Enero", "Febrero", 
                    "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto"]
female_data = data[required_columns]

filter_by_year = female_data[female_data['Año']==2023]
filter_year = filter_by_year.drop(columns=['Año'])

filter_by_sex = filter_year[filter_year['Sexo']=='Mujer']
filter_sex = filter_by_sex.drop(columns=['Sexo'])

sum_by_sex = filter_sex.groupby('Subtipo de delito').sum()
vector = sum_by_sex.sum(axis=1)
vector_total = vector.sum(axis=0)

# Percentage
vector_percentage = (vector / vector_total) * 100

sorted_data = sorted(zip(vector_percentage.index, vector_percentage), key=lambda x: x[1], reverse=True)
sorted_labels, sorted_percentage = zip(*sorted_data) 

ax.set_title(
       label="Relative participation of alleged female victims by crime (%)*", 
       color='gray',
       fontsize='14',
)

# Plot
ax.pie(
    sorted_percentage, 
    labels=[label if vector_percentage[label] > 0.6 else '' for label in sorted_labels], 
    autopct=lambda p: f'{p:.2f}%' if p > 0.6 else '',
    
)

end = time.time()
memory_usage_final = psutil.Process().memory_info().rss
print(f"RAM used to read dataset: {(memory_usage_final - memory_usage_initial) / (1024 ** 2):.2f} MB")
print(f"Elapsed time to read dataset: {end - start:.2f} min")
plt.show()