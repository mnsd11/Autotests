from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "THIS_IS_URL"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("THIS_IS_URL")
        driver.find_element_by_name("VIN").click()
        driver.find_element_by_name("VIN").clear()
        driver.find_element_by_name("VIN").send_keys("THIS_IS_VIN")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").click()
        model1 = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").text
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=concat('TEXT_VALUE_2_WHERE_CONCAT', \"TEXT_VALUE_2_WHERE_CONCAT\", 'TEXT_VALUE_2_WHERE_CONCAT')])[1]/following::td[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::tr[1]").click()
        dvigatel1 = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=concat('TEXT_VALUE_2_WHERE_CONCAT', \"'\", 'TEXT_VALUE_2_WHERE_CONCAT')])[1]/following::td[1]").text
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").click()
        korobka1 = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").text
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[2]").click()
        privod1 = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[2]").text
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").click()
        GOD1 = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").text
        driver.find_element_by_name("VIN").click()
        driver.find_element_by_name("VIN").clear()
        driver.find_element_by_name("VIN").send_keys("TEXT_VALUE")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").click()
        model2 = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").text
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[2]/following::footer[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").click()
        dvigatel2 = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").text
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").click()
        korobka2 = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").text
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[2]").click()
        privod2 = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[2]").text
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").click()
        GOD2 = driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]").text
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()