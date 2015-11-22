
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  #1

    def setUp(self):  #2
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  #3
        self.browser.quit()

    def test_can_display_the_income_list(self):  #4
        self.browser.get('http://localhost:8000/income')
        self.assertIn('Income List', self.browser.title)  #5
        # self.fail('Finish the test!')  #6


if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8
