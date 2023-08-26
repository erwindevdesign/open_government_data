# Data Exploration and Optimization Analysis

This analysis is conducted to implement best practices in the utilization and exploration of large-scale datasets, aiming to minimize resource consumption on the device where the analysis is performed. 

*Execution times and system resource utilization will depend on the capacity of the underlying hardware.*

For efficient data handling, it's essential to consider:

* Prioritize Relevant Data.

* Load data in small chunks.

* Access and change data chunks values.

* Save modified data into a new csv* file.

* Employing optimal algorithms for processing large datasets.
    
* Utilizing memory-efficient techniques to mitigate resource usage.
    
* Fine-tuning execution parameters based on available hardware capacity.


By following these practices, we aim to enhance the efficiency of our data analysis processes while achieving a more sustainable use of system resources.

<!-- Este analisis se realiza para la aplicación de mejores lracticas en el uso y exploración de datos de gran tamaño, logrando aminorar el uso de recursos del dispositibo donde se realice el analisis. Los tiempos de ejecución y el uso de recursos del sistema dependera de la capasidad del mismo. -->

### Dataset size

    Municipal-Delitos-2015-2023_jul2023.csv

    - Type: Documento CSV (text/csv)
    - Size: 305.5 MB
    - Data Shape:  (2075738, 21)
    - FILE LOADED! this operation took 44.671736001968384 seconds
    - Rename: data.csv

### Setting Up the Work Environment

We will create the file **"explore.py"** to initiate the data exploration process. We'll import the necessary dependencies and libraries that will aid in the exploratory analysis of data extracted from the "data.csv" file. We will also modify the parameter encoding= to **'latin1'** to ensure standardization of characters that the data may contain.

~~~py
# explore.py
import pandas as pd
import time

start = time.time() 
data = pd.read_csv(
    "data.csv", 
    encoding='latin1'
)
~~~

### Initial Data Exploration

In this phase, we will conduct a comprehensive test on the entire dataset, serving as a time benchmark. This benchmark will be used for performance comparison as we progress through the data exploration process. The aim is to optimize resource utilization and implement best practices for data analysis.

~~~py
# explore.py
import pandas as pd
import time

start = time.time() 
data = pd.read_csv(
    "data.csv", 
    encoding='latin1'
)

print('FILE LOADED! this operation took', time.time()-start, 'seconds')
print('Data Shape: ', data.shape)
~~~
~~~sh
# console
❯ python3 explore.py

FILE LOADED! this operation took 12.577690839767456 seconds
Data Shape:  (2075738, 21)
~~~


### Prioritize Relevant Data.

**Explore column data**

After understanding the dataset's size and structure, the next step is to identify the specific data with which we will be working. This will be determined by the business logic or the objectives of the analysis.

~~~py
# explore.py
import pandas as pd
import time

start = time.time() 
data = pd.read_csv(
    "data.csv", 
    encoding='latin1'
)

print(data.columns) # identify the specific data
~~~
~~~sh
# console
❯ python3 explore.py

Index(['Año', 'Clave_Ent', 'Entidad', 'Cve. Municipio', 'Municipio',
       'Bien jurídico afectado', 'Tipo de delito', 'Subtipo de delito',
       'Modalidad', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
      dtype='object')
~~~

**Column Selection for Exploratory Analysis**

From the exploration of the columns, we will select the ones required for our exploratory analysis.

~~~py
# explore.py
import pandas as pd
import time

start = time.time() 
data = pd.read_csv(
    "data.csv", 
    encoding='latin1', 
    usecols=['Año', 'Entidad', 'Municipio', 'Bien jurídico afectado', 'Tipo de delito', 'Modalidad' ]
)

print('FILE LOADED! this operation took', time.time()-start, 'seconds')
print('Data Shape: ', data.shape)
~~~
~~~sh
# console
❯ python3 explore.py

FILE LOADED! this operation took 2.9510388374328613 seconds
Data Shape:  (2075738, 6)
~~~

**chunksize Value**

To optimize data exploration times within the dataset, we will employ the **chunksize=** option to limit the number of rows under exploration. This approach aims to reduce exploration times significantly.

~~~py
import pandas as pd
import time

start = time.time() 
data = pd.read_csv(
    "data.csv", 
    encoding='latin1', 
    usecols=['Año', 'Entidad', 'Municipio', 'Bien jurídico afectado', 'Tipo de delito', 'Modalidad' ],
    chunksize= 50000
)

print('FILE LOADED! this operation took', time.time()-start, 'seconds')
~~~
~~~sh
# console
❯ python3 explore.py

FILE LOADED! this operation took 0.06291007995605469 seconds
~~~

### Load data in small chunks.

**Chunk Size Value**

To optimize data exploration times within the dataset, we will employ the **chunksize=** option to limit the number of rows under exploration. This approach aims to reduce exploration times significantly.

~~~py
# explore.py
import pandas as pd
import time

start = time.time() 
data = pd.read_csv(
    "data.csv", 
    encoding='latin1', 
    usecols=['Año', 'Entidad', 'Municipio', 'Bien jurídico afectado', 'Tipo de delito', 'Modalidad' ],
    chunksize= 50000 # chunksize value
)

print('FILE LOADED! this operation took', time.time()-start, 'seconds')
~~~
~~~sh
# console
❯ python3 better_data_science_skills.py

FILE LOADED! this operation took 0.0022623538970947266 seconds
~~~

### Access and change data

~~~py
# exlore.py
import pandas as pd
import time

start = time.time() 
data = pd.read_csv(
    "data.csv", 
    encoding='latin1', 
    usecols=['Año', 'Entidad', 'Municipio', 'Bien jurídico afectado', 'Tipo de delito', 'Modalidad' ],
    chunksize= 50000
)

for idx, chunk in enumerate(data):
    if idx == 0:
        print(chunk)
    else:
        break

print('FILE LOADED! this operation took', time.time()-start, 'seconds')
~~~
~~~sh
# console
❯ python3 explore.py

        Año         Entidad  ... Tipo de delito                 Modalidad
0      2015  Aguascalientes  ...      Homicidio         Con arma de fuego
1      2015  Aguascalientes  ...      Homicidio           Con arma blanca
2      2015  Aguascalientes  ...      Homicidio         Con otro elemento
3      2015  Aguascalientes  ...      Homicidio           No especificado
4      2015  Aguascalientes  ...      Homicidio         Con arma de fuego
...     ...             ...  ...            ...                       ...
49995  2015         Hidalgo  ...       Lesiones  En accidente de tránsito
49996  2015         Hidalgo  ...       Lesiones         Con otro elemento
49997  2015         Hidalgo  ...       Lesiones           No especificado
49998  2015         Hidalgo  ...    Feminicidio         Con arma de fuego
49999  2015         Hidalgo  ...    Feminicidio           Con arma blanca

[50000 rows x 6 columns]
FILE LOADED! this operation took 0.48381972312927246 seconds
~~~

### Accessing a Specific Field

This section demonstrates how to access a specific field within the dataset while processing it in chunks.

~~~py
# explore.py

import pandas as pd
import time

start = time.time() 
data = pd.read_csv(
    "data.csv", 
    encoding='latin1', 
    usecols=['Año', 'Entidad', 'Municipio', 'Bien jurídico afectado', 'Tipo de delito', 'Modalidad' ],
    chunksize= 50000
)

for idx, chunk in enumerate(data):
    if idx == 0:
        df = pd.DataFrame(chunk)
        print(df['Municipio'][50])
    else:
        break

print('FILE LOADED! this operation took', time.time()-start, 'seconds')
~~~
~~~sh
# console
❯ python3 explore.py

Aguascalientes
FILE LOADED! this operation took 0.25665283203125 seconds
~~~

### Modifying a Single Value

This section demonstrates how to modify a single value within the dataset while processing it in chunks.

~~~py
# explore.py
import pandas as pd
import time

start = time.time() 
data = pd.read_csv(
    "data.csv", 
    encoding='latin1', 
    usecols=['Año', 'Entidad', 'Municipio', 'Bien jurídico afectado', 'Tipo de delito', 'Modalidad' ],
    chunksize= 50000
)

for idx, chunk in enumerate(data):
    if idx == 0:
        df = pd.DataFrame(chunk)
        df['Municipio'][50] = 'Lalaland' # change new data
        print(df['Municipio'][50])
    else:
        break

print('FILE LOADED! this operation took', time.time()-start, 'seconds')
~~~
~~~sh
# console
Lalaland
FILE LOADED! this operation took 0.2867546081542969 seconds
~~~

### Modified data to new csv

~~~py
# explore.py

~~~
~~~sh

~~~

~~~py
# explore.py

~~~
~~~sh

~~~

## Bibliographic References

Dataset

[![Incidencia delictiva](data:image/jpeg;base64,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)](https://www.gob.mx/sesnsp/acciones-y-programas/incidencia-delictiva-299891?state=published)

> Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública. (2023). "Municipal-Delitos-2015-2023_jul2023.csv". Recuperado de [https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva?state=published] [https://www.gob.mx/sesnsp/acciones-y-programas/incidencia-delictiva-299891?state=published]

Video reference

[![reference video](https://i.ytimg.com/vi/x2DxiL8WOmc/hqdefault.jpg)](https://youtu.be/x2DxiL8WOmc?si=6A3F2v-AETN6EtJM)

> Mariya MariyaSha. (2023).[ Read Giant Datasets Fast - 3 Tips For Better Data Science Skills](https://www.youtube.com/watch?v=x2DxiL8WOmc). YouTube. 

### Attributions

We extend our gratitude to the author of the reference video for providing valuable insights that contributed to our development.

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