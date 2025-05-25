import pdfplumber
import pandas as pd
from tabulate import tabulate

pdf_file = 'Vypis_816605002_CZK_2024_6.pdf'
pdf = pdfplumber.open(f"pdf/{pdf_file}")

#Load page_0
p0 = pdf.pages[0]
table = p0.extract_table()

df = pd.DataFrame(table[1:], columns=table[0])
print(tabulate(df, headers='keys', tablefmt='psql'))


# csv_file = f'csv/{pdf_file[:-4]}.csv'
# with open(csv_file, 'w') as csv_file:
#     df.to_csv(csv_file, index=False)