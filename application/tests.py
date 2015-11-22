#
# from django.test import TestCase, LiveServerTestCase
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#
# from django.core.urlresolvers import resolve
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# # from django.db import models
# from application.models import Expense
#
# # from django.contrib.auth.models import Expense
# import unittest
#
# class ExpenseTest(StaticLiveServerTestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#         self.browser.implicitly_wait(3)
#
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_can_display_the_income_list(self):
#
#         self.browser.get('http://localhost:8081/expense')
#
#         self.assertIn('Expense List', self.browser.title)
#
#         self.fail('Finish the test!')
#
#     def test_can_visit_add_expense_page(self):
#         self.browser.get('http://localhost:8081/expense')
#
#         add_expense_link = self.browser.find_element_by_link_text('Add Expense')
#         add_expense_link.click()
#         self.browser.implicitly_wait(10)
#
#         self.assertIn('New Expense', self.browser.title)
#         self.assertIn('This is my new expense page.', self.browser.page_source)
#
#     def test_can_delete_an_epxense_item(self):
#         self.browser.get('http://localhost:8081/expense')
#         delete_expense_link = self.browser.find_element_by_id('delete-exoense-1')
#         delete_expense_link.click()
#
#
#         alert = self.browser.switch_to.alert
#         alert.accept()
#
#         self.assertIn('This is my new expense page.', self.browser.page_source)
#
#
