from playwright.sync_api import sync_playwright, Request, Response


def log_request(request: Request) -> None:
    print(f'Request: {request.url}')


def log_response(response: Response) -> None:
    print(f'Response: {response.url}, {response.status}, {response.status_text}')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.on('request', log_request)
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')


    # page.remove_listener('request', log_request) #Тут мы удаляем обработчик для примера
    page.on('response',log_response)

    page.wait_for_timeout(5000)