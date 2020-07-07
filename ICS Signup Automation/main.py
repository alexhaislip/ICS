from webauto import logging_in
from selenium import webdriver
import os
import pyautogui
from excel_read import get_tenant_list
from webauto import find_address, find_unit, nav_search_bar

"""

Questions:

are the excel files generated?
will they be the same every time?

"""

"""
process for signupAutomation:

(1.) find by tenant phone number
    if not found : 
        search by email
            if email is empty then search the address
                if the address is not found, make new user (2.)

    if email or phone number found :
        click the user and update new info

(2.) finding a room to add a tenant from address

"""


def main():
    chromedriver_path = os.getcwd() + '/chromedriver'
    driver = webdriver.Chrome(chromedriver_path)
    logging_in(driver)
    tenant_list = get_tenant_list('sheet1.xlsx')
    for tenant in tenant_list:
        print(tenant.first_name)
        print(tenant.last_name)
        print(tenant.phone_number)
        print(tenant.email)
        print(tenant.unit_number)
        print(tenant.address)
        print("-" * 40)
        nav_search_bar(driver)
        find_address(driver, tenant)
        find_unit(driver, tenant)


    # alert the user the program has ended
    pyautogui.alert(text='Program has finished', title='Alert', button='OK')



if __name__ == '__main__':
    main()
