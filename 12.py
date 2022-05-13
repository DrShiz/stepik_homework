from re import sub
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
button = browser.find_element_by_id('book')
button.click()

x = browser.find_element_by_id('input_value').text
y = calc(x)
answer = browser.find_element_by_id('answer')
answer.send_keys(y)

button = browser.find_element_by_id('solve')
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()