from selenium.webdriver.common.by import By

from pageObjects.confirmationPage import ConfirmationPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, "div[class='card h-100']")
    addButton = (By.CSS_SELECTOR, "div button")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    confirmButton = (By.CLASS_NAME, "btn-success")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def addToCart(self):
        return self.driver.find_element(*CheckoutPage.addButton)

    def checkout(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def confirmCheckout(self):
        self.driver.find_element(*CheckoutPage.confirmButton).click()
        confirmationPage = ConfirmationPage(self.driver)
        return confirmationPage
