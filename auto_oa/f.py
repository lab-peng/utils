from faker import Faker
from config import url 

import random 
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


fake = Faker(['zh_CN'])





# The below two lines fixed USB error logging
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
# capabilities = options.to_capabilities()
# capabilities['acceptInsecureCerts'] = True

# PATH = 'C:\Program Files (x86)\chromedriver.exe'
PATH = './chromedriver.exe'
# driver = webdriver.Chrome(PATH, options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

pg_url = url + '?next=/pg/pg_list/'
driver.get(pg_url)
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
login = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')

username.send_keys("user63")
password.send_keys("pass63")
login.click()



def create_pg():
    client = fake.company()
    contact_person = fake.name()
    contact = fake.phone_number()
    address = fake.street_name() + str(random.randint(1, 100)) + '号'
    obligee = fake.name()
    land_area = random.randint(20,200)
    house_area = random.randint(20, 200)

    estate = fake.company_prefix() + random.choices(['花园', '花苑', '家园', '一区', ''])[0]
    department = random.randint(1, 30)


    create_button = driver.find_element(By.CSS_SELECTOR, '#card_add')
    create_button.click()

    driver.find_element(By.CSS_SELECTOR, 'input[name=client]').send_keys(client)
    driver.find_element(By.CSS_SELECTOR, 'input[name=contact_person]').send_keys(contact_person)
    driver.find_element(By.CSS_SELECTOR, 'input[name=contact]').send_keys(contact)


    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=customer]')).select_by_visible_text('工商银行留园支行')
    driver.implicitly_wait(3)

    # First Time
    # driver.find_element(By.CSS_SELECTOR, '#add_contact').click()
    # driver.find_element(By.CSS_SELECTOR, 'input[name=customer_contact_person]').send_keys('刘玄德')
    # driver.find_element(By.CSS_SELECTOR, 'input[name=customer_contact]').send_keys('13645625879')

    # Second Time
    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=customer_contact_person]')).select_by_visible_text('刘玄德')

    # r = random.choice([1, 2])
    # if r == 1:
    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=usage]')).select_by_visible_text('住宅')
    # else:
    #     Select(driver.find_element(By.CSS_SELECTOR, 'select[name=usage]')).select_by_visible_text('商业')

    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=pgtype]')).select_by_visible_text('房地产')
    driver.implicitly_wait(3)
    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=codetype]')).select_by_visible_text('苏拓房')

    driver.find_element(By.CSS_SELECTOR, 'input[name=address]').send_keys(address)
    driver.find_element(By.CSS_SELECTOR, 'input[name=obligee]').send_keys(obligee)
    driver.execute_script("let x= document.getElementById('appraise_time');"+"x.value='2022-06-06'")
    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=pgpurpose]')).select_by_visible_text('抵押')

    driver.find_element(By.CSS_SELECTOR, 'input[name=land_area]').send_keys(land_area)
    driver.find_element(By.CSS_SELECTOR, 'input[name=house_area]').send_keys(house_area)
        
    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=appraiser1]')).select_by_visible_text('吴华')   
    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=appraiser2]')).select_by_visible_text('应丽平') 
    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=method1]')).select_by_visible_text('收益法')   
    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=method2]')).select_by_visible_text('成本法')

    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=area]')).select_by_visible_text('吴中区')  
    driver.implicitly_wait(3) 
    Select(driver.find_element(By.CSS_SELECTOR, 'select[name=street]')).select_by_visible_text('长桥街道') 

    driver.implicitly_wait(5)
    add_estate_button = driver.find_element(By.CSS_SELECTOR, '#estate_department > div:nth-child(1) > div > div > a')
    driver.execute_script("arguments[0].click();", add_estate_button) 
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, 'input[name=estate_name]').send_keys(estate)
    driver.implicitly_wait(3)
    driver.find_element(By.CSS_SELECTOR, '#pageWrapper > div.page-body-wrapper.null > div.page-body > form > div > div.card_btn > button').click()

    driver.implicitly_wait(3)
    add_department_button = driver.find_element(By.CSS_SELECTOR, '#estate_department > div:nth-child(2) > div > div > a')
    driver.execute_script("arguments[0].click();", add_department_button) 
    driver.implicitly_wait(3)
    driver.find_element(By.CSS_SELECTOR, 'input[name=department_number]').send_keys(department)
    driver.implicitly_wait(3)
    driver.find_element(By.CSS_SELECTOR, '#pageWrapper > div.page-body-wrapper.null > div.page-body > form > div > div.card_btn > button').click()
    driver.implicitly_wait(3)

    # driver.implicitly_wait(3)
    # Select(driver.find_element(By.CSS_SELECTOR, 'select[name=estate]')).select_by_visible_text('怡邻')   
    # driver.implicitly_wait(3)
    # Select(driver.find_element(By.CSS_SELECTOR, 'select[name=department]')).select_by_visible_text('93')

    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    # submit_button.click()
    driver.execute_script("arguments[0].click();", submit_button)
    print('create pg success')
    time.sleep(5)
    # webdriver.ActionChains(driver).move_to_element(submit_button).click(submit_button).perform()

# WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[name=appraise_time]')))
# driver.close()


for _ in range(10):
    create_pg()






