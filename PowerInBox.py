# -*- coding: utf-8 -*-
#start BrowserStackLocal ./BrowserStackLocal MDKicy4nya2192zewKpz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'browser': 'Firefox',
 'browser_version': '76.0',
 'os': 'OS X',
 'os_version': 'High Sierra',
 'resolution': '1024x768',
 'name': 'PowerInBox'
}

#browser = webdriver.Remote(
#    command_executor='http://scottmaretick2:MDKicy4nya2192zewKpz@hub.browserstack.com:80/wd/hub',
#    desired_capabilities=desired_cap)

browser = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver")
#browser = webdriver.Firefox()
#browser.maximize_window()
browser.get("https://www.powerinbox.com/")
print(driver.title)
browser.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[1]/a").click() #PLATFORMS DROPDOWN
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/PoweInBox1.png')
browser.navigate().to("https://www.powerinbox.com/monetization/") #MONETIZATION
#browser.find_element_by_xpath("//*[@id="start-now-hero"]").click() #DEMO
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/PoweInBox2.png')
browser.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[3]/a").click() #ADVERTISING
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/PoweInBox3.png')
browser.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[4]/a").click() #RESOURCES DROPDOWN
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/PoweInBox4.png')
browser.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[5]/a").click() #POWERBLOG
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/PoweInBox5.png')
browser.find_element_by_xpath("/html/body/header/nav/div/div[2]/ul/li[6]/a").click() #ABOUT DROPDOWN
browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/PoweInBox6.png')
browser.quit()