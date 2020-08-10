from selenium import webdriver
import pandas as pd
import time
import os

browser = webdriver.Chrome("C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe")
browser.get('https://www.worldometers.info/coronavirus/')
time.sleep(10)

df=pd.DataFrame(columns=['Rank', 'Country', 'Total Cases', 'New Cases', 'Deaths', 'New Deaths', 'Recovered', 'Active cases', 'Critical'])

for i in browser.find_elements_by_xpath("//*[@id='main_table_countries_today']/tbody/tr"):
	td_list=i.find_elements_by_tag_name('td')
	row = []
	for td in td_list:
		row.append(td.text)
	data={}
	for k in range(len(df.columns)):
		data[df.columns[k]]=row[k]
	df = df.append(data, ignore_index=True)

df=df[1:]
path = "C:\\Users\\mayan\\Desktop\\isb code\\covid"
path1 = os.path.join(path, 'Covid.csv')
df.to_csv(path1, index=False)

parint("The data has been stored at "+path1)
browser.quit()

#print(df)
