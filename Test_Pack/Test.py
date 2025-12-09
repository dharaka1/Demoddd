import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.save_screenshot("Main_page.png")
search_Product=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Search for Products, Brands and More"]')))
search_Product.send_keys("Latest model Vivo Mobile Phones",Keys.ENTER)
driver.save_screenshot("search_Product.png")
Scroll_Into_Product=wait.until(EC.visibility_of_element_located((By.XPATH,'//div[text()="vivo T4 5G (Phantom Grey, 128 GB)"]')))
driver.execute_script("arguments[0].scrollIntoView()",Scroll_Into_Product)
driver.save_screenshot("Scroll_Into_Product.png")


Click_Into_Product=wait.until(EC.visibility_of_element_located((By.XPATH,'//div[text()="vivo T4 Pro 5G (Blaze Gold, 256 GB)"]')))
Click_Into_Product.click()
driver.save_screenshot("Click_Into_Product.png")

Original_Window=driver.window_handles
driver.switch_to.window(Original_Window[1])

Scroll_Into_Cart=wait.until(EC.visibility_of_element_located((By.XPATH,'//div[text()="Questions and Answers"]')))
driver.execute_script("arguments[0].scrollIntoView()",Scroll_Into_Cart)
driver.save_screenshot("Scroll_Into_Cart.png")

Click_Into_Cart=wait.until(EC.visibility_of_element_located((By.XPATH,'//button[text()="Add to cart"]')))
Click_Into_Cart.click()
driver.save_screenshot("Click_Into_Cart.png")
time.sleep(15)

driver.quit()

