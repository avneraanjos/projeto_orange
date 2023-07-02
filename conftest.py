from selenium import webdriver
from selenium.webdriver.edge.options import Options

import pytest
from Pages.login import LoginPage
from Pages.pmi import PMIPage


@pytest.fixture()
def open_login_page():
    login_page = LoginPage()
    yield login_page

@pytest.fixture()
def open_pmi_page():
    pmi = PMIPage()
    yield pmi