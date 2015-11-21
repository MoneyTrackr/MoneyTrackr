
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

    def test_can_visit_add_expense_page(self):
        self.browser.get('http://localhost:8000/expense')

        add_expense_link = self.browser.find_element_by_link_text('Add Expense')
        add_expense_link.click()
        self.browser.implicitly_wait(10)

        self.assertIn('New Expense', self.browser.title)
        self.assertIn('This is my new expense page.', self.browser.page_source)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
