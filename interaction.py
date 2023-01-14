from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/momo/Development/chromedriver"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options,
                          service=Service(executable_path=chrome_driver_path))

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# all_portals= driver.find_element(By.LINK_TEXT,"Current events")
# all_portals.click()

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("python")
search_bar.send_keys(Keys.ENTER)

# driver.close()