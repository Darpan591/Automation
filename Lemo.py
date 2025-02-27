from selenium import webdriver   
import time                                                 #C:\Users\BAPS\.virtualenvs\Lemolite-QXvE2ijl
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)


driver.get("https://lemolite.com/")
time.sleep(5)

for i in range(3):
 driver.execute_script("window.scrollBy(0, 3000);")


#Invalid
time.sleep(2)
driver.find_element("xpath", "//a[text()='Contact Us']").click()
time.sleep(2)   
driver.find_element("xpath", "//input[@placeholder='Your Name']").send_keys(12345)
time.sleep(2)
driver.find_element("xpath", "//input[@placeholder='Your Email']").send_keys('343455@4')
time.sleep(2)
driver.find_element("xpath", "//input[@class='PhoneInputInput']").send_keys(8989834)
time.sleep(2)
driver.find_element("xpath", "//input[@placeholder='Company Name']").send_keys('abcd')
time.sleep(2)
driver.find_element("xpath", "//textarea[@placeholder='Your Message']").send_keys('abcd')
time.sleep(5)
driver.find_element("xpath", "//button[@class='block text-center py-5 w-full bg-[#D8E8C5] text-black rounded-md font-bold']").click()
time.sleep(7)   



#contact form (Valid)
time.sleep(2)   
driver.find_element("xpath", "//input[@placeholder='Your Name']").send_keys('darpan')
time.sleep(2)
driver.find_element("xpath", "//input[@placeholder='Your Email']").send_keys('darpan6t8@gmail.com')
time.sleep(2)
driver.find_element("xpath", "//input[@class='PhoneInputInput']").send_keys(6354385243)
time.sleep(2)
driver.find_element("xpath", "//input[@placeholder='Company Name']").send_keys('abcd')
time.sleep(2)
driver.find_element("xpath", "//textarea[@placeholder='Your Message']").send_keys('abcd')
time.sleep(5)
driver.find_element("xpath", "//button[@class='block text-center py-5 w-full bg-[#D8E8C5] text-black rounded-md font-bold']").click()
time.sleep(5)   
