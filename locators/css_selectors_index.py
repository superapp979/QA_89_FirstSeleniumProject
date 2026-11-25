from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # open site
    driver.get("https://telranedu.pages.dev/login")

    #by tag name
    div = driver.find_element(By.TAG_NAME,"div")
    div_1 = driver.find_element(By.CSS_SELECTOR,"div")

    h1 = driver.find_element(By.TAG_NAME,"h1")
    h1_1 = driver.find_element(By.CSS_SELECTOR,"h1")

    input_box = driver.find_element(By.TAG_NAME,"input")
    input_1 = driver.find_element(By.CSS_SELECTOR,"input")

    a_list = driver.find_elements(By.TAG_NAME,"a")
    a_1 = driver.find_elements(By.CSS_SELECTOR,"a")
    print(len(a_list))
    #by class

    #by id

finally:
    driver.quit()

#driver.close()