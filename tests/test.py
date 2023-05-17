import unittest
import os
import base64
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    appPackage='org.thoughtcrime.securesms',
    appActivity='.RoutingActivity',
    autoGrantPermissions=True,
    waitForIdleTimeout=500,
    skipDeviceInitialization=True
)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
            
    def testMain(self) -> None:    
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Continue"]')
        el.click()
        
        
if __name__ == '__main__':
    unittest.main()
