import logging

from utils.globalVariable import defaultAddress
from utils.webDriver.Driver import Driver

__directLinkPage = "cart.html"
__nameProducts = "//*[@class='inventory_item_name']"
__removeBtn = "//button[contains(@name,'remove')]"

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()


def getHref():
    return defaultAddress + __directLinkPage


def checkProductPresentInChart(estListProduct):
    result: bool = False
    actText = []
    try:
        for i in range(Driver().getPage().locator(__nameProducts).count()):
            actText.append(Driver().getPage().locator(__nameProducts).nth(i).text_content())
        result = set(actText) == set(estListProduct)
    except BaseException:
        pass
    LOG.info("--- est: " + str(estListProduct))
    LOG.info("--- act: " + str(actText))
    return result


def clearCart():
    while Driver().getPage().locator(__removeBtn).count() > 0:
        Driver().getPage().locator(__removeBtn).nth(0).click()
