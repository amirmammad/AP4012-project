from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

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


def search(target, type):
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
        results.append((caption, price, link))
        if len(results) == 20:
            break
    return results
