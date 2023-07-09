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
        sleep(1.5)
        detail_side = driver.find_element(By.CLASS_NAME, 'kt-col-5')
        information = detail_side.find_element(By.CLASS_NAME, 'post-page__section--padded').find_elements(By.XPATH, "//div[@class ='kt-base-row kt-base-row--large kt-unexpandable-row']")
        self.title = detail_side.find_element(By.CLASS_NAME, 'kt-page-title__texts').find_elements(By.TAG_NAME, 'div')[0].text
        self.brand = information[0].find_element(By.XPATH, 'a').text
        self.status = information[1].find_elements(By.TAG_NAME, 'p')[-1].text
        self.originality = information[2].find_elements(By.TAG_NAME, 'p')[-1].text
        self.sim_num = information[3].find_elements(By.TAG_NAME, 'p')[-1].text
        self.internal_storage = information[4].find_elements(By.TAG_NAME, 'p')[-1].text
        self.ram = information[5].find_elements(By.TAG_NAME, 'p')[-1].text
        self.color = information[6].find_elements(By.TAG_NAME, 'p')[-1].text
        self.price = information[-1].find_elements(By.TAG_NAME, 'p')[-1].text
        self.description = detail_side.find_elements(By.CLASS_NAME, 'post-page__section--padded')[1].find_element(By.TAG_NAME, 'p').text


class Laptop:
    def __init__(self, link):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        sleep(1.5)
        detail_side = driver.find_element(By.CLASS_NAME, 'kt-col-5')
        information = detail_side.find_element(By.CLASS_NAME, 'post-page__section--padded').find_elements(By.XPATH, "//div[@class ='kt-base-row kt-base-row--large kt-unexpandable-row']")
        self.title = detail_side.find_element(By.CLASS_NAME, 'kt-page-title__texts').find_elements(By.TAG_NAME, 'div')[0].text
        self.price = information[0].find_elements(By.TAG_NAME, 'div')[-1].text
        self.processor = information[1].find_elements(By.TAG_NAME, 'div')[-1].text
        self.producer = information[2].find_elements(By.TAG_NAME, 'div')[-1].text
        self.status = information[3].find_elements(By.TAG_NAME, 'div')[-1].text
        self.monitor_size = information[4].find_elements(By.TAG_NAME, 'div')[-1].text
        self.internal_storage = information[5].find_elements(By.TAG_NAME, 'div')[-1].text
        self.ram = information[6].find_elements(By.TAG_NAME, 'div')[-1].text
        self.operating_sys = information[7].find_elements(By.TAG_NAME, 'div')[-1].text
        self.color = information[8].find_elements(By.TAG_NAME, 'div')[-1].text
        self.description = detail_side.find_elements(By.CLASS_NAME, 'post-page__section--padded')[1].find_element(By.TAG_NAME, 'p').text


class Motorcycle:
    def __init__(self, link):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        sleep(1.5)
        detail_side = driver.find_element(By.CLASS_NAME, 'kt-col-5')
        information = detail_side.find_element(By.CLASS_NAME, 'post-page__section--padded')
        self.title = detail_side.find_element(By.CLASS_NAME, 'kt-page-title__texts').find_elements(By.TAG_NAME, 'div')[0].text
        self.function = information.find_element(By.CLASS_NAME, 'kt-group-row').find_elements(By.TAG_NAME, 'span')[1].text
        self.production_year = information.find_element(By.CLASS_NAME, 'kt-group-row').find_elements(By.TAG_NAME, 'span')[3].text
        self.brand = information.find_elements(By.XPATH, "//div[@class ='kt-base-row kt-base-row--large kt-unexpandable-row']")[0].find_elements(By.TAG_NAME, 'div')[-1].text
        self.price = information.find_elements(By.XPATH, "//div[@class ='kt-base-row kt-base-row--large kt-unexpandable-row']")[-1].find_elements(By.TAG_NAME, 'div')[-1].text
        self.description = detail_side.find_elements(By.CLASS_NAME, 'post-page__section--padded')[1].find_element(By.TAG_NAME, 'p').text


class Tv:
    def __init__(self, link):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        sleep(1.5)
        detail_side = driver.find_element(By.CLASS_NAME, 'kt-col-5')
        self.title = detail_side.find_element(By.CLASS_NAME, 'kt-page-title__texts').find_elements(By.TAG_NAME, 'div')[0].text
        information = detail_side.find_element(By.CLASS_NAME, 'post-page__section--padded').find_elements(By.XPATH, "//div[@class ='kt-base-row kt-base-row--large kt-unexpandable-row']")
        self.description = detail_side.find_elements(By.CLASS_NAME, 'post-page__section--padded')[1].find_element(By.TAG_NAME, 'p').text
        for info in information:
            topic = info.find_elements(By.TAG_NAME, 'div')[0].text
            value = info.find_elements(By.TAG_NAME, 'div')[-1].text
            if topic == 'قیمت':
                self.price = value
            elif topic == 'وضعیت':
                self.status = value
            elif topic == 'سازنده':
                self.producer = value
            elif topic == 'اندازهٔ صفحه':
                self.size = value
            elif topic == 'شناسهٔ کالا':
                self.id = value
            elif topic == 'تعداد پورت HDMI':
                self.hdmi_num = value
            elif topic == 'تعداد پورت USB':
                self.usb_num = value


class Audio:
    def __init__(self, link):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        sleep(1.5)
        detail_side = driver.find_element(By.CLASS_NAME, 'kt-col-5')
        self.title = detail_side.find_element(By.CLASS_NAME, 'kt-page-title__texts').find_elements(By.TAG_NAME, 'div')[0].text
        information = detail_side.find_element(By.CLASS_NAME, 'post-page__section--padded').find_elements(By.XPATH, "//div[@class ='kt-base-row kt-base-row--large kt-unexpandable-row']")
        self.description = detail_side.find_elements(By.CLASS_NAME, 'post-page__section--padded')[1].find_element(By.TAG_NAME, 'p').text
        for info in information:
            topic = info.find_elements(By.TAG_NAME, 'div')[0].text
            value = info.find_elements(By.TAG_NAME, 'div')[-1].text
            if topic == 'قیمت':
                self.price = value
            elif topic == 'وضعیت':
                self.status = value


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
  