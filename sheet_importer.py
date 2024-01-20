import pandas as pd


def pullexcel(file_name, loc_index=0, vol_index=1):
    print("Reading spreadsheet data...")
    xl_data = pd.read_excel(file_name, engine="openpyxl")
    commands = [(item[loc_index], item[vol_index]) for item in xl_data.itertuples(index=False)]
    print("Finished reading spreadsheet.")
    return commands