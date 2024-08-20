from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(@href, 'shop')]")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    employment = (By.XPATH, "//input[@id='inlineRadio2']")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    successToast = (By.CLASS_NAME, 'alert-success')
    binding = (By.XPATH, "(//input[@type='text'])[3]")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def username(self):
        return self.driver.find_element(*HomePage.name)

    def emailID(self):
        return self.driver.find_element(*HomePage.email)

    def setPassword(self):
        return self.driver.find_element(*HomePage.password)

    def clickHomeCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def selectGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getEmploymentStatus(self):
        return self.driver.find_element(*HomePage.employment)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def verifySuccess(self):
        return self.driver.find_element(*HomePage.successToast)

    def getBindingText(self):
        return self.driver.find_element(*HomePage.binding)
