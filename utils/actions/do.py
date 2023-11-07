import allure

from pages import LoginPage
from utils.Utils import *
from utils.enums.UsersCredentials import UsersCredentials
from utils.webDriver.Driver import Driver
from utils.steps import StepBase

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()


class doClass(object):
    @allure.step("Открыть сайт: {site}, логин: {loginData}")
    def open(self, site: str, loginData: {} = None, user: UsersCredentials = None):
        Driver.open(site)
        self.headerLog()
        LOG.info("------- Открытие страницы: " + site)
        if loginData is not None:
            LOG.info("------- User: " + loginData.get("name"))
            LoginPage.fillUsername(loginData.get("name"))
            LoginPage.fillPass(loginData.get("password"))
            LoginPage.clickOkBtn()
        if user is not None:
            LOG.info("------- User: " + user.login)
            LoginPage.fillUsername(user.login)
            LoginPage.fillPass(user.password)
            LoginPage.clickOkBtn()
        self.footerLog()


    def headerLog(self):
        LOG.info("")
        LOG.info("")
        LOG.info("____________________________________")
        LOG.info("-------------Start Step-------------")

    def footerLog(self):
        LOG.info("-------------End Step---------------")
        LOG.info("____________________________________")

    @allure.step("Проверка: {message}")
    def checkBool(self, action: bool, message: str):
        self.headerLog()
        LOG.info("Проверка: " + message)
        assert action == True
        self.footerLog()
        return self

    @allure.step("Проверка: {message}")
    def checkNotBool(self, action: bool, message: str):
        self.headerLog()
        LOG.info("Проверка: " + message)
        assert action == False
        self.footerLog()
        return self

    @allure.step("Выполнить действия: {message}")
    def step(self, step: StepBase, message: str):
        LOG.info("")
        LOG.info("-------------------------------------")
        LOG.info("Выполнено действие: " + message)
        LOG.info("-------------------------------------")
        return self
