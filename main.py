import openpyxl
from openpyxl import Workbook
import pathlib

arquivo = Workbook()

arquivo.save("cliente.xlsx")