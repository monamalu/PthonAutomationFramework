from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def my_account_link(self):
        my_account = self.driver.find_element(By.XPATH,
                                              "//a[@href='https://practice.automationtesting.in/my-account/']")
        return my_account

