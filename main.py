from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#this two linesof code will keep open the browser after the prosess happend
options = Options()
options.add_experimental_option( "detach" , True)

driver_manager = ChromeDriverManager()
driver = webdriver.Chrome(service=Service(driver_manager.install()), options=options)




driver.get("https://www.neuralnine.com")
driver.maximize_window()

links = driver.find_element("xpath", "//a[@href]")


for link in links:
    print (link.get_attribute("innerHTML"))
