from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    y = calc(x)

    element = browser.find_element_by_id('answer')
    element.send_keys(y)

    button = browser.find_element_by_id('robotCheckbox')
    button.click()

    button = browser.find_element_by_id('robotsRule')
    button.click()

    button = browser.find_element_by_id('robotsRule')
    button.click()

    button = browser.find_element_by_class_name('btn-default')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла