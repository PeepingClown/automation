from selenium import webdriver
import time
browser = webdriver.Chrome('C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe')
browser.get('https://www.facebook.com')

user_id = input("Enter email id or phone number: ")
password = input("Enter your password: ")

email = browser.find_element_by_id('email')
email.click()
email.send_keys(user_id)

psswd = browser.find_element_by_id('pass')
psswd.click()
psswd.send_keys(password)

browser.find_element_by_id('u_0_b').click()
input("Press Enter to continue...")
browser.get('https://www.facebook.com/notifications')

list_nm = '//*[@id="u_0_t"]/div/ul'
time.sleep(10)
for i in range(5):
	single = browser.find_element_by_xpath(list_nm+'/li['+str(i+1)+']/div/div/a/div/div[2]/div/div/div[2]/div/div/span')
	print(single.text)














