import logging

from utils.Utils import click


logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()
__addToCartBtn = "//*[contains(@name,'add-to-cart')]"
__backToProducts = "//*[@name='back-to-products']"


def clickToAddToCart():
    click(__addToCartBtn, "ProductPage add to Cart")


def clickToBackToProducts():
    click(__backToProducts, "ProductPage click to backToProducts")
