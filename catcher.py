import pandas as pd
import requests

# WE PROCESS THE TXT FILE WITH THE GOOGLE SHEETS ID IN IT
def get_sheet():
    with open('sheet_id.txt', "r") as f:
        sheet_ID = f.readline().strip()
        while True:
            # WE CALL THE URL OF THE GOOGLE SHEET WITH THE ID
            url = f'https://docs.google.com/spreadsheets/d/{sheet_ID}/gviz/tq?tqx=out:csv&sheet=/'
            # CATCH 'EM ALL!
            url_catcher = pd.read_csv(url, header=1)

            return url_catcher.head()
        
print(get_sheet())