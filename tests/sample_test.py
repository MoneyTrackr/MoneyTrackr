
from selenium import webdriver
import unittest
from application.models import Category

class NewVisitorTest(unittest.TestCase):  #1

    def setUp(self):  #2
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  #3
        self.browser.quit()

    def test_can_display_the_income_list(self):  #4
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000/income')

        # She notices the page title and header mention to-do lists
        self.assertIn('Income List', self.browser.title)  #5
        self.fail('Finish the test!')  #6

        # She is invited to enter a to-do item straight away
        # [...rest of comments as before]

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8
