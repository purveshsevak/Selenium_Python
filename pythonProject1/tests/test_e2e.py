import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.homePage import HomePage
from utilities.baseClass import BaseClass


class TestOne(BaseClass):

    def test_e2eFlow(self):

        # e2e code for phone order placement
        # new QA commit
        log = self.getLogger()
        homePage = HomePage(self.driver)

        checkoutPage = homePage.shopItems()
        items = checkoutPage.getCardTitles()

        for item in items:
            itemName = item.text
            if itemName == "Blackberry":
                checkoutPage.addToCart().click()

        checkoutPage.checkout().click()
        confirmationPage = checkoutPage.confirmCheckout()
        confirmationPage.searchCountry().send_keys("ind")
        log.info("Country name is selected as India")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(confirmationPage.countryName))

        confirmationPage.selectCountry().click()
        confirmationPage.clickCheckbox().click()
        confirmationPage.clickSubmit().click()

        successMessage = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text message received from application is " + successMessage)
        assert "Success! Thank you!" in successMessage
