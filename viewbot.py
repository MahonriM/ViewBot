from selenium import webdriver
from time import sleep
url="/Users/chumo/Downloads/chromedriver_win32/chromedriver.exe"
url1="https://youtu.be/LklssQttLeI"
url2="https://youtu.be/a6XUPlEbrus"#"https://youtu.be/xvnYwOophpo"
driver1=webdriver.Chrome(executable_path=url)
driver2=webdriver.Chrome(executable_path=url)
driver3=webdriver.Chrome(executable_path=url)
driver4=webdriver.Chrome(executable_path=url)
driver1.get(url2)
driver2.get(url2)
driver3.get(url1)
driver4.get(url1)
while True:
    sleep(30)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()