from logging import root

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # open site
    driver.get("https://telranedu.pages.dev/login")
    #driver.get("https://icarro-v1.netlify.app/login")

    #by tag name
    div = driver.find_element(By.TAG_NAME,"div")
    div_1 = driver.find_element(By.CSS_SELECTOR,"div")
    div_2 = driver.find_element(By.XPATH,"//div")
    div_3 = driver.find_elements(By.XPATH,"//div")

    h1 = driver.find_element(By.TAG_NAME,"h1")
    h1_1 = driver.find_element(By.CSS_SELECTOR,"h1")
    h1_2 = driver.find_element(By.XPATH,"//h1")

    input_box = driver.find_element(By.TAG_NAME,"input")
    input_1 = driver.find_element(By.CSS_SELECTOR,"input")
    input_2 = driver.find_element(By.XPATH,"//input")


    a_list = driver.find_elements(By.TAG_NAME,"a")
    a_1 = driver.find_elements(By.CSS_SELECTOR,"a")
    a_2 = driver.find_elements(By.XPATH,"//a")
    print(len(a_list))

    #by class
    container = driver.find_element(By.CLASS_NAME,"container")
    container_1 = driver.find_element(By.CSS_SELECTOR,".container")
    container_2 = driver.find_element(By.XPATH,"//div[@class='container']")

    navbar = driver.find_element(By.CLASS_NAME,"navbar-component_nav__1X_4m")
    navbar_1 = driver.find_element(By.CSS_SELECTOR,".navbar-component_nav__1X_4m")
    navbar_2 = driver.find_element(By.XPATH,"//*[@class='navbar-component_nav__1X_4m']")

    form = driver.find_element(By.CLASS_NAME,"login_login__3EHKB")
    form_1 = driver.find_element(By.CSS_SELECTOR,".login_login__3EHKB")
    form_2 = driver.find_element(By.XPATH,"//*[@class='login_login__3EHKB']")

    #by id
    root = driver.find_element(By.ID,"root")
    root_1 = driver.find_element(By.CSS_SELECTOR,"#root")
    root_2 = driver.find_element(By.XPATH,"//*[@id='root']")
    #by id list
    root_2 = driver.find_elements(By.ID,"root")
    root_3 = driver.find_elements(By.CSS_SELECTOR,"#root")

    #by attribute[]
    name_input = driver.find_element(By.CSS_SELECTOR,"[placeholder='Email']")
    name_input4=driver.find_element(By.XPATH,"//*[@placeholder='Email']")

    home = driver.find_element(By.CSS_SELECTOR,"[href='/home']")
    home_1 = driver.find_element(By.XPATH,"//*[@href='/home']")

    name_input2 = driver.find_element(By.CSS_SELECTOR,"input[name='email']")
    name_input3 = driver.find_element(By.XPATH,"//input[@name='email']")

    #by Name
    name_input_1 = driver.find_element(By.NAME,"email")


    #by text only xPath
    login_button = driver.find_element(By.XPATH,"//*[text()='Login']")


    #ilcarro
    #start -> ^
    #starts = driver.find_element(By.CSS_SELECTOR,"[class^='login']")
    #end ->$
    #end = driver.find_element(By.CSS_SELECTOR,"[class$='auth-page']")
    #contains -> *
    #contains = driver.find_element(By.CSS_SELECTOR,"[class*='container']")







finally:
    driver.quit()

#driver.close()