import time

import pytest

from pageObjects.HomePage import HomePage
from Utilities.homepageLogger import LogGen


@pytest.mark.usefixtures("setup_and_teardown")
class Test_001_HomePage:
    logger = LogGen.loggen()

    def test_homepage_title(self):
        self.logger.info("**********************Test_001_HomePage*********************")
        self.logger.info("**********************Verifying Home Page Title*************")
        home_page = HomePage(self.driver)
        home_page.act_title = self.driver.title
        if home_page.act_title == "American Airlines - Airline tickets and low fares at aa.com":
            assert True
            self.logger.info("**********************Home Page Title is Passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.logger.error("**********************Verifying Home Page TItle is Failed*************")
            assert False

    def test_booking_flights(self):
        self.logger.info("**********************Verifying Booking_Flights_Functionality*************")
        home_page = HomePage(self.driver)
        home_page.Dismiss_popup()
        time.sleep(5)
        home_page.setFromSearchBox("SFO")
        home_page.setToSearchBox("MAA")
        home_page.setDropdownPassenger(5)
        home_page.setDepartDate()
        time.sleep(2)
        home_page.setReturnDate()
        time.sleep(2)
        home_page.setSearchButton()  # SUBMIT BUTTON
        time.sleep(100)
        # home_page.act_title = self.driver.title
        # if home_page.act_title == "Book flights - Book round trip, one way, multi city - American Airlines" :  # REDIRECT TO NEXT PAGE
        if self.driver.current_url == "https://www.aa.com/booking/choose-flights/1":
            time.sleep(20)
            assert True
            self.logger.info("**********************Successfully Redirect to Flight 1 - Choose flights page *************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_book_tab.png")
            self.logger.error("**********************Failed something went wrong while Booking Flights *************")
            assert False



#"Book flights - Book round trip, one way, multi city - American Airlines"

#"Flight 1 - Choose flights - American Airlines"