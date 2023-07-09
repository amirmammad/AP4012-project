import sys
import typing
from time import sleep
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
from PyQt5.uic import loadUi
import mysql.connector as myc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

divar_results = []
digi_results = []
sheipur_results = []
class Mobile:
    def __init__(self, link):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        detail_side = driver.find_element(By.CLASS_NAME, 'kt-col-5')
        information = detail_side.find_element(By.CLASS_NAME, 'post-page__section--padded').find_elements(By.TAG_NAME, 'div')
        self.title = detail_side.find_element(By.CLASS_NAME, 'kt-page-title__texts').find_elements(By.TAG_NAME, 'div')[0].text
        self.brand = information[0].find_element(By.TAG_NAME, 'a').text
        self.status = information[1].find_elements(By.TAG_NAME, 'p')[-1].text
        self.originality = information[2].find_elements(By.TAG_NAME, 'p')[-1].text
        self.sim_num = information[3].find_elements(By.TAG_NAME, 'p')[-1].text
        self.internal_storage = information[4].find_elements(By.TAG_NAME, 'p')[-1].text
        self.ram = information[5].find_elements(By.TAG_NAME, 'p')[-1].text
        self.color = information[6].find_elements(By.TAG_NAME, 'p')[-1].text
        self.price = information[7].find_elements(By.TAG_NAME, 'p')[-1].text
        self.description = detail_side.find_elements(By.CLASS_NAME, 'post-page__section--padded')[1].find_element(By.TAG_NAME, 'p').text


def search_digi(target, type):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    if type == 'mobile':
        driver.get(f'https://www.digikala.com/search/mobile/?q={target}')
    elif type == 'laptop':
        driver.get(f'https://www.digikala.com/search/laptop/?q={target}')
    elif type == 'motorcycle':
        driver.get(f'https://www.digikala.com/search/motorbike/?q={target}')
    elif type == 'tv':
        driver.get(f'https://www.digikala.com/search/tv2/?q={target}')
    elif type == 'audio':
        driver.get(
            f'https://www.digikala.com/search/home-audio-systems/?q={target}')

    sleep(3)
    search_table = driver.find_element(By.XPATH, '//*[@id="ProductListPagesWrapper"]/section[1]/div[2]')
    search_results = search_table.find_elements(By.CLASS_NAME, 'product-list_ProductList__item__LiiNI')
    results = []
    for result in search_results:
        link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
        caption = result.find_element(By.TAG_NAME, 'h3').text
        price = result.find_elements(By.TAG_NAME, 'span')[-1].text
        digi_results.append((caption, price, link))
        results.append((caption, price, link))
        if len(results) == 20:
            break
    for i in range(20):
        result_page.digi_table.setItem(i, 0, QTableWidgetItem(results[i][0]))
        result_page.digi_table.setItem(i, 1, QTableWidgetItem(results[i][1]))
        result_page.digi_table.setItem(i, 2, QTableWidgetItem(results[i][2]))
    return digi_results


def search_divar(target, type):
    '''this function gets a target and type of the product and
    returns a list of tuples that each tuple contains a caption, a price and a link'''
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get("https://divar.ir/s/tehran")
    sleep(3)
    if type == 'mobile':
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[3]')
        category.click()
        sleep(1)
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[2]/ul/li[1]')
        category.click()
        sleep(1)
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[2]/ul/li/ul/li[1]')
    elif type == 'laptop':
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[3]')
        category.click()
        sleep(1)
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[2]/ul/li[2]')
        category.click()
        sleep(1)
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[2]/ul/li/ul/li[1]')
        category.click()
        sleep(1)
    elif type == 'motorcycle':
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[2]')
        category.click()
        sleep(1)
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[2]/ul/li[2]')
        category.click()
        sleep(1)
    elif type == 'tv':
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[3]')
        category.click()
        sleep(1)
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[2]/ul/li[4]')
        category.click()
        sleep(1)
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[2]/ul/li/ul/li[6]')
        category.click()
        sleep(1)
    elif type == 'audio':
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[3]')
        category.click()
        sleep(1)
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[2]/ul/li[4]')
        category.click()
        sleep(1)
        category = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/div/section[1]/ul/li[2]/ul/li/ul/li[4]')
        category.click()
        sleep(1)

    searchbar = driver.find_element(By.XPATH, '//*[@id="app"]/header/nav/div/div[2]/div/div/div[1]/form/input')
    searchbar.send_keys(target)
    searchbar.send_keys(Keys.ENTER)
    sleep(2)
    search_table = driver.find_element(By.CLASS_NAME, 'browse-post-list-f3858')
    search_results = search_table.find_elements(By.TAG_NAME, 'a')
    results = []
    for result in search_results:
        link = result.get_attribute('href')
        caption = result.find_element(By.CLASS_NAME, 'kt-post-card__title').text
        price = result.find_elements(By.CLASS_NAME, 'kt-post-card__description')[-1].text
        divar_results.append((caption, price, link))
        results.append((caption, price, link))
        if len(divar_results) == 20:
            break
    for i in range(20):
        result_page.divar_table.setItem(i, 0, QTableWidgetItem(results[i][0]))
        result_page.divar_table.setItem(i, 1, QTableWidgetItem(results[i][1]))
        result_page.divar_table.setItem(i, 2, QTableWidgetItem(results[i][2]))
    return divar_results


def search_sheipur(target, type):
    '''this function gets a target and type of the product and
    returns a list of tuples that each tuple contains a caption, a price and a link'''
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    #options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.sheypoor.com/')
    sleep(2)
    if type == 'mobile':
        category = driver.find_element(By.XPATH, '//*[@id="categories-card"]/ul[2]/li[5]')
        category.click()
        sleep(2)
        category = driver.find_element(By.XPATH, '//*[@id="categories"]/div/ul/li[1]')
        category.click()
        sleep(1.5)
    elif type == 'laptop':
        category = driver.find_element(By.XPATH, '//*[@id="categories-card"]/ul[2]/li[3]')
        category.click()
        sleep(2)
        category = driver.find_element(By.XPATH, '//*[@id="categories"]/div/ul/li[1]')
        category.click()
        sleep(1.5)
    elif type == 'motorcycle':
        category = driver.find_element(By.XPATH, '//*[@id="categories-card"]/ul[1]/li[1]/div[2]/span[3]')
        category.click()
        sleep(2)
    elif type == 'tv':
        category = driver.find_element(By.XPATH, '//*[@id="categories-card"]/ul[2]/li[3]')
        category.click()
        sleep(2)
        category = driver.find_element(By.XPATH, '//*[@id="categories"]/div/ul/li[2]')
        category.click()
        sleep(1.5)
        category = driver.find_element(By.XPATH, '//*[@id="categories"]/div/ul/li[1]')
        category.click()
        sleep(1)
    elif type == 'audio':
        category = driver.find_element(By.XPATH, '//*[@id="categories-card"]/ul[2]/li[3]')
        category.click()
        sleep(2)
        category = driver.find_element(By.XPATH, '//*[@id="categories"]/div/ul/li[2]')
        category.click()
        sleep(1.5)
        category = driver.find_element(By.XPATH, '//*[@id="categories"]/div/ul/li[2]')
        category.click()
        sleep(1)

    searchbar = driver.find_element(By.XPATH, '//*[@id="advanced-search"]/form/div[1]/div[1]/div/input')
    searchbar.click()
    searchbar.send_keys(target)
    searchbar.send_keys(Keys.ENTER)
    sleep(2)
    results = []
    search_table = driver.find_element(By.ID, 'serp-wrapper')
    search_results = search_table.find_elements(By.TAG_NAME, 'article')
    for result in search_results:
        caption = result.find_element(By.TAG_NAME, 'h2').text
        link = result.find_element(By.TAG_NAME, 'h2').find_element(By.TAG_NAME, 'a').get_attribute('href')
        price = result.find_element(By.CLASS_NAME, 'item-price').text
        sheipur_results.append((caption, price, link))
        results.append((caption, price, link))
        if len(sheipur_results) == 20:
            break
    for i in range(20):
        result_page.sheipur_table.setItem(i, 0, QTableWidgetItem(results[i][0]))
        result_page.sheipur_table.setItem(i, 1, QTableWidgetItem(results[i][1]))
        result_page.sheipur_table.setItem(i, 2, QTableWidgetItem(results[i][2]))
    return sheipur_results


class LoginPage(QDialog):
    def __init__(self):
        super(LoginPage, self).__init__()
        loadUi("login-page.ui", self)
        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.go_signup)

    def login(self):
        username = self.username_line.text()
        password = self.password_line.text()
        db = myc.connect(host="127.0.0.1", user="root",
                         password="", db="ap4022")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user_list WHERE username='" +
                       username + "' and password='" + password + "'")
        result = cursor.fetchone()
        self.username_line.setText("")
        self.password_line.setText("")
        if result:
            self.logo.setText('')
            sleep(1)
            widget.setCurrentIndex(2)
        else:
            self.logo.setText('!')

    def go_signup(self):
        sleep(0.1)
        widget.setCurrentIndex(1)


class SignupPage(QDialog):
    def __init__(self):
        super(SignupPage, self).__init__()
        loadUi("signup-page.ui", self)
        self.signup_button.clicked.connect(self.signup)
        self.login_button.clicked.connect(self.go_login)

    def signup(self):
        username = self.username_line.text()
        password = self.password_line.text()
        email = self.email_line.text()
        db = myc.connect(host="127.0.0.1", user="root",
                         password="", db="ap4022")
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM user_list WHERE username='" + username + "'")
        result = cursor.fetchone()
        if result:
            self.login_question.setText("you have an account lets")
        else:
            cursor.execute("INSERT INTO user_list values('" + username +"','" + password + "','" + email + "','" + '' + "')")
            db.commit()
            self.login_question.setText("signed up successfully, so")

    def go_login(self):
        sleep(0.1)
        widget.setCurrentIndex(0)


class SearchPage(QDialog):
    def __init__(self):
        super(SearchPage, self).__init__()
        loadUi("First-Page.ui", self)
        self.mobile_button.clicked.connect(self.go_mobile_search)
        self.tv_button.clicked.connect(self.go_tv_search)
        self.motorcycle_button.clicked.connect(self.go_motorcycle_search)
        self.audiosystem_button.clicked.connect(self.go_audiosystem_search)
        self.laptop_button.clicked.connect(self.go_laptop_search)

    def go_mobile_search(self):
        sleep(0.1)
        search_word = self.search_line.text()
        search_divar(search_word, 'mobile')
        search_sheipur(search_word, 'mobile')
        search_digi(search_word, 'mobile')
        sleep(1)
        widget.setCurrentIndex(3)

    def go_laptop_search(self):
        sleep(0.1)
        search_word = self.search_line.text()
        search_divar(search_word, 'laptop')
        search_sheipur(search_word, 'laptop')
        search_digi(search_word, 'laptop')
        sleep(1)
        widget.setCurrentIndex(3)

    def go_audiosystem_search(self):
        sleep(0.1)
        search_word = self.search_line.text()
        search_divar(search_word, 'audio')
        search_sheipur(search_word, 'audio')
        search_digi(search_word, 'audio')
        sleep(1)
        widget.setCurrentIndex(3)

    def go_tv_search(self):
        sleep(0.1)
        search_word = self.search_line.text()
        search_divar(search_word, 'tv')
        search_sheipur(search_word, 'tv')
        search_digi(search_word, 'tv')
        sleep(1)
        widget.setCurrentIndex(3)

    def go_motorcycle_search(self):
        sleep(0.1)
        search_word = self.search_line.text()
        search_divar(search_word, 'motorcycle')
        search_sheipur(search_word, 'motorcycle')
        search_digi(search_word, 'motorcycle')
        sleep(1)
        widget.setCurrentIndex(3)


class ResultPage(QDialog):
    def __init__(self):
        super(ResultPage, self).__init__()
        loadUi("second-page.ui", self)
        self.back_to_main_page_button.clicked.connect(self.back_to_search_page)
        
    def back_to_search_page(self):
        digi_results.clear()
        divar_results.clear()
        sheipur_results.clear()
        sleep(0.1)
        widget.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    login_page = LoginPage()
    signup_page = SignupPage()
    search_page = SearchPage()
    result_page = ResultPage()
    widget.addWidget(login_page)
    widget.addWidget(signup_page)
    widget.addWidget(search_page)
    widget.addWidget(result_page)
    widget.setCurrentIndex(0)
    widget.setFixedHeight(809)
    widget.setFixedWidth(1120)
    widget.show()

    app.exec_()