import pandas as pd

def data_diagnostics(input_file):
    
    try:
        data = pd.read_excel(input_file)
        data_copy = data.copy()
        print(data_copy.head())

        if data_copy.columns[0].diff().dropna().eq(1).all() == True:
            print("No sequentially missing packs.")
            return data_copy, True
        else:
            print("There are sequentially missing packs.")
            return data_copy, False

    except FileNotFoundError:
        print("Error: File is not found.")
        return None
    
    except Exception:
        print("Error: An unexpected error occured.")
        return None

def missing_values(dataframe):
    
    try:
        dataframe.fillna(0, inplace = True)
        return dataframe
    
    except Exception:
        print("Error: An unexpected error occured.")
        return None

def valid_data(dataframe):
    try:
        row_sums = dataframe.iloc[:,1:].sum(axis = 1)
        problematic_packs = []

        for index, row_sum in enumerate(row_sums):
            if row_sum != 5:
                problematic_packs.append(index)
        
        if len(problematic_packs) > 0:
            print(f"The following pack indices are missing cards:\n{problematic_packs}")
        
        return None
    
    except Exception:
        print("Error: An unexpected error occured.")
        return None