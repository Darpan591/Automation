from selenium import webdriver   
import time                                                  #C:\Users\BAPS\.virtualenvs\Lemolite-QXvE2ijl
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

driver.get("https://tekydog.com/")
time.sleep(3)

#search product
driver.find_element("xpath", "//input[@id='boost-pfs-search-box-0']").click()
time.sleep(2)  
driver.find_element("xpath", "//input[@class='input-group-field boost-pfs-search-box ui-autocomplete-input'][1]").send_keys("Insyte Retail Rainproof Strobe - Red")
time.sleep(2)
driver.find_element("xpath", "//img[@src='https://cdn.shopify.com/s/files/1/0182/9211/3472/products/0E-STROBERPRsmall-1517392477_200x.jpg?v=1612009690']").click()
time.sleep(3)
driver.find_element("xpath", "//div[@class='inc button']").click()
time.sleep(2)

#ADD TO CART
driver.find_element("xpath", "//input[@name='add']").click()
time.sleep(2)
driver.find_element("xpath", "//button[@class='btn-secondary btn-go-to-cart shadow']").click()
time.sleep(2)
driver.find_element("xpath", "//textarea[@name='note']").send_keys(1234)
time.sleep(2)
driver.find_element("xpath", "//input[@name='checkout']").click()
time.sleep(2)

#ADDRESS
driver.find_element("xpath", "//input[@name='email']").send_keys('darpan6t8@gmail.com')
time.sleep(2)
driver.find_element("xpath", "//input[@name='firstName'][1]").send_keys('Darpan')
time.sleep(2)
driver.find_element("xpath", "//input[@name='lastName'][1]").send_keys('Tandel')
time.sleep(2)
driver.find_element("xpath", "//input[@placeholder='Address']").click()
time.sleep(2)
driver.find_element("xpath", "//input[@placeholder='Address']").send_keys('Valsad')
time.sleep(2)
driver.find_element("xpath", "//mark[@class='_19gi7yt0 _19gi7ytg _19gi7ytf _1fragemnw _19gi7yt19 _19gi7yt1u _19gi7yt1p _1fragemt8'][1]").click()
time.sleep(2)   
driver.find_element("xpath", "//input[@placeholder='Apartment, suite, etc. (optional)']").send_keys("valsad")
time.sleep(2)
driver.find_element("xpath", "//input[@placeholder='PIN code']").send_keys(396001)
time.sleep(2)
driver.find_element("xpath", "//label[@for='save_shipping_information']").click()
time.sleep(2)

#Card details
driver.find_element("xpath", "input-placeholder-color--lvl-22").click()
time.sleep(2)
driver.find_element("xpath", "//input[@type='text' and contains(@placeholder, 'Card')]").send_keys("2432 4232 4324 3233")
time.sleep(2)
driver.find_element("xpath", "//input[@placeholder='Expiration date (MM / YY)']").send_keys(7/27)
time.sleep(2)
driver.find_element("xpath", "//input[contains(@class, 'input-placeholder-color--lvl-22')]").send_keys(123)
time.sleep(2)
driver.find_element("xpath", "//button[@id='checkout-pay-button']").click()
