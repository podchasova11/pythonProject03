import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestPageOpen:

    def setup(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_github_page_open(self):
        self.driver.get("https://github.com/podchasova11/pythonProject01")
        assert self.driver.current_url == "https://github.com/podchasova11/pythonProject01"

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_orange_page_open(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_free_conference_page_open(self):
        self.driver.get("https://www.freeconferencecall.com/ru/fr")
        assert self.driver.current_url == "https://www.freeconferencecall.com/ru/fr"

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_f_conf_page_open(self):    # Тест не пройдет
        self.driver.get("https://www.freeconferencecall.com/")
        assert self.driver.current_url == "https://www.freeconferenecall.com/ru/fr"

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_band_page_open(self):    # Тест не пройдет
        self.driver.get("https://www.bandicam.com/ru/")
        assert self.driver.current_url == "https://plus"

    def teardown(self):
        self.driver.close()