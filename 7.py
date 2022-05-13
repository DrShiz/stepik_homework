from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")
x = browser.find_element_by_id('input_value').text
y = calc(x)

element = browser.find_element_by_id('answer')
element.send_keys(y)

button = browser.find_element_by_id('robotCheckbox')
button.click()

button = browser.find_element_by_id('robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

button = browser.find_element_by_class_name('btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла