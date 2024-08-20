from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    countryName = (By.LINK_TEXT, "India")
    checkbox = (By.CLASS_NAME, "checkbox-primary")
    submitButton = (By.XPATH, "//input[@type='submit']")
    successToast = (By.CLASS_NAME, "alert-success")

    def searchCountry(self):
        return self.driver.find_element(*ConfirmationPage.country)

    def selectCountry(self):
        return self.driver.find_element(*ConfirmationPage.countryName)

    def clickCheckbox(self):
        return self.driver.find_element(*ConfirmationPage.checkbox)

    def clickSubmit(self):
        return self.driver.find_element(*ConfirmationPage.submitButton)
