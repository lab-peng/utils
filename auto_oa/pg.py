from config import url 

import random 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# The below two lines fixed USB error logging
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH, options=options)

pg_url = url + '?next=/pg/pg_list/'
driver.get(pg_url)
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
login = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')

username.send_keys("user63")
password.send_keys("pass63")
login.click()


create_button = driver.find_element(By.CSS_SELECTOR, '#card_add')
create_button.click()

driver.find_element(By.CSS_SELECTOR, 'input[name=client]').send_keys('世界人民银行苏州分行')
driver.find_element(By.CSS_SELECTOR, 'input[name=contact_person]').send_keys('关云长')
driver.find_element(By.CSS_SELECTOR, 'input[name=contact]').send_keys('18343123432')


Select(driver.find_element(By.CSS_SELECTOR, 'select[name=customer]')).select_by_visible_text('工商银行留园支行')
driver.implicitly_wait(3)

# First Time
# driver.find_element(By.CSS_SELECTOR, '#add_contact').click()
# driver.find_element(By.CSS_SELECTOR, 'input[name=customer_contact_person]').send_keys('刘玄德')
# driver.find_element(By.CSS_SELECTOR, 'input[name=customer_contact]').send_keys('13645625879')

# Second Time
Select(driver.find_element(By.CSS_SELECTOR, 'select[name=customer_contact_person]')).select_by_visible_text('李鸣')

r = random.choice([1, 2])
if r == 1:
    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=usage]')).select_by_visible_text('住宅')
else:
    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=usage]')).select_by_visible_text('商业')

Select(driver.find_element(By.CSS_SELECTOR, 'select[name=pgtype]')).select_by_visible_text('房地产')
driver.implicitly_wait(3)
Select(driver.find_element(By.CSS_SELECTOR, 'select[name=codetype]')).select_by_visible_text('苏拓房')



driver.execute_script("let x= document.getElementById('appraise_time');"+"x.value='2022-06-06'")


    
    

# WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[name=appraise_time]')))
# driver.close()

