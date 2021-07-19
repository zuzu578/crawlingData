from selenium import webdriver
import datetime
driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(50)
driver.get('http://www.foodsafetykorea.go.kr/portal/specialinfo/foodTruckList.do?menu_grp=MENU_NEW04&menu_no=2986&menu_no=2986&menu_grp=MENU_NEW04')
driver.implicitly_wait(50)
table = driver.find_element_by_id('board')
print(table.text)
#print(table.text)