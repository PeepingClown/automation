from selenium import webdriver

browser = webdriver.Chrome('C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe')

browser.get('https://www.linkedin.com')

user_id = input('Enter user id:')
password = input('Enter Password:')

email = browser.find_element_by_id('session_key')
email.click()
email.send_keys(user_id)

psswd = browser.find_element_by_id('session_password')
psswd.click()
psswd.send_keys(password)

btn = browser.find_element_by_class_name('sign-in-form__submit-button')

#input('Press Enter to Login')
btn.click()


try:
	XPATH = '//*[@id = "notifications-nav-item"]/a/span/span[1]'

	noti_num = browser.find_element_by_xpath(XPATH).get_attribute('textContent')

	print('Number of notifications are: '+noti_num)

except:
	print('No new notifications available')

browser.quit()