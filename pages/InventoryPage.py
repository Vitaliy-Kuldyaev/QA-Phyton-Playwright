import logging

from pages import ProductPage, CartPage
from utils.Utils import click
from utils.webDriver.Driver import Driver

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()
__estHeaderPageName = "Swag Labs"
__baseUrl = "https://www.saucedemo.com/inventory.html"
__numberProductsInCart = "//*[@class='shopping_cart_badge']"
__linkToCartPage = "//*[@class='shopping_cart_link']"


def getNameHeader():
    return __estHeaderPageName


def getUrl():
    return __baseUrl


def checkUrl(estUrl: str):
    try:
        LOG.info("  act:" + Driver().getPage().url)
        LOG.info("  est:" + estUrl)
        if Driver().getPage().url == estUrl:
            return True
        else:
            return False
    except BaseException:
        return False


def addProductsToCart(listProducts: list):
    for cartElement in listProducts:
        # click(f"text[{cartElement}])", "нажатие на продукт: " + cartElement)
        click(f"text={cartElement}", "нажатие на продукт: " + cartElement)

        ProductPage.clickToAddToCart()
        ProductPage.clickToBackToProducts()


def checkProductNumberInCart(estListProduct):
    if Driver.getPage().text_content(__numberProductsInCart) == str(len(estListProduct)):
        return True


def checkCartContainsNewProduct(estListProduct):
    click(__linkToCartPage, "открываем корзину")
    return CartPage.checkProductPresentInChart(estListProduct)
