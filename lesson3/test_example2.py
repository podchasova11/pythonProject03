import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginPages: # Название тестового класса
    @pytest.mark.smoke
    @pytest.mark.regression
    def setup(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_open_login_page(self):  # Тест пройдет
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", "Ошибка"  # "https://demoqa.com/login", "Ошибка"

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_open_login_page1(self):  # Тест не пройдет
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert self.driver.current_url == "https://opensrce-demo.orangehrmlive.com/web/index.php/auth/login", "Ошибка"  # "https://demoqa.com/login", "Ошибка"

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_open_books_page(self): # Тест пройдет
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://demoqa.com/books", "Ошибка"

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_open_bo_page(self):  # Тест не пройдет
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://demoqa.com/b", "Ошибка"

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_open_profile_page(self): # Тест пройдет
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка"

    def teardown(self):
        self.driver.close()