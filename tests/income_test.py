
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
        add_income_link = self.browser.find_element_by_link_text('Add Income')
        add_income_link.click()
        #self.browser.implicitly_wait(10)

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

    def test_can_cancel_add_income(self):
        self.browser.get('http://localhost:8081/income/new')
        cancel_income_button = self.browser.find_element_by_id('id_cancel_income')
        cancel_income_button.click()
        #self.assertIn('Income List', self.browser.title)

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

# Can submit edited income with valid values
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

# Can cancel edited edit forms
    def test_can_cancel_edit_income(self):
        income = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        cancel_income_link = self.browser.find_element_by_id("edit-income-"+ str(income.id))
        cancel_income_link.click()

        cancel_income_button = self.browser.find_element_by_id('id_cancel_income')
        cancel_income_button.click()
        #self.assertIn('Income List', self.browser.title)

# Account and Category are empty
    def test_valid_form_acct_category(self):
        income = Income.objects.create(date='2015-12-11', amount='100', notes='test')
        data = {'date': income.date, 'amount': income.amount, 'notes': income.notes}
        form = IncomeForm(data=data)
        self.assertTrue(form.is_valid())

# Incorrect date format
    def test_valid_form_invalid_date(self):
        income = Income.objects.create(date='2015/12/11', amount='100', notes='test')
        data = {'date': income.date, 'amount': income.amount, 'notes': income.notes}
        form = IncomeForm(data=data)
        self.assertTrue(form.is_valid())

# Post empty form
    def test_for_invalid_input_renders_list_template(self):
        response = self.post_invalid_input()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html') 

# Invalid_input_shows_error_on_page
    def test_for_invalid_input_shows_error_on_page(self):
        response = self.post_invalid_input()
        self.assertContains(response, escape(EMPTY_ITEM_ERROR))

# Account and Category are empty on edit
    def test_valid_form_acct_category_edit(self):
        inc = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        edit_income_link = self.browser.find_element_by_id("edit-income-"+ str(inc.id))
        edit_income_link.click()

        income = Income.objects.create(date='2015-12-11', amount='100', notes='test')
        data = {'date': income.date, 'amount': income.amount, 'notes': income.notes}
        form = IncomeForm(data=data)
        self.assertTrue(form.is_valid())

# Incorrect date format on edit
    def test_valid_form_invalid_date_edit(self):
        inc = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        edit_income_link = self.browser.find_element_by_id("edit-income-"+ str(inc.id))
        edit_income_link.click()

        income = Income.objects.create(date='2015/12/11', amount='100', notes='test')
        data = {'date': income.date, 'amount': income.amount, 'notes': income.notes}
        form = IncomeForm(data=data)
        self.assertTrue(form.is_valid())

# Post empty form on edit
    def test_for_invalid_input_renders_list_template_edit(self):
        inc = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        edit_income_link = self.browser.find_element_by_id("edit-income-"+ str(inc.id))
        edit_income_link.click()

        response = self.post_invalid_input()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html') 

# Invalid_input_shows_error_on_page on edit
    def test_for_invalid_input_shows_error_on_page_edit(self):
        inc = Income.objects.latest('id')
        self.browser.get('http://localhost:8081/income')
        edit_income_link = self.browser.find_element_by_id("edit-income-"+ str(inc.id))
        edit_income_link.click()

        response = self.post_invalid_input()
        self.assertContains(response, escape(EMPTY_ITEM_ERROR))