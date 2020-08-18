from selenium import webdriver
import time
import pandas as pd

browser = webdriver.Chrome("C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe")
browser.get('https://twitter.com/explore/tabs/trending')
time.sleep(10)
sp=browser.find_elements_by_tag_name('span')
hashTag=[]

for i in sp:
	if i.text != "" and i.text[0] == "#" and i.text not in hashTag:
		hashTag.append(i.text)
	else:
		continue
urls=[]
for i in hashTag:
	url='https://twitter.com/search?q=%23'+i[1:]+'&src=trend_click'
	urls.append(url)

dic={'#Tag':hashTag, 'URL':urls}
data=pd.DataFrame(dic)
path="C:\\Users\\mayan\\Desktop\\isb code\\data visualization\\Twitter_Trending_Hashtag.csv"
data.to_csv(path, index=False)


print("Data is stored at => "+path)

