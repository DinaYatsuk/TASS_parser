from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def initialize_driver():
    return webdriver.Chrome()


def navigate_to_url(driver, url):
    driver.get(url)


#Скролл страницы до кнопки "Показать больше материалов"
# def click_button_by_xpath(driver, xpath):
#     # Scroll the entire page
#     button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
#
#     # Scroll to the button using JavaScript
#     driver.execute_script("arguments[0].scrollIntoView();", button)
#
#     # Click the button
#     button.click()


#Данный вариант функции можно применять, когда необходимо загрузить лишь часть

# def scroll_page(driver, pixel_increment=5000, max_scroll=300):
#    current_scroll = 0
#    while current_scroll < max_scroll:
#        driver.execute_script(f"window.scrollBy(0, {pixel_increment});")
#        time.sleep(3)  # Adjust the sleep time as needed
#        current_scroll += 1

def scroll_page(driver, pixel_increment=5000):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script(f"window.scrollBy(0, {pixel_increment});")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height


def get_links(driver):
    all_links = []
    news_links = driver.find_elements(By.CLASS_NAME, "tass_pkg_link-v5WdK")
    for my_href in news_links:
        all_links.append(my_href.get_attribute("href"))
    return all_links

#Попытка вытащить даты
# def get_date(driver):
#    all_dates = []
#    dates = driver.find_elements(By.CLASS_NAME, "tass_pkg_marker-JPOGl")
#    for date in dates:
#        all_dates.append(date.text.replace('\xa0', ' '))
#    return all_dates


def process_website():
    driver = initialize_driver()
    url = "https://tass.ru/tag/ssha"
    navigate_to_url(driver, url)
    time.sleep(15)
   # button_xpath = '//button[@class="ds_ext_button-4gOSC ds_ext_button--secondary-wd4YM ds_ext_button--large-3Q9j1 ds_ext_button--stretch-F6Pzo"]'

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # click_button_by_xpath(driver, button_xpath)
    scroll_page(driver)

    all_links = get_links(driver)


    print(f'Total number of links: {len(set(all_links))}')

    driver.quit()

    return all_links




