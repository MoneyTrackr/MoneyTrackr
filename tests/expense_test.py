
from selenium import webdriver
import unittest

class ExpenseTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_display_the_income_list(self):
        self.browser.get('http://localhost:8000/expense')

        self.assertIn('Expense List', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
