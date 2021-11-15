from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
webdriver.F
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
# prefs = {"profile.default_content_settings.popups": 0,
#          "download.default_directory": r"C:\Users\10678727\Index Data",
#          "directory_upgrade": True}
# options.add_experimental_opion("prefs", prefs)
# chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Firefox(r'C:\Users\10678727\Downloads\chromedriver_win32\chromedriver.exe', options=options)
driver.get('https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx')
driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td/ul/li[2]/a').click()
print(driver.title)
time.sleep(5)
driver.quit()