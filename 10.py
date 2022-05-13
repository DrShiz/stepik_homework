from re import sub
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

button = browser.find_element_by_class_name('trollface')
button.click()

browser.switch_to.window(browser.window_handles[1])

x = browser.find_element_by_id('input_value').text
y = calc(x)
answer = browser.find_element_by_id('answer')
answer.send_keys(y)

button = browser.find_element_by_class_name('btn')
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()