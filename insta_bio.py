from selenium import webdriver

browser = webdriver.Chrome("C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe")
user_h = input("Enter user handle: ")

browser.get("https://www.instagram.com/"+user_h)

bio = browser.find_element_by_xpath('//div[@class="-vDIg"]/span').text
#print(bio)

path = "C:\\Users\\mayan\\Desktop\\isb code\\insta\\bio\\"+user_h+".txt"
with open(path, 'w') as f:
	f.write(bio)

browser.quit()