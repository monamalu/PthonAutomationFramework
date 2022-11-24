import time
import pytest
from pageObjects.AccountPage import AccountPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestLogin(BaseClass):
    def test_login(self):
        homepage = HomePage(self.driver)
        accountpage = AccountPage(self.driver)
        homepage.my_account_link().click()
        time.sleep(3)
        accountpage.login_email().send_keys("monalitest12@test.com")
        accountpage.login_password().send_keys("Testdemo@123")
        accountpage.login_button().click()
        actual_text = accountpage.confirmation_text().text
        if "Hello monalitest123" in actual_text:
            print("User logged in successfully.")

    def test_new_user_login_with_email_address(self):
        homepage = HomePage(self.driver)
        accountpage = AccountPage(self.driver)
        homepage.my_account_link().click()
        time.sleep(3)
        accountpage.login_email().send_keys(self.random_email() + "@gmail.com")
        accountpage.login_password().send_keys(self.random_password())
        accountpage.login_button().click()
        time.sleep(2)
        error_msg = accountpage.error_msg().text
        actual_msg = "Error: A user could not be found with this email address."
        assert error_msg == actual_msg, "New User login error message not displayed as expected."

    def test_new_user_login_with_username(self):
        homepage = HomePage(self.driver)
        accountpage = AccountPage(self.driver)
        homepage.my_account_link().click()
        time.sleep(3)
#        if WebDriverWait(self.driver, 5).until(EC.alert_is_present()):
#            alert = self.driver.switch_to.alert
#            alert.dismiss()
        accountpage.login_email().send_keys(self.random_email())
        accountpage.login_password().send_keys(self.random_password())
        accountpage.login_button().click()
        time.sleep(2)
        error_msg = accountpage.error_msg().text
        if "Error: the username is not registered on this site. If you are unsure of your " \
           "username, try your email address instead." in error_msg:
            print("New username login test case is passed.")