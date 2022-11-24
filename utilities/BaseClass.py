import random
import string

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    def wait_for_element_to_display(self, locator):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(By.XPATH, locator))

    def random_email(self):
        random_email = ''
        for x in range(8):
            random_email += ''.join(random.choice(string.ascii_lowercase))
        return random_email

    def random_password(self):
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        num = string.digits
        symbols = string.punctuation
        all = upper+lower+num+symbols
        temp = random.sample(all, 12)
        password = "".join(temp)
        return password

    def alert(self):
       alert = self.driver.find_element(By.XPATH, "//div[@id = 'card']")
       return alert

    def dismiss_alert(self):
        try:
            self.driver(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.dismiss()
            print("alert Exists in page")
        except TimeoutException:
            print("alert does not Exist in page")
