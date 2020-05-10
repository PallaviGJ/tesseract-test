

def pytest_addoption(parser):
    parser.addoption("--browser",default="chrome")
    parser.addoption("--url",default="test")
    parser.addoption("--env",default="windows")