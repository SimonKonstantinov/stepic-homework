import math, time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    
  
    for n in ['robotCheckbox', 'robotsRule']:
        browser.find_element_by_id(n).click()
        browser.execute_script("return arguments[0].scrollIntoView(true);",   browser.find_element_by_id(n))
    browser.find_element_by_tag_name("button").click()
    

finally:
    time.sleep(20)
    browser.quit()
