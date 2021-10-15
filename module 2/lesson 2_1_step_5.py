from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/math.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
    browser.get(link)
  
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    option3 = browser.find_element_by_id("answer").send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox").click()

    option2 =  browser.find_element_by_css_selector("[for='robotCheckbox']").click()

   
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


