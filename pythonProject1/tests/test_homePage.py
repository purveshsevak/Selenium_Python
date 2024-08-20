import pytest

from pageObjects.homePage import HomePage
from testData.homePageData import HomePageData
from utilities.baseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getUserData):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.username().send_keys(getUserData["userName"])
        log.info("User name is " + getUserData["userName"])
        homePage.emailID().send_keys(getUserData["email"])
        homePage.setPassword().send_keys(getUserData["password"])
        homePage.clickHomeCheckbox().click()

        self.selectDropdownOptionByText(homePage.selectGender(), getUserData["gender"])

        homePage.getEmploymentStatus().click()
        homePage.submitForm().click()

        successMessage = homePage.verifySuccess().text
        assert "Success" in successMessage

        homePage.getBindingText().send_keys("Submitted Successfully!")
        homePage.getBindingText().clear()

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getExcelData("TestCase1"))
    def getUserData(self, request):
        return request.param
