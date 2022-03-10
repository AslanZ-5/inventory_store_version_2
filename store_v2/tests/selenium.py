import pytest 
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture(scope='module')
def edge_browser_instance(request):
    """
    Provide a selenium webdriver instance     
    """
    options = Options()
    options.headless = False
    browser = webdriver.Edge(options=options)
    yield browser
    browser.close()
