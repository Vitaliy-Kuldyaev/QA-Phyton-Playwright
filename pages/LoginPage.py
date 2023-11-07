import logging

from utils.webDriver.Driver import Driver

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()

__userNameLocator = 'input[name="user-name"]'
__userPasswordLocator = 'input[name="password"]'
__loginBtnLocator = 'input[name="login-button"]'


def fillUsername(username: str):
    Driver().getPage().fill(__userNameLocator, username)


def fillPass(password: str):
    Driver().getPage().fill(__userPasswordLocator, password)


def clickOkBtn():
    Driver().getPage().click(__loginBtnLocator)
