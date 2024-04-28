import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import getpass
from project import login, profile, No_of_likes_and_comments, post_text, friend_list

class TestFacebookScrapper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup web driver
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs", prefs)
        s = Service("C:/Users/peerf/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s, options=options)
        cls.driver.get("https://www.facebook.com/")

    @classmethod
    def tearDownClass(cls):
        # Cleanup
        cls.driver.quit()

    def setUp(self):
        # Login before each test
        login(self.driver)

    def test_profile(self):
        # Test profile function
        html_content = profile(self.driver)
        self.assertIsInstance(html_content, BeautifulSoup)

    def test_No_of_likes_and_comments(self):
        # Test No_of_likes_and_comments function
        html_content = profile(self.driver)
        with open('test_data.html', 'w', encoding='utf-8') as f:
            f.write(str(html_content))
        soup = BeautifulSoup(open('test_data.html', encoding='utf-8'), 'html.parser')
        self.assertIsNotNone(No_of_likes_and_comments(soup))

    def test_post_text(self):
        # Test post_text function
        html_content = profile(self.driver)
        with open('test_data.html', 'w', encoding='utf-8') as f:
            f.write(str(html_content))
        soup = BeautifulSoup(open('test_data.html', encoding='utf-8'), 'html.parser')
        self.assertIsNotNone(post_text(soup))

    def test_friend_list(self):
        # Test friend_list function
        self.assertIsNotNone(friend_list(self.driver))


if __name__ == "__main__":
    unittest.main()

