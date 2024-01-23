import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_login_user(self):
        browser = self.browser
        link = "https://stepik.org/catalog"
        browser.get(link)
        link = browser.find_element(By.LINK_TEXT, "Войти")
        link.click()

        input1 = browser.find_element(By.NAME, "login")
        input1.send_keys("albinos55522@gmail.com")

        input2 = browser.find_element(By.NAME, "password")
        input2.send_keys("1234fkz1234")

        button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
        button.click()

        self.assertEqual(browser.current_url, "https://stepik.org/catalog?auth=login", 'correct login user')

    def test_register_user(self):
        browser = self.browser
        link = "https://stepik.org/catalog"
        browser.get(link)

        link = browser.find_element(By.LINK_TEXT, "Регистрация")
        link.click()

        time.sleep(5)
        
        button = browser.find_element(By.CSS_SELECTOR, ".btn-google > img")
        button.click()

        time.sleep(5)
        self.assertIn( "https://accounts.google.com",browser.current_url , 'correct reg user')

    def tearDown(self):
        self.browser.quit()

class TestUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

        link = "https://stepik.org/catalog"
        self.browser.get(link)

        link = self.browser.find_element(By.LINK_TEXT, "Войти")
        link.click()
        time.sleep(5)
        input1 = self.browser.find_element(By.NAME, "login")
        input1.send_keys("albinos55522@gmail.com")

        input2 = self.browser.find_element(By.NAME, "password")
        input2.send_keys("1234fkz1234")

        time.sleep(5)

        button = self.browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
        button.click()

        time.sleep(10)

    def test_search_curse(self):
        browser = self.browser
        link = "https://stepik.org/catalog"
        browser.get(link)

        time.sleep(5)
        input3 = browser.find_element(By.CLASS_NAME, "search-form__input ")
        input3.send_keys("Математика")

        time.sleep(5)
        button2 = browser.find_element(By.CLASS_NAME, "button_with-loader")
        button2.click()

        time.sleep(10)
        link2 = browser.find_element(By.LINK_TEXT, "ОГЭ МАТЕМАТИКА 2024")

        self.assertIsNone(link2.get_attribute("media"), 'correct search curse')

    def test_pass_curse(self):
        browser = self.browser
        link = "https://stepik.org/catalog"
        browser.get(link)

        time.sleep(5)

        button2 = browser.find_element(By.CSS_SELECTOR, ".tab > .tab__item:nth-child(2) > button")
        button2.click()
        time.sleep(10)
        link2 = browser.find_element(By.LINK_TEXT, '"Поколение Python": курс для начинающих')
        link2.click()

        time.sleep(10)

        button3 = browser.find_element(By.CSS_SELECTOR, ".button")
        button3.click()

        time.sleep(10)

        self.assertIn( "https://stepik.org/lesson",browser.current_url , 'correct pass curse')


    def test_save_curse(self):
        browser = self.browser
        link = "https://stepik.org/catalog"
        browser.get(link)

        time.sleep(5)

        button2 = browser.find_element(By.CSS_SELECTOR, ".tab > .tab__item:nth-child(2) > button")
        button2.click()
        time.sleep(10)
        link2 = browser.find_element(By.LINK_TEXT, '"Поколение Python": курс для продвинутых')
        link2.click()

        time.sleep(5)

        button3 = browser.find_element(By.CSS_SELECTOR, ".course-promo-enrollment__wishlist-btn")
        button3.click()
        time.sleep(3)

        link2 = browser.find_element(By.XPATH, "//span[contains(.,'Курс «\"Поколение Python\": курс для продвинутых» добавлен в список желаний.')]")
        self.assertIsNone(link2.get_attribute("media"), 'correct save curse')
     

    def test_pass_lesson(self):
        browser = self.browser
        link = "https://stepik.org/catalog"
        browser.get(link)

        time.sleep(5)

        button2 = browser.find_element(By.CSS_SELECTOR, ".tab > .tab__item:nth-child(2) > button")
        button2.click()
        time.sleep(10)
        link2 = browser.find_element(By.LINK_TEXT, '"Поколение Python": курс для начинающих')
        link2.click()

        time.sleep(10)

        button3 = browser.find_element(By.XPATH, "//button[contains(.,'Продолжить')]")
        button3.click()

        time.sleep(10)
        
        self.assertIn( "https://stepik.org/lesson/290248",browser.current_url , 'correct pass curse')

    def test_get_olympia(self):
        browser = self.browser
        link = "https://stepik.org/catalog"
        browser.get(link)

        time.sleep(5)

        link = "https://stepik.org/course/107815/promo"
        browser.get(link)
        time.sleep(5)
        button3 = browser.find_element(By.CSS_SELECTOR, ".button")
        button3.click()
        time.sleep(10)
        self.assertIn( "https://stepik.org/lesson/664646",browser.current_url , 'correct get olympia')


    def test_get_sertificate(self):
        browser = self.browser
        link = "https://stepik.org/catalog"
        browser.get(link)

        time.sleep(5)

        img = browser.find_element(By.CSS_SELECTOR, "img.navbar__profile-img")
        img.click()

        time.sleep(5)
        link3 = browser.find_element(By.LINK_TEXT, 'Профиль')
        link3.click()

        time.sleep(10)

        h3 = browser.find_element(By.CSS_SELECTOR, '.st-h3:nth-child(3)')

        self.assertIsNone(h3.get_attribute("media"), 'correct get sertificate')

    def test_create_curse(self):
        browser = self.browser
        link = "https://stepik.org/catalog"
        browser.get(link)

        time.sleep(5)

        link2 = browser.find_element(By.LINK_TEXT, 'Преподавание')
        link2.click()

        time.sleep(5)

        button = browser.find_element(By.XPATH, "//span[contains(.,'Новый курс')]")
        button.click()
        time.sleep(5)
        
        input3 = browser.find_element(By.XPATH, "//label/div/input")
        input3.send_keys("TEST")
        time.sleep(5)
        
        button2 = browser.find_element(By.XPATH, "//button[contains(.,'Создать курс')]")
        button2.click()
        time.sleep(10)

        self.assertIn( "https://stepik.org/course/",browser.current_url , 'correct create curse')

    def test_create_lesson(self):
        browser = self.browser
        link = "https://stepik.org/catalog"
        browser.get(link)

        time.sleep(5)

        link2 = browser.find_element(By.LINK_TEXT, 'Преподавание')
        link2.click()

        time.sleep(5)

        link3 = browser.find_element(By.LINK_TEXT, 'TEST')
        link3.click()

        time.sleep(5)

        button3 = browser.find_element(By.XPATH, "//a[contains(.,'Редактировать содержание')]")
        button3.click()

        time.sleep(5)
        button4 = browser.find_element(By.XPATH, "//button[contains(.,' Новый модуль')]")
        button4.click()

        input4 = browser.find_element(By.XPATH, "//div[2]/div/div/input")
        input4.send_keys("Lesson 1")

        time.sleep(5)
        button5 = browser.find_element(By.XPATH, "//button[contains(.,' Создать урок')]")
        button5.click()
        time.sleep(5)
        button6 = browser.find_element(By.XPATH, "//button[contains(.,'Сохранить')]")
        button6.click()
        time.sleep(5)

        link4 = browser.find_element(By.XPATH, "//span[contains(.,'Содержание')]")
        link4.click()
        time.sleep(5)

        link5 = browser.find_element(By.XPATH, "//div[2]/div[2]/div/a")
        link5.click()
        time.sleep(10)

        self.assertIn( "https://stepik.org/lesson",browser.current_url , 'correct create lesson')

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()