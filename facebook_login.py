from selenium import webdriver

browser = webdriver.Chrome('C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe')
browser.get('https://www.facebook.com')

user_id = input('Enter email id or phone number:')
password = input('Enter the password:')

email = browser.find_element_by_id('email')
email.click()
email.send_keys(user_id)

psswd = browser.find_element_by_id('pass')
psswd.click()
psswd.send_keys(password)

btn = browser.find_element_by_id('u_0_b')

input('Press Enter')

btn.click()



