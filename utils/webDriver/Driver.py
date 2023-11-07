from playwright.async_api import Browser, Page
from playwright.sync_api import sync_playwright
from selenium import webdriver


class Driver:
    __webBrowser: Browser = None
    __webPage: Page = None

    @classmethod
    def getWebDriver(cls):
        return cls.__webBrowser

    @classmethod
    def getPage(cls):
        return cls.__webPage

    @classmethod
    def openSingelton(cls, site: str):
        if cls.__webBrowser is None:
            p = sync_playwright().start()
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(site)
            # print(page.title())
            cls.__webBrowser = browser
            cls.__webPage = page
        else:
            cls.__webPage.goto(site)


    @classmethod
    def teardown_module(cls):
        cls.__webBrowser.close()

    @classmethod
    def open(cls, site: str):
        cls.openSingelton(site)



