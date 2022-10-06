from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
delay = 30
driver = webdriver.Chrome('C:/Drive D/selenium/chromedriver.exe')
driver.maximize_window()
driver.get('https://www.vlr.gg/event/stats/996/skyesports-champions-series')
data = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/div/div[2]/div/table')
WebDriverWait(browser,delay).until(EC.visibility_of(data))
data = data.get_attribute('outerHTML')
df = pd.read_html(data)
df = df[0].dropna(axis = 0,thresh = 4)
df = pd.DataFrame(df)
df.to_csv('SCS.csv',mode = 'a',index=False,header=True)