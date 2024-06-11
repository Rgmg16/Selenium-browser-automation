from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (ensure chromedriver is in your PATH)
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")
    assert "Google" in driver.title

    # Find the search box
    search_box = driver.find_element(By.NAME, "q")
    
    # Enter search query
    search_box.send_keys("Selenium browser automation")
    
    # Press Enter
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the search results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
    
    # Extract search result titles
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    
    # Print the titles
    for result in results:
        print(result.text)

finally:
    # Close the browser
    driver.quit()
