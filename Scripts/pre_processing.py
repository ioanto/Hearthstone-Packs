import pandas as pd

def data_diagnostics(input_file):
    """
    Load an Excel file, perform data diagnostics, and identify sequentially missing packs.

    Args:
        input_file (str): Path to the Excel file containing pack opening data.

    Returns:
        tuple or None: A tuple containing the DataFrame with pack opening data and a boolean indicating
        whether there are sequentially missing packs. Returns None if an error occurs.
    """
    try:
        # Load the Excel file into a DataFrame
        data = pd.read_excel(input_file)
        data_copy = data.copy()
        print(data_copy.head())

        # Check for sequentially missing packs in the first column
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
    """
    Fill missing values (NaNs) in a DataFrame with 0.

    Args:
        dataframe (DataFrame): Input DataFrame containing missing values.

    Returns:
        DataFrame or None: DataFrame with missing values filled with 0. Returns None if an error occurs.
    """
    try:
        dataframe.fillna(0, inplace=True)  # Fill missing values with 0 inplace
        return dataframe
      
    except Exception:
        print("Error: An unexpected error occurred.")
        return None

def valid_data(dataframe):
    """
    Identify packs with invalid data based on the sum of card counts.

    Args:
        dataframe (DataFrame): Input DataFrame containing card count data.

    Returns:
        None: Prints indices of packs with invalid data. Returns None.
    """
    try:
        # Calculate the sum of card counts in each row, omitting the first column
        row_sums = dataframe.iloc[:, 1:].sum(axis=1)
        
        # Initialize a list to store indices of packs with invalid data
        problematic_packs = []

        # Iterate through each row sum and check for invalid data
        for index, row_sum in enumerate(row_sums):
            if row_sum != 5:
                problematic_packs.append(index)  # Add index to list if sum is not 5
        
        # Print indices of packs with invalid data, if any
        if len(problematic_packs) > 0:
            print(f"The following pack indices are missing cards:\n{problematic_packs}")

        return None
    
    except Exception:
        print("Error: An unexpected error occurred.")
        return None
