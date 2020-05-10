import unittest
from lib.ui.login_page import LoginPage
from lib.utils import create_driver


class TestSample(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_sample(self):
        self.login.wait_for_login_page_to_load()
        self.login.get_username_textbox().send_keys("Invalid")
        self.login.get_password_textbox().send_keys("Invalid")
        self.login.get_login_button().click()
        actual_error_msg = self.login.get_login_error_msg().text
        expected_error_msg = "Username or Password is invalid. Please try again."
        assert actual_error_msg == expected_error_msg,"Invalid credentials"

