from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)
consent_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]')
consent_button.click()

time.sleep(5)
language_button = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language_button.click()

time.sleep(5)
cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

game_duration = time.time() + 5*60
game_on = True

products = driver.find_element(By.XPATH, '//*[@id="products"]')

while game_on:
    clicking_time = time.time() + 5
    click_on = True
    while click_on:
        cookie.click()
        if time.time() > clicking_time:
            click_on = False
    # current_score = int(driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split()[0])

    upgrades = driver.find_elements(By.ID, "upgrades")
    for n in upgrades:
        try:
            active_upgrade = n.find_element(By.CSS_SELECTOR, ".enabled")
            active_upgrade.click()
        except:
            pass

    products_dict = {}

    # active_products = products.find_elements(By.CSS_SELECTOR, ".productName")
    # active_products = products.find_elements(By.XPATH, '//*[@id="product1"]')
    active_products = products.find_elements(By.CSS_SELECTOR, ".storeSection .enabled")
    active_prices = products.find_elements(By.CSS_SELECTOR, ".price")

    for n in range(0, len(active_products)):
        if len(active_products[n].text) > 0:
            products_dict[n] = {
                "name": active_products[n],
                "price": active_prices[n].text
            }
    highest_price = 0
    product_to_buy = ""
    for key in products_dict:
        price = products_dict[key]["price"]
        if "," in price:
            price = price.replace(",", "")
        if int(price) > highest_price:
            highest_price = int(price)
            product_to_buy = products_dict[key]["name"]

    product_to_buy.click()

    if time.time() > game_duration:
        game_on = False

