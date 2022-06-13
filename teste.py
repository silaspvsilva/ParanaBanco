
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()


driver.get('https://the-internet.herokuapp.com/challenging_dom')
time.sleep(5)

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[1]/td[7]/a[1]').click()
time.sleep(2)

#clique Botão azul
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/a[1]').click()
time.sleep(2)


#clique Botão vermelho
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/a[2]').click()
time.sleep(2)


#clique Botão verde
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/a[3]').click()
time.sleep(5)

#Iuvaret0
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[1]/td[7]/a[1]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[1]/td[7]/a[2]').click()
time.sleep(2)

#Iuvaret1
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[2]/td[7]/a[1]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[2]/td[7]/a[2]').click()
time.sleep(2)

#Iuvaret2
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[3]/td[7]/a[1]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[3]/td[7]/a[2]').click()
time.sleep(2)

#Iuvaret3
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[4]/td[7]/a[1]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[4]/td[7]/a[2]').click()
time.sleep(2)

#Iuvaret4
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[5]/td[7]/a[1]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[5]/td[7]/a[2]').click()
time.sleep(2)

#Iuvaret5
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[6]/td[7]/a[1]').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[6]/td[7]/a[2]').click()
time.sleep(2)

#Iuvaret6
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[7]/td[7]/a[1]').click()
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[7]/td[7]/a[2]').click()
time.sleep(2)

#Iuvaret7
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[8]/td[7]/a[1]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[8]/td[7]/a[2]').click()
time.sleep(2)

#Iuvaret8
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[9]/td[7]/a[1]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[9]/td[7]/a[2]').click()
time.sleep(2)

#Iuvaret9
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[10]/td[7]/a[1]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[10]/td[7]/a[2]').click()
time.sleep(2)





