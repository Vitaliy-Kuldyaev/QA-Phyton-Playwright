import testit

from pages import InventoryPage
from utils.base.BaseTest import BaseTest, do
from utils.enums.UsersCredentials import UsersCredentials
from utils.globalVariable import defaultAddress


class Test_authorization(BaseTest):

    @testit.workItemID(100)
    @testit.displayName("saucedemo_100 Тестирование авторизации")
    def test_Saucedemo_100(self, uuid):
        do.open('https://www.saucedemo.com/', user=UsersCredentials.STANDARTUSER)
        do.checkBool(InventoryPage.checkUrl(InventoryPage.getUrl()), "страница загружена")

    @testit.workItemID(101)
    @testit.displayName("saucedemo_101 Тестирование авторизации. Негативный тест")
    def test_Saucedemo_101(self, randomUser):
        do.open(defaultAddress, loginData=randomUser)
        do.checkBool(not InventoryPage.checkUrl(InventoryPage.getUrl()), "страница не загружена")

    @testit.workItemID(101)
    @testit.displayName("saucedemo_102 Тестирование авторизации. Негативный тест c ошибкой")
    def test_Saucedemo_102(self, randomUser):
        do.open(defaultAddress, loginData=randomUser)
        do.checkBool(InventoryPage.checkUrl(InventoryPage.getUrl()), "страница не загружена")
