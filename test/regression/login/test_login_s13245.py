import time
import unittest
import json
from selenium.webdriver import ActionChains
from lib.ui.home_page import HomePage
from lib.ui.login_page import LoginPage
from lib.utils import create_driver


class TestLoginS13245(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

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
        # 4. Select time track user name
        self.home_page.wait_for_home_page_to_load()
        user_name = self.home_page.get_time_drop_down()
        act = ActionChains(self.driver)
        time.sleep(5)
        act.move_to_element(user_name).click().send_keys(data['TC14578']['drop_down_name']).click().perform()





        # 4. Verify Home Page
        #self.home_page.wait_for_home_page_to_load()
        #actual_home_page_title = self.driver.title
        #print(actual_home_page_title)
        #expected_home_page_title = data['TC14578']['home_page_title']
        #print(expected_home_page_title)
        #assert actual_home_page_title == expected_home_page_title ,"Title of webpage is not matching"
        # 5. click on Logout button
        #self.home_page.get_logout_button().click()
        # 6. Verify login page
        #self.login_page.wait_for_login_page_to_load()
        #actual_login_page_title = self.driver.title
        #print(actual_login_page_title)
        #expected_login_page_title = data['TC14578']['login_page_title']
        #print(expected_login_page_title)
        #assert actual_login_page_title == expected_login_page_title,"Title of login page is not matching"

