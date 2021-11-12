import time
from selenium import webdriver

class YandexAutomate:
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='./chromedriver')


    def login(self, email, password):
        self.browser.get(
            "https://passport.yandex.ru/auth/welcome?from=mail&origin=hostroot_homer_auth_L_ru&retpath=https%3A%2F%2Fmail."
            "yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1")
        self.browser.find_element_xpath(
        	"//input[@data-t=field:input-login]").send_keys(email)
        self.browser.find_element_xpath(
        	"//button[@data-t=button:action:passp:sign-in]").click()
        time.sleep(2)
        self.browser.find_element_xpath(
        	"//input[@data-t=field:input-passwd]").send_keys(password)
        self.browser.find_element_xpath(
            "//button[@data-t=button:action]").click()

if __name__ == '__main__':
    yandex = YandexAutomate()
    yandex.login('test_sample@yandex.ru', 'test123')
