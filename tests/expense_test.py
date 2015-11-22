
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from application.models import Expense
from application.models import Category
from application.models import Account

import datetime


class ExpenseTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

        category = Category(name="salary", type="income")
        category.save()

        account = Account(name="savings")
        account.save()

        expense = Expense(category=category, account=account, notes="gift", amount=1000, date=datetime.datetime.now())
        expense.save()

    def tearDown(self):
        self.browser.quit()

    def test_can_display_the_expense_list(self):

        self.browser.get('http://localhost:8081/expense')

        self.assertIn('Expense List', self.browser.title)
        self.assertIn('gift', self.browser.page_source)
        self.assertIn('savings', self.browser.page_source)
        self.assertIn('salary', self.browser.page_source)
        self.assertIn('1000', self.browser.page_source)


    def test_can_visit_add_expense_page(self):
        self.browser.get('http://localhost:8081/expense')
        add_expense_link = self.browser.find_element_by_link_text('Add Expense')
        add_expense_link.click()
        self.browser.implicitly_wait(10)

        self.assertIn('New Expense', self.browser.title)
        self.assertIn('This is my new expense page.', self.browser.page_source)
        self.fail('Finish the test!')


    def test_can_delete_an_epxense_item(self):
        expense = Expense.objects.latest('id')
        self.browser.get('http://localhost:8081/expense')
        delete_expense_link = self.browser.find_element_by_id("delete-expense-"+ str(expense.id))
        delete_expense_link.click()


        alert = self.browser.switch_to.alert
        alert.accept()
        self.browser.implicitly_wait(3)
        self.assertNotIn('gift', self.browser.page_source)
        self.assertNotIn('savings', self.browser.page_source)
        self.assertNotIn('salary', self.browser.page_source)
        self.assertNotIn('1000', self.browser.page_source)

    def test_cancels_delete_of_an_epxense_item(self):
        expense = Expense.objects.latest('id')
        self.browser.get('http://localhost:8081/expense')
        delete_expense_link = self.browser.find_element_by_id("delete-expense-"+ str(expense.id))
        delete_expense_link.click()


        alert = self.browser.switch_to.alert
        alert.dismiss()
        self.browser.implicitly_wait(20)
        self.assertIn('gift', self.browser.page_source)
        self.assertIn('savings', self.browser.page_source)
        self.assertIn('salary', self.browser.page_source)
        self.assertIn('1000', self.browser.page_source)




