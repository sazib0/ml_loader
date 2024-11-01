# ml_loader

`ml_loader` is a Python package to automatically load various data file formats based on file extensions.

## Installation

Install via pip:

    pip install git+https://github.com/sazib0/my_loader.git

or

    pip install ml-loader


## Uses


    import my_loader as ml #import library

##### Define test file paths (you'll need sample files with these formats)

    test_files = [
        'sample.csv',         # CSV file
        'sample.xlsx',        # Excel file
        'sample.json',        # JSON file
        'sample.txt',         # Text file
        'sample.parquet',     # Parquet file
        'sample.h5',          # HDF5 file
        'sample.sav',         # SPSS file
        'sample.dta',         # Stata file
        'sample.xml',         # XML file
        'sample.jpg'          # Image file
    ]

    for file in test_files:
        try:
            data = ml.load_data(file)
            print(f"Successfully loaded {file}")
            print(type(data))  # Print type of data to verify the content
        except Exception as e:
            print(f"Failed to load {file}: {e}")
           
Example

    import my_loader as ml
    
    data = ml.load_data('sample.csv')  
    print(data.head())



