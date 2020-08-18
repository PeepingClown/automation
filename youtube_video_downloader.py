from selenium import webdriver
import urllib.request

browser = webdriver.Chrome("C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe")
url=input("Enter url: ")
browser.get(url)

video = browser.find_element_by_xpath("//div[@id='movie_player']/div/video")
input("Press ENTER to download")
URL=video.get_attribute("src")
path="C:\\Users\\mayan\\Desktop\\isb code\\youtube_video\\video1.mp4"
urllib.request.urlretrieve(URL[5:], path)