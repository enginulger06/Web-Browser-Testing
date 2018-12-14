import os
from selenium import webdriver





source = "http://softruck.net"

#driver = webdriver.Chrome()
#driver = webdriver.Edge()
#driver = webdriver.Firefox()


#driver = webdriver.Opera()
'''
#opera
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Users\\Engin\\AppData\\Local\\Programs\\Opera\\57.0.3098.76\\opera.exe"
driver = webdriver.Opera(options=options)
'''




driver.get(source)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart


print ("Back End: %s" % float((backendPerformance)/float(1000))) #sonuc milisaniye olarak çıkıyor 1 saniye 1000 milisaniye
print ("Front End: %s" % float((frontendPerformance)/float(1000)))

driver.quit()

