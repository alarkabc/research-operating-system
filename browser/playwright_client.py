class BrowserAgent:
    """
    Wrapper around Playwright browser automation.
    """

    def __init__(self):
        self.browser = None

    def start(self):
        print("Starting browser...")

    def open(self, url):
        print(f"Opening {url}")

    def close(self):
        print("Closing browser")


if __name__ == "__main__":
    browser = BrowserAgent()
    browser.start()
    browser.open("https://example.com")
    browser.close()
