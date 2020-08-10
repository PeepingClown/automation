from selenium import webdriver

browser = webdriver.Chrome('C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe')
browser.get('https://www.facebook.com')

user_id = input('Input your email or phone number:')
password = input('Input your password:')

email = browser.find_element_by_id('email')
email.click()
email.send_keys(user_id)

psswd = browser.find_element_by_id('pass')
psswd.click()
psswd.send_keys(password)

btn = browser.find_element_by_id('u_0_b')

input('Press ENTER to login')
btn.click()

# time.sleep(20)

k ='//*[@id = "home_birthdays"]/div/div/div/div/a/div/div/span/span[2]'
n = browser.find_element_by_xpath(k).get_attribute('textContent')

num = n[0]
num = int(num)
print(num)

message = "Happy Birthday !!"
browser.get('https://www.facebook.com/events/birthdays/')

bday_list = browser.find_elements_by_xpath("//*[@class='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")


c=0
for element in bday_list:
	element_id = str(element.get_attribute('id'))
	XPATH = '//*[@id = "' + element_id + '"]'
	post = browser.find_element_by_xpath(XPATH)
	post.send_keys(message)
    # post.send_keys(keys.ENTER)
	c=c+1
    if(c>num):
    	break


browser.quit()

