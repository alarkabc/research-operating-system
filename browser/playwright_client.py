from playwright.sync_api import sync_playwright


class BrowserAgent:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.page = self.browser.new_page()

    def open(self, url):

        self.page.goto(url)

        print("Loaded:", self.page.title())

    def html(self):

        return self.page.content()

    def screenshot(self, filename="page.png"):

        self.page.screenshot(path=filename)

    def close(self):

        self.browser.close()

        self.playwright.stop()


if __name__ == "__main__":

    browser = BrowserAgent()

    browser.start()

    browser.open("https://arxiv.org")

    browser.screenshot()

    browser.close()
