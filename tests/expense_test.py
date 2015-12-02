
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

        category = Category(name="others", type="expense")
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
        self.assertIn('others', self.browser.page_source)
        self.assertIn('1000', self.browser.page_source)


    def test_can_visit_add_expense_page(self):
        self.browser.get('http://localhost:8081/expense')
        add_expense_link = self.browser.find_element_by_link_text('Add Expense')
        add_expense_link.click()
        self.browser.implicitly_wait(10)

        self.assertIn('New Expense', self.browser.title)
        self.assertIn('Add Expense Form', self.browser.page_source)


    def test_can_delete_an_expense_item(self):
        expense = Expense.objects.latest('id')
        self.browser.get('http://localhost:8081/expense')
        delete_expense_link = self.browser.find_element_by_id("delete-expense-"+ str(expense.id))
        delete_expense_link.click()


        alert = self.browser.switch_to.alert
        alert.accept()
        self.browser.implicitly_wait(3)
        self.assertNotIn('gift', self.browser.page_source)
        self.assertNotIn('savings', self.browser.page_source)
        self.assertNotIn('others', self.browser.page_source)
        self.assertNotIn('1000', self.browser.page_source)

    def test_cancels_delete_of_an_expense_item(self):
        expense = Expense.objects.latest('id')
        self.browser.get('http://localhost:8081/expense')
        delete_expense_link = self.browser.find_element_by_id("delete-expense-"+ str(expense.id))
        delete_expense_link.click()


        alert = self.browser.switch_to.alert
        alert.dismiss()
        self.browser.implicitly_wait(20)
        self.assertIn('gift', self.browser.page_source)
        self.assertIn('savings', self.browser.page_source)
        self.assertIn('others', self.browser.page_source)
        self.assertIn('1000', self.browser.page_source)

    def test_can_add_expense_successfully(self):
        self.browser.get('http://localhost:8081/expense/new')
        input_date =  self.browser.find_element_by_id('id_date')
        input_date.send_keys('12/25/2015')

        input_category =  self.browser.find_element_by_id('id_category')
        input_category.send_keys('others')

        input_amount =  self.browser.find_element_by_id('id_amount')
        input_amount.send_keys('100')

        input_account =  self.browser.find_element_by_id('id_account')
        input_account.send_keys('savings')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('family treat')

        add_expense_button = self.browser.find_element_by_id('id_submit_expense')
        add_expense_button.click()

        self.assertIn('Expense List', self.browser.title)

        self.assertIn('Expense List', self.browser.title)
        self.assertIn('family treat', self.browser.page_source)
        self.assertIn('savings', self.browser.page_source)
        self.assertIn('others', self.browser.page_source)
        self.assertIn('100', self.browser.page_source)

    def test_cancels_add_expense_successfully(self):
        self.browser.get('http://localhost:8081/expense/new')
        input_date =  self.browser.find_element_by_id('id_date')
        input_date.send_keys('12/25/2015')

        input_category =  self.browser.find_element_by_id('id_category')
        input_category.send_keys('others')

        input_amount =  self.browser.find_element_by_id('id_amount')
        input_amount.send_keys('100')

        input_account =  self.browser.find_element_by_id('id_account')
        input_account.send_keys('savings')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('family treat')

        cancel_expense_button = self.browser.find_element_by_id('id_cancel_expense')
        cancel_expense_button.click()

        self.assertIn('Expense List', self.browser.title)
        self.assertNotIn('family treat', self.browser.page_source)

    def test_can_visit_edit_expense_page_(self):
       expense = Expense.objects.latest('id')
        self.browser.get('http://localhost:8081/expense')
        edit_expense_link = self.browser.find_element_by_id("edit-expense-"+ str(expense.id))
        edit_expense_link.click()

        self.assertIn('Edit Expense', self.browser.page_source)
    #
    def test_can_update_expense_from_user_edit(self):
        expense = Expense.objects.latest('id')
        self.browser.get('http://localhost:8081/expense')
        edit_expense_link = self.browser.find_element_by_id("edit-expense-"+ str(expense.id))
        edit_expense_link.click()

        input_date =  self.browser.find_element_by_id('id_date')
        input_date.send_keys('12/25/2015')

        input_category =  self.browser.find_element_by_id('id_category')
        input_category.send_keys('others')

        input_amount =  self.browser.find_element_by_id('id_amount')
        input_amount.send_keys('100')

        input_account =  self.browser.find_element_by_id('id_account')
        input_account.send_keys('savings')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('family treat')

        update_expense_button = self.browser.find_element_by_id('id_submit_expense')
        update_expense_button.click()

        self.assertIn('Expense List', self.browser.title)

        self.assertIn('Expense List', self.browser.title)
        self.assertIn('family treat', self.browser.page_source)
        self.assertIn('savings', self.browser.page_source)
        self.assertIn('others', self.browser.page_source)
        self.assertIn('100', self.browser.page_source)

    def test_cancels_update_expense(self):
        expense = Expense.objects.latest('id')
        self.browser.get('http://localhost:8081/expense')
        edit_expense_link = self.browser.find_element_by_id("edit-expense-"+ str(expense.id))
        edit_expense_link.click()

        input_date =  self.browser.find_element_by_id('id_date')
        input_date.send_keys('12/25/2015')

        input_category =  self.browser.find_element_by_id('id_category')
        input_category.send_keys('others')

        input_amount =  self.browser.find_element_by_id('id_amount')
        input_amount.send_keys('100')

        input_account =  self.browser.find_element_by_id('id_account')
        input_account.send_keys('savings')

        input_notes =  self.browser.find_element_by_id('id_notes')
        input_notes.send_keys('family treat')

        cancel_expense_button = self.browser.find_element_by_id('id_cancel_expense')
        cancel_expense_button.click()

        self.assertIn('Expense List', self.browser.title)
        self.assertNotIn('family treat', self.browser.page_source)

    def test_system_notify_user_of_correct_update(self):
        self.browser.get('http://localhost:8081/expense/edit')
        self.assertIn('The expense update list has been updated', response.content)

    def test_blank_fields_when_submit(self):
        expense = Expense.objects.latest('id')
        self.browser.get('http://localhost:8081/expense')
        edit_expense_link = self.browser.find_element_by_id("edit-expense-"+ str(expense.id))
        edit_expense_link.click()

        self.browser.find_element_by_id('id_update_expense').send_keys('\n')
        error = self.browser.find_element_by_css_selector('has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        self.browser.find_element_by_id('id_date').send_keys('\n')
        self.check_for_row_in_list_table('12/25/2015')
        error = self.browser.find_element_by_css_selector('has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        self.browser.find_element_by_id('id_category').send_keys('\n')
        self.check_for_row_in_list_table('others')
        error = self.browser.find_element_by_css_selector('has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        self.browser.find_element_by_id('id_account').send_keys('\n')
        self.check_for_row_in_list_table('savings')
        error = self.browser.find_element_by_css_selector('has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        self.browser.find_element_by_id('id_notes').send_keys('\n')
        self.check_for_row_in_list_table('family treat')
                



    


   # def test_add_expense_valid_data(self):
   #    form = NewExpenseForm(
   #          'date': "2015-12-01",
   #          'category': "food",
   #          'amount': "100.0",
   #          'account': "savings",
   #          'notes': "none",
   #  }, entry=self.entry)
   #  self.assertTrue(form.is_valid())
   #  Expense = form.save()
   #  self.assertEqual(Expense.date, "2015-12-01")
   #  self.assertEqual(Expense.category, "food")
   #  self.assertEqual(Expense.amount, "100.0")
   #  self.assertEqual(Expense.account, "savings")
   #  self.assertEqual(Expense.notes, "none")
   #  self.assertEqual(Expense.entry, self.entry)
   #
   #  def test_add_expense_blank_data(self):
   #      form = NewExpenseForm({}, entry=self.entry)
   #      self.assertFalse(form.is_valid())
   #      self.assettEqual(form.errors,{
   #          'date': ['required']',
   #          'category': ['required']',
   #          'amount': ['required']',
   #          'account': ['required']',
   #          'notes': ['required']',
   #      })
