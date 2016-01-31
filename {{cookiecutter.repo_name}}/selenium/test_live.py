from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase
from selenium.webdriver.phantomjs.webdriver import WebDriver


class LiveTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(LiveTests, cls).setUpClass()
        cls.selenium = WebDriver()

        cls.user = get_user_model().objects.create_user(username="X", password="Y")

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(LiveTests, cls).tearDownClass()
