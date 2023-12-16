import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
Url = 'https://automation.credence.in/shop'
# driver.implicitly_wait(10)
driver.get(Url)
driver.maximize_window()
driver.find_element(By.LINK_TEXT, 'Login').click()
driver.find_element(By.ID, 'email').send_keys('Credencetest@test.com')
driver.find_element(By.ID, 'password').send_keys('Credence@123')
driver.find_element(By.CSS_SELECTOR, 'body > div > div > div > div > div.panel-body > form > div:nth-child(5) > div > button').click()
time.sleep(10)

driver.find_element(By.XPATH, '/html/body/div/div[2]/div[3]/div/div/a[2]/h3').click()
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/form[1]/input[5]').click()
driver.find_element(By.LINK_TEXT, 'Continue Shopping').click()
driver.find_element(By.XPATH, '/html/body/div/div[2]/div[4]/div/div/a[2]/h3').click()
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/form[1]/input[5]').click()
driver.find_element(By.LINK_TEXT, 'Continue Shopping').click()
driver.find_element(By.XPATH, '/html/body/div/div[3]/div[3]/div/div/a[2]/h3').click()
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/form[1]/input[5]').click()
time.sleep(5)
Select_lap = Select(driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[1]/td[3]/select"))
Select_lap.select_by_index(2)
driver.implicitly_wait(10)
Select_Tab = Select(driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[2]/td[3]/select"))
Select_Tab.select_by_index(2)
Select_Tab = Select(driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[3]/td[3]/select"))
Select_Tab.select_by_index(2)
time.sleep(5)
# driver.find_element(By.LINK_TEXT, 'Proceed to Checkout').click()
l = len(driver.find_elements(By.XPATH, '/html/body/div/table/tbody/tr/td[4]'))
print(l)
product_price_list = []
for r in range(1, l-2):
    time.sleep(5)
    val1 = driver.find_element(By.XPATH, '/html/body/div/table/tbody/tr['+str(r)+']/td[4]').text
    price = float(val1[1:])
    product_price_list.append(price)



print(sum(product_price_list))


