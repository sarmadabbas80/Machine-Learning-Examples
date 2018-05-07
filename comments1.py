import os
import pandas as pd

os.chdir('C:\\Users\\sabbas6\\Desktop\\Python')
os.getcwd()

file = 'MRCS_KMI_Client_201705.xlsx'

xl = pd.ExcelFile(file)

print(xl.sheet_names)

dfl1 = xl.parse('7148220-MAY_KMI_Client')

dfl1.describe()
