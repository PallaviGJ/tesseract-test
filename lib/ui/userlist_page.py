from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class UserListPage:

    def __init__(self,driver):
        self.driver = driver

    def get_new_user_tab(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='New User']")
        except:
            return None

    def get_new_user_first_name_textbox(self):
        try:
            return self.driver.find_element_by_id("createUserPanel_firstNameField")
        except:
            return None

    def get_new_user_last_name_textbox(self):
        try:
            return self.driver.find_element_by_id("createUserPanel_lastNameField")
        except:
            return None

    def get_new_user_email_textbox(self):
        try:
            return self.driver.find_element_by_id("createUserPanel_emailField")
        except:
            return None

    def get_save_send_button(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='Save & Send Invitation']")
        except:
            return None

    def get_success_msg(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='Account for Rishik Vihaan has been created.']")
        except:
            return None

    def get_departname(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='-- department not assigned --']")
        except:
            return None

    def get_hire_date(self):
        try:
            return self.driver.find_element_by_id("ext-gen610")
        except:
            return None

    def wait_new_user_page_to_load(self):
        wait = WebDriverWait(timeout=30,driver=self.driver)
        wait.until(expected_conditions.visibility_of(self.get_new_user_tab()))
        #wait.until(expected_conditions.visibility_of(self.get_new_user_first_name_textbox()))
        # wait.until(expected_conditions.visibility_of(self.get_new_user_last_name_textbox()))
        #wait.until(expected_conditions.visibility_of(self.get_new_user_email_textbox()))
        #wait.until(expected_conditions.visibility_of(self.get_save_send_button()))
