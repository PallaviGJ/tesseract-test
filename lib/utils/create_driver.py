from argparse import ArgumentParser
from selenium.webdriver import Chrome, Firefox, Ie


def get_driver_instance():
    parser = ArgumentParser()
    parser.add_argument("--browser", default="firefox")
    parser.add_argument("--url", default="test")
    parser.add_argument("--env", default="windows")

    options, arg = parser.parse_known_args()

    browser_type = options.browser.lower()
    url_info = options.url.lower()
    env_info = options.env.lower()

    if browser_type == "chrome":
        driver = Chrome()
    elif browser_type == "firefox":
        driver = Firefox("./browser-servers/geckodriver.exe")
    elif browser_type == "ie":
        driver = Ie("./browser-servers/iedriver.exe")
    else:
        print("-- !!!!!!! not found----!!!!")

    driver.maximize_window()
    driver.implicitly_wait(30)

    if url_info == "prod":
        driver.get("https://demo.actitime.com/login.do")
    elif url_info == "staging":
        driver.get("https://192.168.1.101/login.html")
    else:
        driver.get("https://actitime.jmr.co.za/actitime/login.do")

    return driver

