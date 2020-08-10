from selenium import webdriver

browser = webdriver.Chrome('C:\\Users\\mayan\\Desktop\\isb code\\web driver\\chromedriver.exe')
browser.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&n')

number = int(input('Enter your number: '))
cnt= int(input('Enter times: '))

fld = browser.find_element_by_id('ap_email')
fld.click()
fld.send_keys(number)

btn = browser.find_element_by_id('continue')
btn.click()



btn1 = browser.find_element_by_id('continue')
btn1.click()


for i in range(cnt-1):
	XPATH = '//*[@id="cvf-page-content"]/div/div/div/form/div[5]/a'
	send = browser.find_element_by_xpath(XPATH)
	#find_element_by_link_text
	send.click()


browser.quit()
