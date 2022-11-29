import time
import pytest
from pageObjects.AccountPage import AccountPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestRegistration(BaseClass):
    def test_registration(self):
        homepage = HomePage(self.driver)
        accountpage = AccountPage(self.driver)
        homepage.my_account_link().click()
        time.sleep(3)
        accountpage.reg_email().send_keys(self.random_email()+"@gmail.com")
        accountpage.reg_password().send_keys(self.random_password())
        accountpage.reg_submit().click()
        actual_text = accountpage.confirmation_text().text
        if "Hello" + self.random_email()+"@gmail.com" in actual_text:
            print("User registered successfully.")

    def test_registration_weak_password(self, get_data):
        homepage = HomePage(self.driver)
        accountpage = AccountPage(self.driver)
        homepage.my_account_link().click()
        time.sleep(3)
        accountpage.reg_email().send_keys(get_data["email"])
        accountpage.reg_password().send_keys(get_data["password"])
        accountpage.reg_submit().get_property('disabled')
        actual_text = accountpage.weak_password_warning().text
        expected_text = "Weak - Please enter a stronger password."
        assert actual_text == expected_text, "Weak password test case failed."

    def test_registartion_empty_email_address(self):
        homepage = HomePage(self.driver)
        accountpage = AccountPage(self.driver)
        homepage.my_account_link().click()
        time.sleep(3)
        accountpage.reg_email().send_keys(" ")
        accountpage.reg_password().send_keys(self.random_password())
        accountpage.reg_submit().click()
        time.sleep(2)
        actual_text = accountpage.error_msg().text
        expected_text = "Error: Please provide a valid email address."
        assert actual_text == expected_text, "Error message is not shown up as expected."

    def test_registartion_empty_password(self):
        homepage = HomePage(self.driver)
        accountpage = AccountPage(self.driver)
        homepage.my_account_link().click()
        time.sleep(3)
        accountpage.reg_email().send_keys(self.random_email()+"@gmail.com")
        accountpage.reg_password().send_keys("")
        accountpage.reg_submit().click()
        time.sleep(2)
        actual_text = accountpage.error_msg().text
        expected_text = "Error: Please enter an account password."
        assert actual_text == expected_text, "Error message is not shown up as expected."

    @pytest.fixture(params=[{"email": "Test1234", "password": "test4545"}])
    def get_data(self, request):
        return request.param

