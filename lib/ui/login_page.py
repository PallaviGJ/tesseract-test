from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_name("username")
            #return self.driver.find_element_by_id("username") -- for url-prod
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_name("pwd")
        except:
            return None

    def get_login_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@type='submit']")
            #return self.driver.find_element_by_id("loginButton")-- for url-prod
        except:
            return None

    def get_login_error_msg(self):
        try:
            return self.driver.find_element_by_xpath("//span[text()='Username or Password is invalid. Please try again.']")
        except:
            return None

    def wait_for_login_page_to_load(self):
        wait = WebDriverWait(timeout=30,driver = self.driver)
        wait.until(expected_conditions.visibility_of(self.get_username_textbox()))
        wait.until(expected_conditions.visibility_of(self.get_password_textbox()))
        wait.until(expected_conditions.visibility_of(self.get_login_button()))
