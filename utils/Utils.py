import logging
import time
from typing import Type

import allure
import playwright.sync_api
from playwright.sync_api import Browser

from utils.webDriver.Driver import Driver

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()


def headerPrecondicion():
    LOG.info("")
    LOG.info("")
    LOG.info("")
    LOG.info("--- подготовка к проверке")


def getWebBrowser() -> Type[Browser]:
    return playwright.sync_api.Browser


def generateUUID():
    return str(int(time.time()))


def headerLog():
    LOG.info("")
    LOG.info("")
    LOG.info("____________________________________")
    LOG.info("-------------Start Step-------------")


def footerLog():
    LOG.info("-------------End Step---------------")
    LOG.info("____________________________________")


@allure.step("Нажатие на элемент: {message}")
def click(el: str, message: str):
    headerLog()
    LOG.info("------- Нажатие: " + message)
    Driver().getPage().click(el)
    # el.with_(timeout=10).should(be.visible).click()
    footerLog()
