from selenium import webdriver
import time as t
from selenium.webdriver.common.keys import Keys


def logging_in(driver):
    # log in with username and password
    user_name = "ahaislip"
    password = "Password1$"
    driver.get("https://signup.ics-llc.net/")
    element = driver.find_element_by_xpath("//*[@id='body']/div/div[2]/div/form/input[3]")
    element.send_keys(user_name)
    element = driver.find_element_by_xpath("//*[@id='body']/div/div[2]/div/form/input[4]")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)


def find_address(driver, user):
    """
    spiked version of finding the address, will need revisions for other addresses...

    """

    user_address = driver.find_element_by_xpath('//*[@id="q"]')
    user_address.clear()
    user_address.send_keys(str(user.address))
    search_button = driver.find_element_by_xpath('//*[@id="subbut"]')
    search_button.click()
    t.sleep(1)
    property_link = driver.find_element_by_xpath('//*[@id="prop_content"]/table/tbody/tr[3]')
    property_link.click()


def find_unit(driver, user):
    t.sleep(3)
    search = driver.find_element_by_xpath('//*[@id="table-filter"]')

    if int(str(user.unit_number)) < 10:
        search.send_keys('0' + str(user.unit_number))
    else:
        search.send_keys(str(user.unit_number))

    t.sleep(1)

    table_body = driver.find_element_by_xpath('//*[@id="units-table"]/tbody')
    list_of_units = table_body.find_elements_by_tag_name('tr')

    for unit in range(0, len(list_of_units) - 1):
        table_body = driver.find_element_by_xpath('//*[@id="units-table"]/tbody')
        list_of_units = table_body.find_elements_by_tag_name('tr')
        print(len(list_of_units))
        t.sleep(1)
        list_of_units[unit].click()
        table_body = driver.find_element_by_xpath('//*[@id="content-panel"]/div[4]/div/table/tbody')
        table_rows = table_body.find_elements_by_tag_name('tr')

        t.sleep(2)

        for row in table_rows:
            row_cols = row.find_elements_by_tag_name('td')
            if len(row_cols) == 0:
                continue
            print(len(row_cols))
            name = row_cols[1]

            print(user.first_name + ' ' + user.last_name)
            if name.text.lower() == (user.first_name + ' ' + user.last_name).lower():
                print("user found...")
                name.click()
                update_user(driver, user)
                return

        back_to_building = driver.find_element_by_xpath('//*[@id="content-panel"]/div[1]/div/div[2]/span[2]/a[1]')
        back_to_building.click()

        t.sleep(3)

        search = driver.find_element_by_xpath('//*[@id="table-filter"]')

        if int(str(user.unit_number)) < 10:
            search.send_keys('0' + str(user.unit_number))
        else:
            search.send_keys(str(user.unit_number))

    t.sleep(1)

    first_unit = driver.find_element_by_xpath('//*[@id="units-table"]/tbody/tr[1]')
    first_unit.click()

    tenant_button = driver.find_element_by_xpath('//*[@id="add_tenant"]')
    tenant_button.click()

    create_new_user_button = driver.find_element_by_xpath('//*[@id="new_user"]')
    create_new_user_button.click()

    create_user(driver, user)


def nav_search_bar(driver):
    search_button = driver.find_element_by_xpath('//*[@id="Tenants-link"]')
    search_button.click()
    property_button = driver.find_element_by_xpath('//*[@id="prop"]')
    property_button.click()


def tenant_selection(driver):
    tenant = driver.find_element_by_xpath('//*[@id="Tenants-link"]')
    tenant.click()


def create_user(driver, user):
    first_name_input = driver.find_element_by_xpath('//*[@id="content-panel"]/div/form/table/tbody/tr[1]/td[2]/input')
    first_name_input.clear()
    first_name_input.send_keys(user.first_name)
    last_name_input = driver.find_element_by_xpath('//*[@id="content-panel"]/div/form/table/tbody/tr[2]/td[2]/input')
    last_name_input.clear()
    last_name_input.send_keys(user.last_name)
    email_input = driver.find_element_by_xpath('//*[@id="content-panel"]/div/form/table/tbody/tr[3]/td[2]/input')
    email_input.clear()
    email_input.send_keys(user.email)
    phone_input = driver.find_element_by_xpath('//*[@id="content-panel"]/div/form/table/tbody/tr[4]/td[2]/input')
    phone_input.clear()
    phone_input.send_keys(user.phone_number)
    submit = driver.find_element_by_xpath('//*[@id="content-panel"]/div/form/button')
    submit.click()
    nav_search_bar(driver)


def update_user(driver, user):
    first_name_input = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form[2]/div[4]/div[1]/div/input[1]')
    first_name_input.clear()
    first_name_input.send_keys(user.first_name)
    last_name_input = driver.find_element_by_xpath('//*[@id="content-panel"]/form[2]/div[4]/div[1]/div/input[2]')
    last_name_input.clear()
    last_name_input.send_keys(user.last_name)
    email_input = driver.find_element_by_xpath('//*[@id="content-panel"]/form[2]/div[4]/div[1]/div/input[3]')
    email_input.clear()
    email_input.send_keys(user.email)
    phone_input = driver.find_element_by_xpath('//*[@id="content-panel"]/form[2]/div[4]/div[1]/div/input[4]')
    phone_input.clear()
    phone_input.send_keys(user.phone_number)
    submit = driver.find_element_by_xpath('//*[@id="saveform"]')
    submit.click()
    nav_search_bar(driver)
