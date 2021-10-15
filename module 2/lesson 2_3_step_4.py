import math, time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_tag_name('button').click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id('input_value').text

    answer = browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_tag_name("button").click()
    

finally:
    time.sleep(20)
    browser.quit()
