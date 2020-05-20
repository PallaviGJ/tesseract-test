import time
import unittest
import json
from selenium.webdriver import ActionChains
from lib.ui.home_page import HomePage
from lib.ui.login_page import LoginPage
from lib.ui.userlist_page import UserListPage
from lib.utils import create_driver


class TestLoginS13245(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.userlist_page = UserListPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_success_tc14578(self):
        data = json.load(open("./test/regression/login/S13245.json"))
        # 1. Go to Login page
        self.login_page.wait_for_login_page_to_load()
        # 2. Enter valid UN and PWD
        self.login_page.get_username_textbox().send_keys(data['TC14578']['username'])
        self.login_page.get_password_textbox().send_keys(data['TC14578']['password'])
        # 3. Click on Login Button
        self.login_page.get_login_button().click()
        # 4. Click on user tab
        self.home_page.get_user_tab().click()
        # 5. Click on New user
        self.userlist_page.get_new_user_tab().click()
        time.sleep(3)
        # 6. Add new user to list
        self.userlist_page.get_new_user_first_name_textbox().send_keys(data["TC13246"]["first_name"])
        self.userlist_page.get_new_user_last_name_textbox().send_keys(data["TC13246"]["last_name"])
        self.userlist_page.get_new_user_email_textbox().send_keys(data["TC13246"]["mail_id"])
        department = self.userlist_page.get_departname()
        act = ActionChains(self.driver)
        act.move_to_element(department).click().send_keys(data["TC13246"]["depart_name"]).click().perform()
        time.sleep(5)
        hire_date = self.userlist_page.get_hire_date()
        act.move_to_element(hire_date).click().send_keys(data["TC13246"]["hire1_date"]).perform()
        time.sleep(5)
        # 7. Click on save and send button
        self.userlist_page.get_save_send_button().click()
        time.sleep(5)
        # 8 . Verify success message
        actual_success_message = self.userlist_page.get_success_msg().text
        print(actual_success_message)
        expected_success_message = data["TC13246"]["success_message"]
        print(expected_success_message)
        assert actual_success_message == expected_success_message,"New user is not added successfully"