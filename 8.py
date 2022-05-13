from re import sub
from selenium import webdriver
import time
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test.txt')

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

firstname = browser.find_element_by_name("firstname")
firstname.send_keys('Вася')

lastname = browser.find_element_by_name("lastname")
lastname.send_keys('Петров')

email = browser.find_element_by_name("email")
email.send_keys('a@a')

file = browser.find_element_by_id('file')
file.send_keys(file_path)

submit = browser.find_element_by_class_name('btn')
submit.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()