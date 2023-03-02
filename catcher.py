import pandas as pd

# WE PROCESS THE TXT FILE WITH THE GOOGLE SHEETS ID IN IT
with open('sheet_id.txt') as f:
    sheet_ID = f.readlines()

sheet_name = "AAPL"

# WE CALL THE URL OF THE GOOGLE SHEET WITH THE ID
url = f'https://docs.google.com/spreadsheets/d/{sheet_ID}/gviz/tq?tqx=out:csv&sheet=/{sheet_name}'

# CATCH 'EM ALL!
url_catcher = pd.read_csv(url)
print(url_catcher.head())
