from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    def reg_email(self):
        reg_email = self.driver.find_element(By.XPATH, "//input[@id = 'reg_email']")
        return reg_email

    def reg_password(self):
        reg_password = self.driver.find_element(By.XPATH, "//input[@id = 'reg_password']")
        return reg_password

    def reg_submit(self):
        reg_submit = self.driver.find_element(By.XPATH, "//input[@value = 'Register']")
        return reg_submit

    def confirmation_text(self):
        confirmation_text = self.driver.find_element(By.XPATH, "//div[@class='woocommerce-MyAccount-content']")
        return confirmation_text

    def weak_password_warning(self):
        password_warning = self.driver.find_element(By.XPATH, "//div[@class='woocommerce-password-strength bad']")
        return password_warning

    def error_msg(self):
        error_msg = self.driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']")
        return error_msg

    def login_email(self):
        login_email = self.driver.find_element(By.ID, "username")
        return login_email

    def login_password(self):
        login_password = self.driver.find_element(By.ID, "password")
        return login_password

    def login_button(self):
        login = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        return login
