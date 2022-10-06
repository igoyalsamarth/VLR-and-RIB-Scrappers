from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
delay = 30
driver = webdriver.Chrome('C:/Drive D/selenium/chromedriver.exe')
driver.maximize_window()
driver.get('https://rib.gg/players/skrossi/1685?tab=overview/')
#driver.implicitly_wait(15)
for i in range(3,14):
    content = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/a['+str(i)+']')
    WebDriverWait(browser,delay).until(EC.visibility_of(content))
    content.click()
    driver.implicitly_wait(15)
    data = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[5]/div[3]/table')
    WebDriverWait(browser,delay).until(EC.visibility_of(data))
    data = data.get_attribute('outerHTML')
    df = pd.read_html(data)
    df = df[0].dropna(axis = 0,thresh = 4)
    df = pd.DataFrame(df)
    df.to_csv('GE_MultikillandClutches_SCS.csv',mode = 'a',index=False,header=False)

    driver.back()
    #driver.implicitly_wait(15)