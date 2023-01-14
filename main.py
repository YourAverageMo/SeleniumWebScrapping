from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/momo/Development/chromedriver"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options,
                          service=Service(executable_path=chrome_driver_path))
# driver.get(
#     "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_1_sspa?crid=321TQAIK15I47&keywords=instant%2Bpot%2Bduo%2Bplus&qid=1673655743&sprefix=instant%2Bpot%2Bduo%2Bplus%2Caps%2C212&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFTSDIwOEhQUkNEV1YmZW5jcnlwdGVkSWQ9QTAwMDQ2OTUyT0JBTTZCUkZUTTVKJmVuY3J5cHRlZEFkSWQ9QTA2ODUxMTMxNEFQMlI1TENVNkhBJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"
# )
# price = driver.find_element(By.CLASS_NAME, "a-offscreen").get_attribute("textContent")
# print(price)

# use '.' to find something inside a css_selector like below
# driver.get("https://www.python.org/")
# test = driver.find_element(By.CSS_SELECTOR, ".small-widget.documentation-widget a")

driver.get("https://www.python.org/")
times = driver.find_elements(By.CSS_SELECTOR, ".event-widget.last time")
names = driver.find_elements(By.CSS_SELECTOR, ".event-widget.last li a")
events = {}

for time in times:
    index = times.index(time)
    name = names[index]
    events[index] = {"time": time.text, "name": name.text}

print(events)

driver.close()