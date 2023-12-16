import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome()
from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
driver = webdriver.Firefox(options=options)

driver.get("https://automation.credence.in/login")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
# Click Login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()


# Click on Product--Macbook
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div/div/a[2]/h3").click()
# Click on add to cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
# Click on Continue Shopping
driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
# Click on Product--Headphone
driver.find_element(By.XPATH, "//h3[normalize-space()='Headphones']").click()
# Click on add to cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
# Click on Continue Shopping
driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
# Click on Product--Ipad
driver.find_element(By.XPATH, "//h3[normalize-space()='Apple iPad Retina']").click()
# Click on add to cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
# Select Quality dropdown value for product 1
product_quantity1 = Select(driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select"))
product_quantity1.select_by_index(3)
# Select Quality dropdown value for product 2
product_quantity2 = Select(driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select"))
product_quantity2.select_by_index(3)
# Select Quality dropdown value for product 3
product_quantity3 = Select(driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select"))
product_quantity3.select_by_index(2)

l = len(driver.find_elements(By.XPATH, "//tbody/tr/td[4]"))
# l=6

Product_Price_List =[]
for r in range(1, l-2):
    var1 = driver.find_element(By.XPATH, "//tbody/tr["+str(r) + "]/td[4]").text
    product_price = (var1[1:])
    Product_Price_List.append(float(product_price))

Exp_Subtotal = round((sum(Product_Price_List)), 2)
# Exp_Subtotal-->11999.889999999998
# Exp_Subtotal-->11999.89
print("Exp_Subtotal-->" + str(Exp_Subtotal))

print(Product_Price_List)


System_Value = []

for r in range(l-2, l+1):
    var2 = driver.find_element(By.XPATH, "//tbody/tr["+str(r) + "]/td[4]").text
    system_price = (var2[1:])
    System_Value.append(system_price)

print(System_Value)


# Open browser
# Url
# Login
# add product in cart
# verify the amount

time.sleep(10)