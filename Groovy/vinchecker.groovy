import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webui.driver.DriverFactory as DriverFactory
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import internal.GlobalVariable as GlobalVariable
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.thoughtworks.selenium.Selenium
import org.openqa.selenium.firefox.FirefoxDriver
import org.openqa.selenium.WebDriver
import com.thoughtworks.selenium.webdriven.WebDriverBackedSelenium
import static org.junit.Assert.*
import java.util.regex.Pattern
import static org.apache.commons.lang3.StringUtils.join

WebUI.openBrowser('THIS_IS_URL')
def driver = DriverFactory.getWebDriver()
String baseUrl = "THIS_IS_URL"
selenium = new WebDriverBackedSelenium(driver, baseUrl)
selenium.open("THIS_IS_URL")
selenium.click("name=VIN")
selenium.click("name=VIN")
selenium.type("name=VIN", "THIS_IS_VIN")
selenium.click("name=submit")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
String model1 = selenium.getText("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)=concat('TEXT_VALUE_2_WHERE_CONCAT', \"'\", 'TEXT_VALUE_2_WHERE_CONCAT')])[1]/following::td[1]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::tr[1]")
String dvigatel1 = selenium.getText("xpath=(.//*[normalize-space(text()) and normalize-space(.)=concat('TEXT_VALUE_2_WHERE_CONCAT', \"'\", 'TEXT_VALUE_2_WHERE_CONCAT')])[1]/following::td[1]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
String korobka1 = selenium.getText("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[2]")
selenium.doubleClick("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[2]")
String privod1 = selenium.getText("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[2]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
selenium.doubleClick("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
String GOD1 = selenium.getText("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
selenium.click("name=VIN")
selenium.doubleClick("name=VIN")
selenium.type("name=VIN", "TEXT_VALUE")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::span[1]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
String model2 = selenium.getText("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[2]/following::footer[1]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
String dvigatel2 = selenium.getText("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::div[2]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
String korobka2 = selenium.getText("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[2]")
String privod2 = selenium.getText("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[2]")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
String GOD2 = selenium.getText("xpath=(.//*[normalize-space(text()) and normalize-space(.)='TEXT_VALUE'])[1]/following::td[1]")
