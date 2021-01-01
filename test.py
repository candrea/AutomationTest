import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Andrea.Carrillo\Documents\SELENIUM\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.amazon.com/")

        driver.implicitly_wait(10)
    def testAutomation(self):
        driver = self.driver
        search_bar = driver.find_element_by_id("twotabsearchtextbox")
        button_search = driver.find_element_by_id("nav-search-submit-button")
        search_bar.send_keys("Mobile phones")
        button_search.click()
        see_more = driver.find_element_by_class_name("a-expander-prompt")
        see_more.click()
        for i in range(10):
            try:
                driver.find_element_by_css_selector("#p_89\/Motorola .a-icon").click()
                break
            except NoSuchElementException as e:
                print('Retry in 1 second')


        else:
            raise e
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


        results = driver.find_element_by_class_name("s-main-slot s-result-list s-search-results sg-row")
        for results in driver.find_elements_by_tag_name('img'):
            size = results.size
        size = size - 1
        last = "data-image-index" + size
        selected = driver.find_element_by_css_selector(last)
        selected.click()
        cart = driver.find_element_by_id("wishListMainButton-announce")
        cart.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reports", report_name="TestAutomation"))
