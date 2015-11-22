
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from application.models import Expense


class IncomeTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_display_the_income_list(self):
        self.browser.get('http://localhost:8081/income')
        self.assertIn('Income List', self.browser.title)


    def test_can_go_to_new_income_page(self):
        self.browser.get('http://localhost:8081/income')

