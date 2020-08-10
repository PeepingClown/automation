from selenium import webdriver
import pandas as pd
import time


browser = webdriver.Chrome("C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe")
browser.get('https://www.worldometers.info/population/countries-in-asia-by-population/')

df=pd.DataFrame(columns=['Country', 'Population'])

for i in browser.find_elements_by_xpath('//*[@id="example2"]/tbody/tr'):
	td_list = i.find_elements_by_tag_name('td')
	row = []
	for td in td_list:
		row.append(td.text)
	t = {}
	for p in range(len(df.columns)):
		t[df.columns[p]] = row[p+1]
	df = df.append(t, ignore_index=True)

print(df)



