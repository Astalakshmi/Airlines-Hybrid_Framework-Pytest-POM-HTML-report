import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:
    popup_javascript_code = "return document.querySelector('#cookieBannerMessage > ""adc-cookie-banner').shadowRoot.querySelector(""'#toast-dismiss-button').shadowRoot.querySelector('#button')"

    from_search_box_xpath = "//div[@class='row-form normalLayout']//input[""@id='reservationFlightSearchForm.originAirport']"

    to_search_box_xpath = "//div[@class='row-form normalLayout']//input[""@id='reservationFlightSearchForm.destinationAirport']"

    dropdown_passenger_xpath = "//div[@class='row-form normalLayout']//select[""@id='flightSearchForm.adultOrSeniorPassengerCount']"

    depart_datepicker_xpath = "//*[@id='reservationFlightSearchForm']/div[4]/div[1]/div/button"  # OPEN DATEPICKER depart textbox path

    return_datepicker_xpath = "//*[@id='reservationFlightSearchForm']/div[4]/div[2]/div/button"  # open datepicker return textbox xpath

    loop_month_xpath = "//*[@id='ui-datepicker-div']/div[1]/div/div/span[1]"

    loop_year_xpath = "//*[@id='ui-datepicker-div']/div[1]/div/div/span[2]"

    loop_else_option = "#ui-datepicker-div > div.ui-datepicker-group.ui-datepicker-group-last > div > a"

    select_date_xpath = "//tbody/tr/td/a"

    search_button_xpath = "//div[@class='row-form aa-flightSearchForm-datesRow']//div[""@id='flightSearchFormSubmitButton']//div//input[""@id='flightSearchForm.button.reSubmit']"

    def __init__(self, driver):
        self.driver = driver

    def Dismiss_popup(self):
        # Shadow Dom-->Shadow Root--->Dismiss the popup
        # using javascript executor code
        Dismiss = self.driver.execute_script(self.popup_javascript_code)
        self.driver.execute_script("arguments[0].click();", Dismiss)

    def setFromSearchBox(self, from_airport):
        self.driver.find_element(By.XPATH, self.from_search_box_xpath).click()
        self.driver.find_element(By.XPATH, self.from_search_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.from_search_box_xpath).send_keys(from_airport)

    def setToSearchBox(self, to_airport):
        self.driver.find_element(By.XPATH, self.to_search_box_xpath).send_keys(to_airport)

    def setDropdownPassenger(self, number_passenger):
        dropdown = Select(self.driver.find_element(By.XPATH, self.dropdown_passenger_xpath))
        dropdown.select_by_index(number_passenger)

    def setDepartDate(self):
        self.driver.find_element(By.XPATH, self.depart_datepicker_xpath).click()
        year = "2024"
        month = "May"
        date = "28"
        while True:
            mon = self.driver.find_element(By.XPATH, self.loop_month_xpath).text
            yr = self.driver.find_element(By.XPATH, self.loop_year_xpath).text

            if mon == month and yr == year:
                break
            else:
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, self.loop_else_option).click()
        # selecting Date Depart
        dates = self.driver.find_elements(By.XPATH, self.select_date_xpath)
        for d in dates:
            if d.text == date:
                d.click()
                break

    def setReturnDate(self):
        self.driver.find_element(By.XPATH, self.return_datepicker_xpath).click()
        year_return = "2024"
        month_return = "August"
        date_return = "30"
        while True:
            mon = self.driver.find_element(By.XPATH, self.loop_month_xpath).text
            yr = self.driver.find_element(By.XPATH, self.loop_year_xpath).text

            if mon == month_return and yr == year_return:
                break
            else:
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, self.loop_else_option).click()
        dates1 = self.driver.find_elements(By.XPATH, self.select_date_xpath)
        for d1 in dates1:
            if d1.text == date_return:
                d1.click()
                break

    def setSearchButton(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).submit()
