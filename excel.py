import pandas as pd

file = "C:\doc\EXCEL MARKSHEET.xlsx"
sheet1 = pd.read_excel(file, 
                        sheet_name = 0, 
                        index_col = 0)

sheet2 = pd.read_excel(file, 
                        sheet_name = 1, 
                        index_col = 0)

# concatinating both the sheets
newData = pd.concat([sheet1, sheet2])
print(newData.tail())

