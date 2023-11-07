import logging
import random
from pathlib import Path

import allure
import pytest
import slugify
from allure_commons.types import AttachmentType
from mimesis import Person, Locale
from selenium import webdriver

from pages import CartPage
from utils.Utils import generateUUID
from utils.base.BaseTest import do
from utils.webDriver.Driver import Driver

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()
prev_test_screenshot = None
prev_test_page_source = None

@pytest.fixture(autouse=True)
def uuid(request):
    return generateUUID()


@pytest.fixture(autouse=True)
def randomUser():
    person = Person(Locale.RU)
    name = person.username(mask='l_d')
    password = person.password(length=16, hashed=False)
    do.headerLog()
    LOG.info("------- Генерация пользователя")
    LOG.info("------- Login: " + name)
    LOG.info("------- Password: " + password)
    do.footerLog()
    return {"name": name, "password": password}


@pytest.fixture()
def newCartProduct(request):
    marker = request.node.get_closest_marker('newCartProducts')
    data = None if marker is None else list(marker.args[0][0])
    numberNewCartElements = None if marker is None else marker.args[0][1]
    if len(data) < numberNewCartElements:
        do.headerLog()
        LOG.info("------- Ошибка: количество запрашиваемых товаров не больше количества тестовых")
        do.footerLog()
        return None
    randomPosition = random.sample(range(len(data)), numberNewCartElements)
    resultListProducts = []
    for i in randomPosition:
        resultListProducts.append(data[i])
    return resultListProducts


@pytest.fixture()
def clearCart():
    yield
    do.open(CartPage.getHref())
    do.step(CartPage.clearCart(), "очистка корзины")


def pytest_exception_interact():
    with allure.step('Screenshot'):
        browserDriver = Driver().getWebDriver()
        if browserDriver is not None:
            allure.attach(Driver().getPage().screenshot(), name="Screenshot", attachment_type=AttachmentType.PNG)
