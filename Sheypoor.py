from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def search_sheipur(target, type):
    '''this function gets a target and type of the product and
    returns a list of tuples that each tuple contains a caption, a price and a link'''
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    #options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=options)
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
    search_table = driver.find_element(By.ID, 'serp-wrapper')
    search_results = search_table.find_elements(By.TAG_NAME, 'article')
    results = []
    for result in search_results:
        caption = result.find_element(By.TAG_NAME, 'h2').text
        link = result.find_element(By.TAG_NAME, 'h2').find_element(By.TAG_NAME, 'a').get_attribute('href')
        price = result.find_element(By.CLASS_NAME, 'item-price').text
        results.append((caption, price, link))
        if len(results) == 20:
            break
    return results
print(search_sheipur("legion 5", 'laptop'))