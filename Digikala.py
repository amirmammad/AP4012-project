from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def search(target, type): 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    #options.add_argument("--headless")
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
        driver.get(f'https://www.digikala.com/search/home-audio-systems/?q={target}')
    
    sleep(3)
    search_table = driver.find_element(By.XPATH, '//*[@id="ProductListPagesWrapper"]/section[1]/div[2]')
    search_results = search_table.find_elements(By.CLASS_NAME, 'product-list_ProductList__item__LiiNI')
    results = []
    for result in search_results:
        link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
        caption = result.find_element(By.TAG_NAME, 'h3').text
        price = result.find_elements(By.TAG_NAME, 'span')[-1].text
        results.append((caption, price, link))
        if len(results) == 20:
            break
    return results
print(search('a52', 'mobile'))