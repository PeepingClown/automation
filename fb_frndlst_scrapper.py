from selenium import webdriver
import time
from bs4 import BeautifulSoup

browser = webdriver.Chrome("C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe")
browser.get('https://www.facebook.com')

user_id = input("Enter email or phone number: ")
password = input("Enter your password: ")

user = browser.find_element_by_id('email')
user.click()
user.send_keys(user_id)

passwd = browser.find_element_by_id('pass')
passwd.click()
passwd.send_keys(password)

btn = browser.find_element_by_id('u_0_b')
btn.click()

input("Press Enter to continue: ")

prof = browser.find_element_by_xpath('//a[@class="_2s25 _606w"]')
prof.click()

time.sleep(20)
frnds = browser.find_element_by_xpath('//ul[@id="u_fetchstream_1_a"]/li[3]/a')
frnds.click()

while True:
	browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
	time.sleep(0.1)
	browser.execute_script('window.scrollTo(0, 0);')
	time.sleep(0.1)
	try:
		exit_control=browser.find_element_by_xpath("//*[contains(text(), 'More about you')]")
		break
	except:
		continue

ps = browser.page_source
soup = BeautifulSoup(ps, 'html.parser')

flist = soup.find('div', {'class': '_3i9'})
friends = []
for i in flist.findAll('a'):
	friends.append(i.text)

name_list = []
for name in friends:
	if(name == 'FriendFriends'):
		continue
	if('friends' in name):
		continue
	if(name == ''):
		continue
	else:
		name_list.append(name)

print(name_list)


#browser.quit()