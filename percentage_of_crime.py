import matplotlib.pyplot as plt
import pandas as pd
import time
import psutil

memory_usage_initial = psutil.Process().memory_info().rss
start = time.time()

# canvas
plt.style.use("seaborn-pastel")
fig, ax = plt.subplots()

data = pd.read_csv(
    "data/transformed_data/data.csv",
    encoding="utf-8",
    header=0
)
required_columns = ["Año", "Subtipo de delito", "Enero", "Febrero", "Marzo",
                    "Abril", "Mayo", "Junio", "Julio", "Agosto"]
data = data[required_columns]

filter_year = data['Año'] == 2023 
filter_by_year = data[filter_year]
filter_by_year = filter_by_year.drop(columns=['Año'])
legal_interest_type = filter_by_year.groupby('Subtipo de delito').sum()

legal_interest_sum = legal_interest_type.sum(axis=1)
percentage_vector = (legal_interest_sum / legal_interest_sum.sum()) * 100

sorted_data = sorted(zip(percentage_vector.index, percentage_vector), key=lambda x: x[1], reverse=True)
sorted_labels, sorted_percentage = zip(*sorted_data) 
ax.set_title(
       label="PERCENTAGE OF CRIMES BY PROTECTED LEGAL INTEREST", 
       color='gray',
       fontsize='14',
)

ax.pie(
    sorted_percentage, 
    labels=[label if percentage_vector[label] > 0.9 else '' for label in sorted_labels], 
    autopct=lambda p: f'{p:.2f}%' if p > 0.9 else '',  
    startangle=-97,
    pctdistance=0.7,
    labeldistance=1.2
)

end = time.time()
memory_usage_final = psutil.Process().memory_info().rss
print(f"RAM used: {(memory_usage_final - memory_usage_initial) / (1024 ** 2):.2f} MB")
print(f"Elapsed time: {end - start:.2f} min")
plt.show()