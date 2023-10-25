<a name="readme-top"></a>

<div align="center">
    <img src="https://drive.google.com/uc?export=view&id=1aA_4Uo08zyi-wXtKRept0aTyIiGlAsb7" width="95vw">
    <h1>Information on Violence Against Women</h1>
        <h2>Data Exploration and Optimization Analysis</h2>
</div>

In January 2018, the Mexican government implemented a new methodology for the registration and classification of crimes and victims, which allows for the preparation of a statistical report on alleged crimes against women. This project will use open data extracted from official Mexican government websites to implement data exploration, cleaning, and validation methods. These methods will be used to create visualizations similar to those provided on these websites for statistical purposes.


<br />
<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1S5JugqaArm8wK-8UWBmNpFdpAKHj-Ozh">
</div>

###### ***Criminal incidence refers to the alleged occurrence of crimes recorded in preliminary investigations initiated or cases reported by the State Attorney General's Offices and General Prosecutors of the federal entities in the case of common law and by the Attorney General's Office of the Republic in the federal jurisdiction.***


<details>
    <summary><b>Table of Contents</b></summary>
        <ul>
            <li>
                <a href="#about-the-project" >
                About The Project
                </a>
            </li>
            <li>
                <a href="#built-with">
                Built With
                </a>
            </li>
            <li>
                <a href="#prerequisites">
                Prerequisites
                </a>
                <ul>
                    <li>
                        <a href="#to-get-stated">
                        To get started
                        </a>
                    </li>
                    <li>
                        <a href="#folder-structure"> 
                        Folder Structure
                        </a>
                    </li>
                </ul>
            </li>
            <li>
                <a href="#dataset">
                Dataset
                </a>
            </li>
            <li>
                <a href="#lets-start">
                Lets-start
                </a>
            </li>
            <ol>
                    <li>
                        <a href="#data-exploration"> 
                        Data Exploration
                        </a>
                    </li>
                    <li>
                        <a href="#data-cleaning"> 
                        Data Cleaning
                        </a>
                    </li>
                    <li>
                        <a href="#data-validation"> 
                        Data Validation
                        </a>
                    </li>
                    <li>
                        <a href="#data-visualization"> 
                        Data Visualization
                        </a>
                    </li>
                </ol>
            <li>
                <a href="#contributing">
                Contributing
                </a>
            </li>
            <li>
                <a href="#license">
                License
                </a>
            </li>
            <li>
                <a href="#contact">
                Contact
                </a>
            </li>
            <li>
                <a href="#acknowledgments">
                Acknowledgments
                </a>
            </li>
            <li>
                <a href="#additional-resources">
                Additional Resources
                </a>
            </li>
        </ul>
</details>

<a name="about-the-project"></a>

### 📝 About The Project 

This analysis is conducted to implement best practices in the utilization and exploration of large-scale datasets, aiming to minimize resource consumption on the device where the analysis is performed.

For efficient data handling, it's essential to consider:

- [x] Prioritize Relevant Data.
- [x] Load data in small `chunks`.
- [x] Access and change data `chunks` values.
- [x] Save modified data into a new `csv\*` file.
- [x] Employing optimal algorithms for processing large datasets.
- [x] Utilizing memory-efficient techniques to mitigate resource usage.
- [ ] Fine-tuning execution parameters based on available hardware capacity.
- [ ] Testing.

By following these practices, we aim to enhance the efficiency of our data analysis processes while achieving a more sustainable use of system resources. _Execution times and system resource utilization will depend on the capacity of the underlying hardware._

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="built-with"></a>

### 🛠️ Built With 

This project was created with the following technologies:

<br />
<div align="center">

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Numpy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

</div>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="prerequisites"></a>

### 📋 Prerequisites 

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) <br>

This project uses the following Python libraries:

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Numpy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

In addition, the project uses open data provided by the Mexican government. This data is manipulated using best practices to ensure that the datasets have the same dimensions.

<a name="to-get-stated"></a>

#### :school_satchel: To get started

To get a local copy of the project up and running, follow these simple steps:

1. Create a working directory for hosting the files for the analysis:

```sh
❯ mkdir hosting_folder_name
❯ cd hosting_folder_name
```

2. Clone the repository:

```sh
git clone https://github.com/erwindevdesign/open_government_data.git
```

3. Create a virtual environment in the current working directory to manage projects with different dependencies, and install the Python packages and libraries:

```sh
❯ python3 -m venv env
source env/bin/activate
```

4. Install the dependencies required for the execution of the analysis:

```sh
❯ pip3 install -r requirements.txt
```

5. Create a `.gitignore` file to ignore specific files and prevent them from being tracked:

```sh
❯ touch .gitignore
```

Copy and paste the following text into the .gitignore file:

```sh
images
data
venv
```

6. Download the [contents](https://drive.google.com/drive/folders/1QFvRC7E9biw8x6y_I3CalyWy14Fb7Yfh?usp=sharing) of the data folder from the following cloud link:

[Download](https://drive.google.com/drive/folders/1QFvRC7E9biw8x6y_I3CalyWy14Fb7Yfh?usp=sharing)

<a name="folder-structure"></a>

#### :cactus: Folder Structure

```sh
code
.
│
├── data
│   ├── raw_data
│   │   └── IDVFC_NM_ago23.csv
│   │
│   └── transformed_data
│       └── selected_data.csv
│
├── female_vixtims_by_crime.py
├── femicide_crime_national_trend.py
├── percentage_of_crime.py
├── victims_by_gender.py
├── README.md
├── .gitignore
└── requirements.txt
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="dataset"></a>

### :floppy_disk: Dataset

The code presented in this repository is designed to be executed in a command-line interface or terminal using the Python programming language. The analysis presented here will make use of [Open Data](https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva?state=published) related to [Criminal Incidence](https://www.gob.mx/sesnsp/acciones-y-programas/incidencia-delictiva-299891?state=published) provided by the government of Mexico and published on their [official websites](https://www.gob.mx/sesnsp/articulos/incidencia-delictiva). It focuses on their new methodology, which offers a more detailed breakdown of crimes, increasing from 22 to 53 different offenses grouped into 7 affected legal interests.

    * Name: **IDVFC_NM_jul23.csv**
    * Type: Documento CSV (text/csv)
    * Size: 10.6+ MB
    * Data Shape:  (66240, 21)
    * Rename: **data_victims.csv**

Download: [IDVFC_NM_jul23.csv](https://drive.google.com/file/d/1rXHjOxSXeTJhOwoDb6fdar_YApa7Pe43/view)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="lets-start"></a>

### :bar_chart: Let's start

#### Introduction

In this phase, we will conduct a comprehensive test on the entire dataset, serving as a time benchmark. This benchmark will be used for performance comparison as we progress through the data exploration process. The aim is to optimize resource utilization and implement best practices for data analysis. After understanding the dataset's size and structure, the next step is to identify the specific data with which we will be working. This will be determined by the business logic or the objectives of the analysis. Once the relevant data to the analysis are selected, we will proceed to validate the hypotheses and theories about the data. With the validation of the data, we will create the visualizations objective of the analysis.

<a name="data-exploration"></a>

#### :heavy_exclamation_mark: Data Exploration

The first step in any data visualization project is to explore the data. This involves understanding the data's dimension and shape, as well as its distribution and characteristics.

##### Code:

```py
# Import the required dependencies and libraries
import pandas as pd
import time
import psutil

# Define memory usage variables
memory_usage_initial = psutil.Process().memory_info().rss
start = time.time()

# Read the dataset into a DataFrame
data = pd.read_csv(
    "data/raw_data/IDVFC_NM_ago23.csv",
    encoding="latin1",
    header=0
)

# Calculate the elapsed time and memory usage
end = time.time()
memory_usage_final = psutil.Process().memory_info().rss

# Results
print(f"RAM used to read dataset: {(memory_usage_final - memory_usage_initial) / 1024 ** 2:.2f} MB")
print(f"Elapsed time to read dataset: {end - start:.2f} minutes")
print(f"Data shape: {data.shape}")
```

##### Results:

```
RAM used to read dataset: 12.11 MB
Elapsed time to read dataset: 0.47 minutes
Data shape: (66240, 21)
```

##### Code:

```py
print(data.head(5))
print(data.columns)
print(data.info())
```

##### Example:

```py
    Año  Clave_Ent         Entidad            Bien jurídico afectado Tipo de delito  Subtipo de delito  ... Julio Agosto Septiembre  Octubre  Noviembre  Diciembre
0  2015          1  Aguascalientes  La vida y la Integridad corporal      Homicidio   Homicidio doloso  ...     0      0        0.0      0.0        0.0        0.0
1  2015          1  Aguascalientes  La vida y la Integridad corporal      Homicidio   Homicidio doloso  ...     0      0        0.0      0.0        0.0        0.0
2  2015          1  Aguascalientes  La vida y la Integridad corporal      Homicidio   Homicidio doloso  ...     0      1        0.0      0.0        0.0        0.0
3  2015          1  Aguascalientes  La vida y la Integridad corporal      Homicidio   Homicidio doloso  ...     0      0        0.0      0.0        0.0        0.0
4  2015          1  Aguascalientes  La vida y la Integridad corporal      Homicidio  Homicidio culposo  ...     0      0        0.0      0.0        0.0        0.0
[5 rows x 21 columns]

Index(['Año', 'Clave_Ent', 'Entidad', 'Bien jurídico afectado',
       'Tipo de delito', 'Subtipo de delito', 'Modalidad', 'Sexo',
       'Rango de edad', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
      dtype='object')
      
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 66240 entries, 0 to 66239
Data columns (total 21 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   Año                     66240 non-null  int64  
 1   Clave_Ent               66240 non-null  int64  
 2   Entidad                 66240 non-null  object 
 3   Bien jurídico afectado  66240 non-null  object 
 4   Tipo de delito          66240 non-null  object 
 5   Subtipo de delito       66240 non-null  object 
 6   Modalidad               66240 non-null  object 
 7   Sexo                    66240 non-null  object 
 8   Rango de edad           66240 non-null  object 
 9   Enero                   66240 non-null  int64  
 10  Febrero                 66240 non-null  int64  
 11  Marzo                   66240 non-null  int64  
 12  Abril                   66240 non-null  int64  
 13  Mayo                    66240 non-null  int64  
 14  Junio                   66240 non-null  int64  
 15  Julio                   66240 non-null  int64  
 16  Agosto                  66240 non-null  int64  
 17  Septiembre              58880 non-null  float64
 18  Octubre                 58880 non-null  float64
 19  Noviembre               58880 non-null  float64
 20  Diciembre               58880 non-null  float64
dtypes: float64(4), int64(10), object(7)
memory usage: 10.6+ MB
```

##### Conclusion

The data exploration revealed the following key findings:

- The dataset has 66,240 rows and 21 columns.
- The months of August through December have significantly fewer data points than the other months, suggesting that there may be missing data in those months.
- The columns have headers.
- Some of the data is not required for the current visualization goals, such as the entity key, federal entity, among others.
- The data types in the dataset are integers, objects, and floats.

##### Additional comments:

```
The execution times and system resource utilization will depend on the underlying hardware and software environment. This is important to keep in mind when interpreting the results of the code, as they may vary depending on the specific environment in which the code is run.
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="data-cleaning"></a>

#### :x: Data Cleaning

##### Objective:

- To optimize resource utilization and implement best practices for data analysis.

##### Method:

- Explore the columns of the dataset to identify the ones that are required for the exploratory analysis.
- Select the required columns and generate a new CSV file.

##### Code:

```py
import pandas as pd
import time
import psutil

# Calculate the initial elapsed time and memory usage.
memory_usage_initial = psutil.Process().memory_info().rss
start = time.time()

# Read the dataset into a Pandas DataFrame.
data = pd.read_csv(
    "data/raw_data/IDVFC_NM_ago23.csv",
    encoding="latin1",
    header=0
)

# Select the required columns.
required_columns = ["Año", "Subtipo de delito", "Sexo",
                    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
data = data[required_columns]

# Write the selected data to a new CSV file.
data.to_csv("data/transformed_data/data.csv", index=False, encoding="utf-8")

# Filter null data
data_null_mask = data.isnull().any(axis=1)
data_null = data[data_null_mask]

# Get the year of each null record
data_null_year = data_null["Año"].unique()

# Calculate the final elapsed time and memory usage.
end = time.time()
memory_usage_final = psutil.Process().memory_info().rss

# Print the results.
print(f"RAM used to read dataset: {(memory_usage_final - memory_usage_initial) / (1024 ** 2):.2f} MB")
print(f"Elapsed time to read dataset: {end - start:.2f} min")
print(f"The null data is located in: {data_null_year}")
print(data.info())
```

##### Example:

```py
RAM used to read dataset: 16.45 MB
Elapsed time to read dataset: 0.61 min
The null data is located in: [2023]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 66240 entries, 0 to 66239
Data columns (total 15 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   Año                66240 non-null  int64  
 1   Subtipo de delito  66240 non-null  object 
 2   Sexo               66240 non-null  object 
 3   Enero              66240 non-null  int64  
 4   Febrero            66240 non-null  int64  
 5   Marzo              66240 non-null  int64  
 6   Abril              66240 non-null  int64  
 7   Mayo               66240 non-null  int64  
 8   Junio              66240 non-null  int64  
 9   Julio              66240 non-null  int64  
 10  Agosto             66240 non-null  int64  
 11  Septiembre         58880 non-null  float64
 12  Octubre            58880 non-null  float64
 13  Noviembre          58880 non-null  float64
 14  Diciembre          58880 non-null  float64
dtypes: float64(4), int64(9), object(2)
memory usage: 7.6+ MB
```

##### Conclusion

The data exploration revealed the following key findings:

- We identified that there is missing data in the months of September to December.
- We also identified the year in which each missing data point occurs.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="data-validation"></a>

#### :o: Data Validation

##### Objective:

- Validate the data to be used in the visualizations that will be created later:
~~~
  - PERCENTAGE OF CRIMES BY PROTECTED LEGAL INTEREST
  - RELATIVE PARTICIPATION OF TOTAL VICTIMS BY GENDER (%)
  - RELATIVE PARTICIPATION OF ALLEGED FEMALE VICTIMS BY CRIME (%)
  - ALLEGED FEMICIDE CRIMES: NATIONAL TREND
~~~
##### Method:

- Structure the business logic.

:one: PERCENTAGE OF CRIMES BY PROTECTED LEGAL INTEREST

##### Code:

```py
# PERCENTAGE OF CRIMES BY PROTECTED LEGAL INTEREST
import pandas as pd
import time
import psutil

# Calculate the initial elapsed time and memory usage.
memory_usage_initial = psutil.Process().memory_info().rss
start = time.time()

# Read the dataset into a Pandas DataFrame.
data = pd.read_csv(
    "data/transformed_data/data.csv",
    encoding="utf-8",
    header=0
)

# Select the required columns.
required_columns = ["Año", "Subtipo de delito", "Enero", "Febrero", "Marzo",
                    "Abril", "Mayo", "Junio", "Julio", "Agosto"]
data = data[required_columns]

# **Filter the data by year**
filter_year = data['Año'] == 2023 
filter_by_year = data[filter_year]
filter_by_year = filter_by_year.drop(columns=['Año'])

# Modeling data
legal_interest_type = filter_by_year.groupby('Subtipo de delito').sum()
legal_interest_sum = legal_interest_type.sum(axis=1)

# Calculate the percentage of each crime type
percentage_vector = (legal_interest_sum / legal_interest_sum.sum()) * 100

# Format the percentage vector
percentage_vector = percentage_vector.apply(lambda x: f"{x:.2f} %")

# Calculate the final elapsed time and memory usage.
end = time.time()
memory_usage_final = psutil.Process().memory_info().rss

# Print the results.
print(f"RAM used to read dataset: {(memory_usage_final - memory_usage_initial) / (1024 ** 2):.2f} MB")
print(f"Elapsed time to read dataset: {end - start:.2f} min")
print(percentage_vector)
```
##### Example:
```py
RAM used to read dataset: 12.30 MB
Elapsed time to read dataset: 0.10 min
Subtipo de delito
Aborto                                                                0.26 %
Corrupción de menores                                                 0.86 %
Extorsión                                                             2.94 %
Feminicidio                                                           0.23 %
Homicidio culposo                                                     5.14 %
Homicidio doloso                                                      7.85 %
Lesiones culposas                                                    18.33 %
Lesiones dolosas                                                     48.74 %
Otros delitos contra la sociedad                                      2.07 %
Otros delitos que atentan contra la libertad personal                 8.76 %
Otros delitos que atentan contra la vida y la integridad corporal     4.31 %
Rapto                                                                 0.02 %
Secuestro                                                             0.20 %
Trata de personas                                                     0.27 %
Tráfico de menores                                                    0.00 %
dtype: object
```
:two: RELATIVE PARTICIPATION OF TOTAL VICTIMS BY GENDER (%)

##### Code:
~~~py
# RELATIVE PARTICIPATION OF TOTAL VICTIMS BY GENDER (%)
import pandas as pd
import time
import psutil

# Calculate the initial elapsed time and memory usage.
memory_usage_initial = psutil.Process().memory_info().rss
start = time.time()

# Read the dataset into a Pandas DataFrame.
data = pd.read_csv(
    "data/transformed_data/data.csv",
    encoding="utf-8",
    header=0
)

# Select the required columns.
required_columns = ["Año", "Sexo", "Enero", "Febrero", "Marzo", 
                    "Abril", "Mayo", "Junio", "Julio", "Agosto"]
data = data[required_columns]

# **Filter the data by year**
filter_year = data['Año'] == 2023 
filter_by_year = data[filter_year]
filter_by_year = filter_by_year.drop(columns=['Año'])

# Modeling data
sum_by_sex = filter_by_year.groupby('Sexo').sum()
vector = sum_by_sex.sum(axis=1)
vector_sum = vector.sum(axis=0)
percentage_vector = (vector / vector.sum()) * 100 

# Format the percentage vector
percentage_vector = percentage_vector.apply(lambda x: f"{x:.2f} %")

# Calculate the final elapsed time and memory usage.
end = time.time()
memory_usage_final = psutil.Process().memory_info().rss

# Print the results.
print(f"RAM used to read dataset: {(memory_usage_final - memory_usage_initial) / (1024 ** 2):.2f} MB")
print(f"Elapsed time to read dataset: {end - start:.2f} min")
print(percentage_vector)
~~~
##### Example:
~~~py
memory_usage_initial) / (1024 ** 2):.2f} MB")
RAM used to read dataset: 11.79 MB
Elapsed time to read dataset: 0.17 min
Sexo
Hombre             55.14 %
Mujer              33.51 %
No identificado    11.35 %
dtype: object
~~~
:three: RELATIVE PARTICIPATION OF ALLEGED FEMALE VICTIMS BY CRIME (%)
##### Code:
~~~py
# RELATIVE PARTICIPATION OF ALLEGED FEMALE VICTIMS BY CRIME (%)
import pandas as pd
import time
import psutil

# Calculate the initial elapsed time and memory usage.
memory_usage_initial = psutil.Process().memory_info().rss
start = time.time()

# Read the dataset into a Pandas DataFrame.
data = pd.read_csv(
    "data/transformed_data/data.csv",
    encoding="utf-8",
    header=0
)

# Select the required columns.
required_columns = ['Año', 'Subtipo de delito','Sexo', "Enero", "Febrero", 
                    "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto"]
data = data[required_columns]

# **Filter the data by year**
filter_year = data['Año'] == 2023 
filter_by_year = data[filter_year]
filter_by_year = filter_by_year.drop(columns=['Año'])

# **Filter the data by sex**
filter = filter_by_year['Sexo'] == 'Mujer'
filter_by_sex = filter_by_year[filter]
filter_sex_int = filter_by_sex.drop(columns=['Sexo'])

sum_by_sex = filter_sex_int.groupby('Subtipo de delito').sum()
vector = sum_by_sex.sum(axis=1)
vector_total = vector.sum(axis=0)

# Percentage
vector_percentage = (vector / vector_total) * 100

# Format the percentage vector
percentage_vector = vector_percentage.apply(lambda x: f"{x:.2f} %")

# Calculate the final elapsed time and memory usage.
end = time.time()
memory_usage_final = psutil.Process().memory_info().rss

# Print the results.
print(f"RAM used to read dataset: {(memory_usage_final - memory_usage_initial) / (1024 ** 2):.2f} MB")
print(f"Elapsed time to read dataset: {end - start:.2f} min")
print(percentage_vector)
~~~
##### Example:
~~~py
RAM used to read dataset: 12.52 MB
Elapsed time to read dataset: 0.10 min
Subtipo de delito
Corrupción de menores                                                 1.44 %
Extorsión                                                             2.96 %
Feminicidio                                                           0.68 %
Homicidio culposo                                                     3.10 %
Homicidio doloso                                                      2.03 %
Lesiones culposas                                                    18.29 %
Lesiones dolosas                                                     54.90 %
Otros delitos contra la sociedad                                      1.27 %
Otros delitos que atentan contra la libertad personal                10.48 %
Otros delitos que atentan contra la vida y la integridad corporal     4.08 %
Rapto                                                                 0.06 %
Secuestro                                                             0.17 %
Trata de personas                                                     0.52 %
Tráfico de menores                                                    0.01 %
dtype: object
~~~
:four: ALLEGED FEMICIDE CRIMES: NATIONAL TREND
##### Code:
~~~py
import pandas as pd
import time
import psutil

memory_usage_initial = psutil.Process().memory_info().rss
start = time.time()

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

month_data = pd.DataFrame.from_dict(data_month_dict)

end = time.time()
memory_usage_final = psutil.Process().memory_info().rss

print(f"RAM used to read dataset: {(memory_usage_final - memory_usage_initial) / (1024 ** 2):.2f} MB")
print(f"Elapsed time to read dataset: {end - start:.2f} min")
# Results
print(month_data)
print(data_year_sum)
~~~
##### Example:
~~~py
RAM used to read dataset: 19.89 MB
Elapsed time to read dataset: 0.19 min
            2015  2016  2017  2018  2019  2020  2021  2022  2023
Enero         33    41    51    71    70    75    76    80    74
Febrero       30    54    69    69    69    92    78    88    76
Marzo         33    70    63    72    81    77   106    78    84
Abril         36    63    62    82    67    73    80    88    64
Mayo          28    52    69    64    81    73   112    90    66
Junio         28    61    77    79    81    98    87    93    82
Julio         37    43    75    84    88    76    72    62    72
Agosto        40    46    70    65    93    75   110    74    67
Septiembre    44    57    56    79    88    82    70    81     0
Octubre       48    48    61    85    73    82    71    85     0
Noviembre     30    63    58    68    81    88    74    82     0
Diciembre     40    50    55   101    96    85    82    75     0
{2015: 427, 2016: 648, 2017: 766, 2018: 919, 2019: 968, 2020: 976, 2021: 1018, 2022: 976, 2023: 585}
~~~

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="data-visialization"></a>

#### :red_circle: Data Visualization

##### Introduction:

This project will create visualizations of a data set of [data set description]. The goals of the project are to [list of goals]. The target audience is [target audience].

##### Objective:

- Once the data is validated, we will create the corresponding visualizations.
~~~
  * PERCENTAGE OF CRIMES BY PROTECTED LEGAL INTEREST
  * RELATIVE PARTICIPATION OF TOTAL VICTIMS BY GENDER (%)
  * RELATIVE PARTICIPATION OF ALLEGED FEMALE VICTIMS BY CRIME (%)
  * ALLEGED FEMICIDE CRIMES: NATIONAL TREND
~~~
- Compare the visualizations with the reference from the source where the data was extracted.

##### Method:

- Create visualizations using the `Matplotlib` library.

:one: PERCENTAGE OF CRIMES BY PROTECTED LEGAL INTEREST


<br />
<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1Ao0QphQzVmPLpyCU7LTNKdEnHgu7I0nI">
<img src="https://drive.google.com/uc?export=view&id=1CYZ5_d8wwdhYQi9De5zRJ_dgygdigpZl">
</div>

~~~py
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
~~~
:two: RELATIVE PARTICIPATION OF TOTAL VICTIMS BY GENDER (%)


<br />
<div align="center">

<img src="https://drive.google.com/uc?export=view&id=1lox1VnzlWFZ4vPEdVRNAUAMOHjC7YVuT">

<img src="https://drive.google.com/uc?export=view&id=1YSyRBjrQFEERnnCdpSvxB4xcxXKWW0mR">

</div>

~~~py
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
    label='Relative participation of total victims by gender (%)*',
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
~~~


:three: RELATIVE PARTICIPATION OF ALLEGED FEMALE VICTIMS BY CRIME (%)


<br />
<div align="center">

<img src="https://drive.google.com/uc?export=view&id=1KyjYkC28Gu97NoCZjg88EQnGs1MbdQIa">

<img src="https://drive.google.com/uc?export=view&id=1K6nn63010rqTRXp3KnsUqjFTTSSZ4rve">

</div>

~~~py
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
~~~

:four: ALLEGED FEMICIDE CRIMES: NATIONAL TREND


<br />
<div align="center">

<img src="https://drive.google.com/uc?export=view&id=1S5JugqaArm8wK-8UWBmNpFdpAKHj-Ozh">

<img src="https://drive.google.com/uc?export=view&id=1XCqenfD3INsyx1i52mJTd-TV9CnFAGxm">

</div>


~~~py
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
~~~

<a name="contributing"></a>

### :bust_in_silhouette: Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! **Thanks again!**

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<a name="license"></a>

### :scroll: License

Distributed under the MIT License. See LICENSE file for more information.

<a name="contact"></a>

### :iphone: Contact

@erwindevdesign - erwindevdesign@gmail.com

Pages: 

<a name="acknowledgments"></a>

### :speech_balloon: Acknowledgments

- [Gitignore file](https://www.toptal.com/developers/gitignore/)
- [Markdown Badges](https://github.com/Ileriayo/markdown-badges)
- [Contributing to projects by GitHub](https://docs.github.com/en/get-started/quickstart/contributing-to-projects?tool=webui)

We extend our gratitude to the author of the reference video for providing valuable insights that contributed to our development.

<a name="additional-resources"></a>

### :page_with_curl: Additional Resources

<div align="center">

[![Government Image Reference](https://www.gob.mx/cms/uploads/press/main_image/157910/post_gobierno_mexico_.jpg)](https://www.gob.mx/sesnsp/acciones-y-programas/incidencia-delictiva-299891?state=published)

</div>

> Executive Secretariat of the National Public Security System. (October 17, 2023). "Common Jurisdiction Victims Figures, 2015 - September 2023". [Dataset File](https://drive.google.com/file/d/1JsXir5EGFMcEjtJKzZSu7hSdEt5zYOX9/view?usp=sharing). Retrieved from the [official government website](https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva?state=published).

> Executive Secretariat of the National Public Security System. (September 25, 2023). "Information on Violence Against Women (Criminal Incidents and 9-1-1 Emergency Calls), August 2023".  [Official Government Website](https://www.gob.mx/sesnsp/articulos/informacion-sobre-violencia-contra-las-mujeres-incidencia-delictiva-y-llamadas-de-emergencia-9-1-1-febrero-2019?idiom=es). [[PDF](https://drive.google.com/file/d/19wXac8xDT4MV8QXK2ZhgrWWoCR9hNBYp/view)].

<div align="center">

[![Video Reference](https://i.ytimg.com/vi/x2DxiL8WOmc/hqdefault.jpg)](https://youtu.be/x2DxiL8WOmc?si=6A3F2v-AETN6EtJM)

</div>

> Mariya MariyaSha. (March 6, 2023). "Reading Large Datasets Quickly - 3 Tips for Improving Data Science Skills". [YouTube](https://www.youtube.com/watch?v=x2DxiL8WOmc).


<!-- ## Additional Resources

For more details on how we implemented this video reference, you can review the source code in our GitHub repository: [Repository Link](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY). -->

<!--

Estructura de referencias bibliograficas:

    Dataset

        > Nombre del organismo emisor. (Año). "Titulo dle dataset". Versión [No. de versión]. [Archivo dataset]. Recuperado de [URL del dataset]

    Video YouTube

        > Nombre del autor, Apellido, Inicial. (Año). Título del video [Archivo de video]. Plataforma. URL

 -->

 <!-- 
 
 Ante posibles errores u omisiones detectados, agradecemos que éstos sean informados al cni@sspc.gob.mx
 
  -->



<br>
<br>
<br>

<div align="center" max-width="70vw" >

<img src="https://drive.google.com/uc?export=view&id=1wBpfw_H6qm9VIMz1Uu50-LUbpypqTMO4">

[@erwindevdesign](https://www.google.com/search?channel=fs&client=ubuntu-sn&q=%40erwindevdesign)

</div>

