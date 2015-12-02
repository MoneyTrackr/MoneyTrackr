
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

#1 List
    def test_can_display_the_income_list(self):

        self.browser.get('http://localhost:8081/income')

        self.assertIn('Income List', self.browser.title)
        self.assertIn('October 2015 salary', self.browser.page_source)
        self.assertIn('savings', self.browser.page_source)
        self.assertIn('salary', self.browser.page_source)
        self.assertIn('100000', self.browser.page_source)

#2 Add
    def test_can_visit_add_income_page(self):
        self.browser.get('http://localhost:8081/income')
        add_income_link = self.browser.find_element_by_link_text('Add Income')
        add_income_link.click()
        #self.browser.implicitly_wait(10)

#3 Add
    def test_can_submit_add_income(self):
        self.browser.get('http://localhost:8081/income/new')

        self.assertIn('Date:', self.browser.page_source)
        self.browser.find_element_by_id('id_date')
        self.assertIn('Category:', self.browser.page_source)
        self.browser.find_element_by_id('id_category')
        self.assertIn('Amount:', self.browser.page_source)
        self.browser.find_element_by_id('id_amount')
        self.assertIn('Account:', self.browser.page_source)
        self.browser.find_element_by_id('id_account')
        self.assertIn('Notes:', self.browser.page_source)
        self.browser.find_element_by_id('id_notes')

        submit_income_button = self.browser.find_element_by_id('id_submit_income')
        submit_income_button.click()
        self.browser.implicitly_wait(20)

#4 Add
    def test_can_cancel_add_income(self):
        self.browser.get('http://localhost:8081/income/new')
        cancel_income_button = self.browser.find_element_by_id('id_cancel_income')
        cancel_income_button.click()
        #self.assertIn('Income List', self.browser.title)

    def test_detects_date_is_invalid_on_add(self):
        self.browser.get('http://localhost:8081/income/new')

        input_category =  self.browser.find_element_by_id('id_category')
        input_category.send_keys('others')

        input_amount =  self.browser.find_element_by_id('id_amount')
        input_amount.send_keys('100')

        input_account =  self.browser.find_element_by_id('id_account')
        input_account.send_keys('savings')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('family treat')

        add_expense_button = self.browser.find_element_by_id('id_submit_income')
        add_expense_button.click()

        self.browser.implicitly_wait(10)

#5 Add
    def test_detects_category_is_invalid_on_add(self):
        self.browser.get('http://localhost:8081/income/new')
        input_date =  self.browser.find_element_by_id('id_date')
        input_date.send_keys('12/25/2015')

        input_amount =  self.browser.find_element_by_id('id_amount')
        input_amount.send_keys('100')

        input_account =  self.browser.find_element_by_id('id_account')
        input_account.send_keys('savings')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('family treat')

        add_expense_button = self.browser.find_element_by_id('id_submit_income')
        add_expense_button.click()

        self.browser.implicitly_wait(10)

#6 Add
    def test_detects_amount_is_invalid_on_add(self):
        self.browser.get('http://localhost:8081/income/new')
        input_date =  self.browser.find_element_by_id('id_date')
        input_date.send_keys('12/25/2015')

        input_category =  self.browser.find_element_by_id('id_category')
        input_category.send_keys('others')

        input_account =  self.browser.find_element_by_id('id_account')
        input_account.send_keys('savings')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('family treat')

        add_expense_button = self.browser.find_element_by_id('id_submit_income')
        add_expense_button.click()

        self.browser.implicitly_wait(10)

#7 Add
    def test_detects_account_is_invalid_on_add(self):
        self.browser.get('http://localhost:8081/income/new')
        input_date =  self.browser.find_element_by_id('id_date')
        input_date.send_keys('12/25/2015')

        input_category =  self.browser.find_element_by_id('id_category')
        input_category.send_keys('others')

        input_amount =  self.browser.find_element_by_id('id_amount')
        input_amount.send_keys('100')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('family treat')

        add_expense_button = self.browser.find_element_by_id('id_income_expense')
        add_expense_button.click()

        self.browser.implicitly_wait(10)

#8 Delete
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

#9 Delete
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

#10 Edit
    def test_can_submit_edit_income(self):
        income = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        edit_income_link = self.browser.find_element_by_id("edit-income-"+ str(income.id))
        edit_income_link.click()

        self.assertIn('Date:', self.browser.page_source)
        self.browser.find_element_by_id('id_date')
        self.assertIn('Category:', self.browser.page_source)
        self.browser.find_element_by_id('id_category')
        self.assertIn('Amount:', self.browser.page_source)
        self.browser.find_element_by_id('id_amount')
        self.assertIn('Account:', self.browser.page_source)
        self.browser.find_element_by_id('id_account')
        self.assertIn('Notes:', self.browser.page_source)
        self.browser.find_element_by_id('id_notes')

        submit_income_button = self.browser.find_element_by_id('id_submit_income')
        submit_income_button.click()
        self.browser.implicitly_wait(20)

#11 Edit
    def test_can_cancel_edit_income(self):
        income = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        cancel_income_link = self.browser.find_element_by_id("edit-income-"+ str(income.id))
        cancel_income_link.click()

        cancel_income_button = self.browser.find_element_by_id('id_cancel_income')
        cancel_income_button.click()
        #self.assertIn('Income List', self.browser.title)

#12 Edit
    def test_detects_date_is_invalid_on_edit(self):
        income = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        cancel_income_link = self.browser.find_element_by_id("edit-income-"+ str(income.id))
        cancel_income_link.click()

        input_category =  self.browser.find_element_by_id('id_category')
        input_category.send_keys('salary')

        input_amount =  self.browser.find_element_by_id('id_amount')
        input_amount.send_keys('10000')

        input_account =  self.browser.find_element_by_id('id_account')
        input_account.send_keys('savings')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('from salary')

        add_expense_button = self.browser.find_element_by_id('id_submit_income')
        add_expense_button.click()

        self.browser.implicitly_wait(10)
        self.assertIn('This field is required', self.browser.page_source)

#13 Edit

    def test_detects_date_is_invalid_on_edit(self):
        income = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        edit_income_link = self.browser.find_element_by_id("edit-income-"+ str(income.id))
        edit_income_link.click()

        input_date =  self.browser.find_element_by_id('id_date')
        input_date.send_keys('12/25/2015')

        input_category =  self.browser.find_element_by_id('id_category')
        input_category.send_keys('salary')

        input_amount =  self.browser.find_element_by_id('id_amount')
        input_amount.send_keys('10000')

        input_account =  self.browser.find_element_by_id('id_account')
        input_account.send_keys('savings')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('from salary')

        add_expense_button = self.browser.find_element_by_id('id_submit_income')
        add_expense_button.click()

        self.browser.implicitly_wait(10)

#14 Edit

    def test_detects_category_is_invalid_on_edit(self):
        income = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        edit_income_link = self.browser.find_element_by_id("edit-income-"+ str(income.id))
        edit_income_link.click()

        input_date =  self.browser.find_element_by_id('id_date')
        input_date.send_keys('12/25/2015')

        input_amount =  self.browser.find_element_by_id('id_amount')
        input_amount.send_keys('100')

        input_account =  self.browser.find_element_by_id('id_account')
        input_account.send_keys('savings')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('family treat')

        add_expense_button = self.browser.find_element_by_id('id_submit_income')
        add_expense_button.click()

        self.browser.implicitly_wait(10)

#15 Edit

    def test_detects_amount_is_invalid_on_edit(self):
        income = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        edit_income_link = self.browser.find_element_by_id("edit-income-"+ str(income.id))
        edit_income_link.click()

        input_date =  self.browser.find_element_by_id('id_date')
        input_date.send_keys('12/25/2015')

        input_category =  self.browser.find_element_by_id('id_category')
        input_category.send_keys('others')

        input_account =  self.browser.find_element_by_id('id_account')
        input_account.send_keys('savings')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('family treat')

        add_expense_button = self.browser.find_element_by_id('id_submit_income')
        add_expense_button.click()

        self.browser.implicitly_wait(10)

#16 Edit

    def test_detects_account_is_invalid_on_add(self):
        income = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        edit_income_link = self.browser.find_element_by_id("edit-income-"+ str(income.id))
        edit_income_link.click()

        input_date =  self.browser.find_element_by_id('id_date')
        input_date.send_keys('12/25/2015')

        input_category =  self.browser.find_element_by_id('id_category')
        input_category.send_keys('others')

        input_amount =  self.browser.find_element_by_id('id_amount')
        input_amount.send_keys('100')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('family treat')

        add_expense_button = self.browser.find_element_by_id('id_submit_income')
        add_expense_button.click()

        self.browser.implicitly_wait(10)