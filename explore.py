import pandas as pd
import time

start = time.time() 
data = pd.read_csv(
    "data.csv", 
    encoding='latin1', 
    usecols=['Año', 'Entidad', 'Municipio', 'Bien jurídico afectado', 'Tipo de delito', 'Modalidad' ]
)

#data.to_csv('modified_data.csv', index=False, encoding='utf-8')

#new_data = pd.read_csv('modified_data.csv')

print('FILE LOADED! this operation took', time.time()-start, 'seconds')
print('Data Shape: ', data.shape)

