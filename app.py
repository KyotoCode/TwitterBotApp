from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwiterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(
            executable_path=r'C:\Users\mihaj\AppData\Local\Programs\Python\Python38-32\geckodriver.exe')

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(7)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)


mika = TwiterBot('username', 'password')
mika.login()
