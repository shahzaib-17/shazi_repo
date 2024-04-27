from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self,driver):
        self.driver=driver

    shop =(By.XPATH,"//a[@href='/angularpractice/shop']")

    def shop_item(self):
        return self.driver.find_element(*Homepage.shop)

