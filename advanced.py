from selenium import webdriver

driver = webdriver.Chrome()

# Taking screenshots
driver.save_screenshot("screenshot.png")

# Handling javascript alerts
alert = driver.switch_to.alert
alert.accept()  # To accept the alert
alert.dismiss()  # To dismiss the alert

# To switch to a frame
driver.switch_to.frame("frame_name_or_id")

# To switch back to the main content
driver.switch_to.default_content()
