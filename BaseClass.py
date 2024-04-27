import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("driver_fix")
class BaseClass:

    def wait(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(locator))
