from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = "https://the-internet.herokuapp.com/dynamic_controls"

# instantiate webdriver and open a chrome browser 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load the webpage 
driver.get(url)

# waits up to 10 seconds for specified conditions to be met
wait = WebDriverWait(driver, 10)

# find the Enable button
enable_button = driver.find_element(By.XPATH, '//*[@id="input-example"]/button')
# click the Enable button
enable_button.click()

sleep(3)

# find the disable button
disable_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/button')))
# click the Disable button
disable_button.click()

# view result
sleep(3)

# find the Remove button
remove_button = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
# click the Remove button
remove_button.click()

sleep(3)

# find the Add button
add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox-example"]/button')))
# click the Add button
add_button.click()

sleep(3)

# find the checkbox 
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox"]')))
checkbox.click()

sleep(3)

# close the browser and quit the webdriver
driver.quit()
