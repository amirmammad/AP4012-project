from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def search(target, type):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.minimize_window()
    driver.get(f'https://www.digikala.com/search/?q={target}')
    sleep(3)
    if type == 'mobile':
        category = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/section[2]/div/div/div[1]/div[2]')
        category.click()
        sleep(2)
        category = driver.find_element(By.XPATH, '//*[@id="ProductListPagesWrapper"]/section[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/div')
        category.click()
        sleep(3)



print(search('a14', 'mobile'))
        

