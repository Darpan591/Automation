from selenium import webdriver   
import time                                                 #C:\Users\BAPS\.virtualenvs\Lemolite-QXvE2ijl
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

driver.get("https://www.instagram.com/accounts/login/?hl=en")
time.sleep(2)

driver.find_element("xpath", "//span[@style='----base-line-clamp-line-height: 18px; --lineHeight: 18px;'][1]").click()
time.sleep(2)
driver.find_element("xpath", "//input[@placeholder='Email, Phone, or Username']").send_keys('tandeldarpan3091@gmail.com')
time.sleep(2)
driver.find_element("xpath", "//div[@role='button']").click()