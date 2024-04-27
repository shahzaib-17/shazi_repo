from selenium.webdriver.common.by import By
from seleniume2e.Page_Objects.Homepage import Homepage


class checkoutpage(Homepage):
    def __init__(self, driver):
        super().__init__(driver)

    cart =(By.XPATH,"//button[@class='btn btn-info']")
    name=(By.CSS_SELECTOR,".card-title")
    check=(By.CLASS_NAME, 'btn-primary')

    def item_selection(self):
        return self.driver.find_elements(*checkoutpage.cart)

    def card_header(self):
        return self.driver.find_elements(*checkoutpage.name)

    def checkout_button(self):
        return self.driver.find_element(*checkoutpage.check)
