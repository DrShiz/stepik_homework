from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select





browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

sum = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum))

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()