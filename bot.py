from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time, os, wget


driver_path = 'Insert your chromedriver path here'
username = "Insert your Instagram username here"
password = "Insert your Instagram password here"
keyword = "Insert your tag keyword here"
url = 'https://www.instagram.com/'

driver = webdriver.Chrome(driver_path)
driver.get(url)

username_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username_box.clear()
username_box.send_keys(username)
password_box.clear()
password_box.send_keys(password)

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

searchbox.send_keys('#' + keyword)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)

driver.execute_script("window.scrollTo(0,4000);")

images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]

print('Number of scraped images: ', len(images))

path = os.getcwd()
path = os.path.join(path, keyword + "s")
os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, keyword + str(counter+1) + '.jpg')
    wget.download(image, save_as)
    counter += 1

print('Done')
driver.close()
