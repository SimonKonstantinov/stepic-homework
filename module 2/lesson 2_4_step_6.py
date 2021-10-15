import math, time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = " http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_id("button")
    

finally:
    time.sleep(20)
    browser.quit()
