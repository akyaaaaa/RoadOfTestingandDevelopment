from openpyxl import load_workbook
wb = load_workbook('person.xlsx')
sheet_name = wb['Sheet']
print(sheet_name['B3'].value)