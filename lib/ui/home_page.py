from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    def get_logout_button(self):
        try:
            return self.driver.find_element_by_xpath("//a[text()='Logout']")
        except:
            return None

    def get_user_tab(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='Users']")
        except:
            return None

    def get_time_drop_down(self):
        try:
            return self.driver.find_element_by_xpath("//span[text()='Me']")
        except:
            return None

    def wait_for_home_page_to_load(self):
        wait = WebDriverWait(timeout=30,driver=self.driver)
        wait.until(expected_conditions.visibility_of(self.get_logout_button()))
        wait.until(expected_conditions.visibility_of(self.get_user_tab()))