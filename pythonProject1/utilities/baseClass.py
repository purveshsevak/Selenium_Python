import pytest
from selenium.webdriver.support.select import Select
import inspect
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler("/Users/purvesh.sevak/PycharmProjects/PythonFramework/pythonProject1"
                                          "/utilities/logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)

        return logger

    def selectDropdownOptionByText(self, locator, text):

        dropdownStatic = Select(locator)
        dropdownStatic.select_by_visible_text(text)
