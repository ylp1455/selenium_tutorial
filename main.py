import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Set browser options to keep it open after the process finishes
options = Options()
options.add_experimental_option("detach", True)

# Download and install the appropriate version of ChromeDriver, then start the browser
driver_manager = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_manager), options=options)

# Navigate to a website and maximize the browser window
driver.get("https://www.neuralnine.com")
driver.maximize_window()
time.sleep(10)

# Find all links on the page and click on the first one that contains the text "Books"
links = driver.find_elements_by_xpath("//a[@href]")
for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break

# Find specific links using an XPath expression and print their contents
book_links = driver.find_elements_by_xpath('//div[contains(@class, "elemntor-column-wrap")]//h2[contains(text(), "7 in 1")][count(.//a) = 2]')


book_links[0].click()

driver.switch_to.window(driver.window_handles[1])

time.sleep(10)

buttons = driver.find_element("xpath" , "//a[.//span[text()[contains('Paperback')]]]/span[text()[contains(.,'$']]")

for button in buttons:
    print(button.get_attribute("innerHTML") .replace("&nbsp;" , " ") )






# Close the browser window
# driver.quit()
