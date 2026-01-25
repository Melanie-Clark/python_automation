from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "https://www.javascripttutorial.net/sample/webapis/drag-n-drop-basics/"

# instantiate webdriver and open a chrome browser 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load the webpage 
driver.get(url)

# find source - yellow square
square = driver.find_element(By.XPATH, '//*[@id="item"]')

# find destination - middle box
middle_box = driver.find_element(By.XPATH, '/html/body/div/div/div[2]')

# find destination - right box
right_box = driver.find_element(By.XPATH, '/html/body/div/div/div[3]')

# find destination - left box
left_box = driver.find_element(By.XPATH, '/html/body/div/div/div[1]')

# ActionsChains is used for drag and drop
actions = ActionChains(driver)

# perform drag and drop - drag square into middle_box
actions.drag_and_drop(square, middle_box).perform()

# perform drag and drop - drag square into right_box
actions.drag_and_drop(square, right_box).perform()

# perform drag and drop - drag square into left_box
actions.drag_and_drop(square, left_box).perform()

actions.drag_and_drop(square, right_box).perform()

actions.drag_and_drop(square, middle_box).perform()

# paused to view the results
sleep(10)

# close the driver
driver.quit()
