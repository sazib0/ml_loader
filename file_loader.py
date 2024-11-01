# file_loader.py
import pandas as pd
import pyreadstat
from PIL import Image
from sqlalchemy import create_engine
import os

def load_data(filepath):
    # Get the file extension
    _, file_extension = os.path.splitext(filepath)
    file_extension = file_extension.lower()

    # File type detection and reading
    if file_extension == '.csv':
        return pd.read_csv(filepath)
    elif file_extension in ['.xls', '.xlsx']:
        return pd.read_excel(filepath)
    elif file_extension == '.json':
        return pd.read_json(filepath)
    elif file_extension == '.txt':
        return pd.read_csv(filepath, delimiter='\t')
    elif file_extension == '.parquet':
        return pd.read_parquet(filepath)
    elif file_extension == '.h5':
        return pd.read_hdf(filepath)
    elif file_extension == '.sav':
        data, _ = pyreadstat.read_sav(filepath)
        return data
    elif file_extension == '.dta':
        return pd.read_stata(filepath)
    elif file_extension == '.xml':
        return pd.read_xml(filepath)
    elif file_extension in ['.png', '.jpg', '.jpeg']:
        return Image.open(filepath)
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")
