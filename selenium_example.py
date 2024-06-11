from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (ensure chromedriver is in your PATH)
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Ensure the page has loaded
assert "Google" in driver.title

# Find the search box using its name attribute value
search_box = driver.find_element(By.NAME, "q")

# Type a search query
search_box.send_keys("Selenium browser automation")

# Press Enter (or you can use search_box.submit())
search_box.send_keys(Keys.RETURN)

# Wait until the search results are present
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))

# Get search result titles
results = driver.find_elements(By.CSS_SELECTOR, "h3")

# Print the titles
for result in results:
    print(result.text)
