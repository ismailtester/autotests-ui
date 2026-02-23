from playwright.sync_api import expect, Page

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        return self.page.goto(url, wait_until='domcontentloaded') #networkidle позволяет дожидаться полной загрузки сетевых запросов

    def reload(self):
        return self.page.reload(wait_until='domcontentloaded') #В данном методе мы используем wait_until='domcontentloaded', чтобы дождаться, когда DOM страницы будет полностью загружен.
