
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from application.models import Income
from application.models import Category
from application.models import Account

import datetime


class IncomeTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

        category = Category(name="salary", type="income")
        category.save()

        account = Account(name="savings")
        account.save()

        income = Income(category=category, account=account, notes="October 2015 salary", amount=100000, date=datetime.datetime.now())
        income.save()

    def tearDown(self):
        self.browser.quit()

    def test_can_display_the_income_list(self):

        self.browser.get('http://localhost:8081/income')

        self.assertIn('Income List', self.browser.title)
        self.assertIn('October 2015 salary', self.browser.page_source)
        self.assertIn('savings', self.browser.page_source)
        self.assertIn('salary', self.browser.page_source)
        self.assertIn('100000', self.browser.page_source)


    def test_can_visit_add_income_page(self):
        self.browser.get('http://localhost:8081/income')
        add_expense_link = self.browser.find_element_by_link_text('Add Income')
        add_expense_link.click()
        self.browser.implicitly_wait(10)

        self.assertIn('New Income', self.browser.title)
        self.assertIn('This is my new income page.', self.browser.page_source)
        self.fail('Finish the test!')


    def test_can_delete_an_income_item(self):
        income = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        delete_income_link = self.browser.find_element_by_id("delete-income-"+ str(income.id))
        delete_income_link.click()


        alert = self.browser.switch_to.alert
        alert.accept()
        self.browser.implicitly_wait(3)


        self.assertNotIn('October 2015 salary', self.browser.page_source)
        self.assertNotIn('savings', self.browser.page_source)
        self.assertNotIn('salary', self.browser.page_source)
        self.assertNotIn('1000000', self.browser.page_source)

    def test_cancels_delete_of_an_income_item(self):
        income = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        delete_income_link = self.browser.find_element_by_id("delete-income-"+ str(income.id))
        delete_income_link.click()


        alert = self.browser.switch_to.alert
        alert.dismiss()
        self.assertIn('Income List', self.browser.title)
        self.assertIn('October 2015 salary', self.browser.page_source)
        self.assertIn('savings', self.browser.page_source)
        self.assertIn('salary', self.browser.page_source)
        self.assertIn('100000', self.browser.page_source)





