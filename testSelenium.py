from selenium import webdriver
path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(executable_path=path)
browser.get('http://www.baidu.com/')
browser.close()