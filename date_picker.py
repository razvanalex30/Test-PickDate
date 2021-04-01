from datetime import datetime

from selenium import webdriver
from driver_creation import SeleniumLibraryExt
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class DatePicker:
    
    @staticmethod
    def date_parse(date_dict):
        month = datetime.strptime(date_dict["Month"], "%B")
        day = datetime.strptime(str(date_dict["Day"]), "%d")
        year = datetime.strptime(str(date_dict["Year"]), "%Y")
        date = month.strftime("%m") + "/" + day.strftime("%d") + "/" + year.strftime("%Y")
        return date

    @staticmethod
    def time_parse(time_dict):
        hour = datetime.strptime(str(time_dict["Hour"]), "%H")
        minute = datetime.strptime(str(time_dict["Minute"]), "%M")
        time = hour.strftime("%H") + ":" + minute.strftime("%M")
        return time

    @staticmethod
    def textbox_parse(textbox, input_string):
        textbox.send_keys(Keys.CONTROL + "a")
        textbox.send_keys(Keys.DELETE)
        textbox.send_keys(input_string)
        textbox.send_keys(Keys.RETURN)

    def select_date(self, date_selected):
        self.driver = SeleniumLibraryExt.create_driver()
        date_dict = dict()
        self.driver.find_element_by_xpath("//input[@id='datePickerMonthYearInput']").click()
        self.driver.find_element_by_xpath("//select[@class='react-datepicker__month-select']").click()
        date_dict[
            'Month'] = f"//select[@class='react-datepicker__month-select']//option[text()='{date_selected['Month']}']"
        self.driver.find_element_by_xpath("//select[@class='react-datepicker__year-select']").click()
        date_dict[
            'Year'] = f"//select[@class='react-datepicker__year-select']//option[text()='{date_selected['Year']}']"
        date_dict['Day'] = f"//div[text()='{date_selected['Day']}'][not(contains(@class,'--outside-month'))]"
        for key in date_dict:
            self.driver.find_element_by_xpath(date_dict[key]).click()

    def input_date(self, date_selected):
        self.driver = SeleniumLibraryExt.create_driver()
        date = self.date_parse(date_selected)
        date_textbox = self.driver.find_element_by_xpath("//input[@id='datePickerMonthYearInput']")
        self.textbox_parse(date_textbox, date)

    def input_date_time(self, date_time_selected):
        self.driver = SeleniumLibraryExt.create_driver()
        date = self.date_parse(date_time_selected)
        time = self.time_parse(date_time_selected)
        date_time = date + " " + time
        date_time_textbox = self.driver.find_element_by_xpath("//input[@id='dateAndTimePickerInput']")
        self.textbox_parse(date_time_textbox, date_time)