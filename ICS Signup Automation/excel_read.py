import xlrd
from xlrd.sheet import ctype_text
import os

# fetching all values from excel sheet in data folder
a = "true"


def get_tenant_list(file_name):
    workbook_path = os.getcwd() + '/Data/' + file_name

    # Open the workbook
    xl_workbook = xlrd.open_workbook(workbook_path)

    # List sheet names, and pull a sheet by name
    #

    sheet_names = xl_workbook.sheet_names()

    xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])

    xl_sheet = xl_workbook.sheet_by_index(0)

    # Pull the first row by index
    #  (rows/columns are also zero-indexed)
    row = xl_sheet.row(0)  # 2nd row

    tenant_list = []

    for row_idx in range(1, xl_sheet.nrows):  # Iterate through rows

        email = xl_sheet.cell(row_idx, 5).value
        first_name = xl_sheet.cell(row_idx, 3).value
        last_name = xl_sheet.cell(row_idx, 2).value
        phone_number = xl_sheet.cell(row_idx, 4).value
        unit_number = str(int(xl_sheet.cell(row_idx, 1).value))
        address = str(int(xl_sheet.cell(row_idx, 0).value))
        print(type(unit_number))
        print(type(address))

        person = Tenant(first_name, last_name, phone_number, email, unit_number, address)

        tenant_list.append(person)

    return tenant_list


class Tenant:

    def __init__(self, first_name='', last_name='', phone_number='', email='', unit_number='', address=''):
        self.address = address
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.unit_number = unit_number
