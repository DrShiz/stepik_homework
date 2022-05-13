from re import sub
from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")

element = browser.find_element_by_id("button")

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()