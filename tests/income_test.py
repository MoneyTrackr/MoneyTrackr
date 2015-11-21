
from selenium import webdriver
import unittest

class IncomeTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    # def tearDown(self):
    #     self.browser.quit()

    def test_can_display_the_income_list(self):
        self.browser.get('http://localhost:8000/income')

        self.assertIn('Income List', self.browser.title)
        self.fail('Finish the test!')

    def test_can_go_to_new_income_page(self):
        self.browser.get('http://localhost:8000/income')




if __name__ == '__main__':
    unittest.main(warnings='ignore')
