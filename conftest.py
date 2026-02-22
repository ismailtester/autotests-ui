import pytest  # Импортируем pytest
from playwright.sync_api import  Page, Playwright  # Имопртируем класс страницы, будем использовать его для аннотации типов



@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)

    # Передаем страницу для использования в тесте
    yield browser.new_page()

    # Закрываем браузер после выполнения тестов
    browser.close()
