import pandas as pd

bank_data = pd.read_html(
    "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/")

bank_data[0].to_excel('pandas/assets/bank_data.xlsx',
                      sheet_name='html_to_excel', index=None)
