import pandas as pd
import time

start = time.time() 
data = pd.read_csv(
    "data.csv", 
    encoding='latin1', 
    usecols=['Año', 'Entidad', 'Municipio', 'Bien jurídico afectado', 'Tipo de delito', 'Modalidad' ],
    chunksize= 50000
)

# Access the chunk data
for idx, chunk in enumerate(data):
    """ Iterates through a dataset in chunks, extracting specific information from the chunk data.

    Parameters:
    - data: pandas.io.parsers.TextFileReader
        A text file reader containing the dataset.

    Functionality:
    - The code iterates through the dataset using the enumerate function.
    - It processes each chunk of data.
    - If the index is 0, indicating the first chunk, the chunk is converted into a pandas DataFrame.
    """
    if idx == 0:
        df = pd.DataFrame(chunk)
        df['Municipio'][50] = 'Lalaland'
        print(df['Municipio'][50])
    else:
        break

# fisrt explorate
print('FILE LOADED! this operation took', time.time()-start, 'seconds')
#print('Data Shape: ', data.shape)

# identify the specific data
#print(data.columns)