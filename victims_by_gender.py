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
)
required_columns = ["Año", "Sexo", "Enero", "Febrero", "Marzo", 
                    "Abril", "Mayo", "Junio", "Julio", "Agosto"]
required_data = data[required_columns]

filter_by_year = required_data[required_data['Año']==2023]
filter_year= filter_by_year.drop(columns=['Año'])

# Modeling data
sum_by_sex = filter_year.groupby('Sexo').sum()
vector = sum_by_sex.sum(axis=1)
percentage_vector = (vector / vector.sum()) * 100 

sorted_index = percentage_vector.sort_values(ascending=False).index.tolist()
labels = [label for label in sorted_index]

ax.set_title(
    label='RELATIVE PARTICIPATION OF TOTAL VICTIMS BY GENDER (%)*',
    color='gray',
    fontsize='14',
)

ax.pie(
    percentage_vector, 
    labels=labels, 
    autopct='%1.2f%%',
)

end = time.time()
memory_usage_final = psutil.Process().memory_info().rss

# Print the results.
print(f"RAM used to read dataset: {(memory_usage_final - memory_usage_initial) / (1024 ** 2):.2f} MB")
print(f"Elapsed time to read dataset: {end - start:.2f} min")
plt.show()