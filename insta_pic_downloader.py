from selenium import webdriver
import urllib.request

browser = webdriver.Chrome("C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe")

user = input("Enter User handle: ")

browser.get("https://www.instagram.com/"+user)

try:
	image1 = browser.find_element_by_class_name('_6q-tv')
except:
	image1 = browser.find_element_by_class_name('be6sr')

img_link = image1.get_attribute('src')
path = "C:\\Users\\mayan\\Desktop\\isb code\\insta\\"+user+".jpg"

urllib.request.urlretrieve(img_link, path)



print("The profile pic has been downloaded")
browser.quit()