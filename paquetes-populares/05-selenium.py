# el archivo no se tiene que llamar selenium.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()
user_gh = os.getenv("GIT_HUB_USER")
pass_gh = os.getenv("GIT_HUB_PASS")

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=options)

browser = webdriver.Chrome()

browser.implicitly_wait(10)
browser.get("https://github.com")

link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()


user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

user_input.send_keys(user_gh)
pass_input.send_keys(pass_gh)
pass_input.send_keys(Keys.RETURN)


link_avatar = browser.find_element(By.CLASS_NAME, "avatar.circle")
link_avatar.click()

profile = browser.find_element(By.CLASS_NAME,
                               "Truncate__StyledTruncate-sc-23o1d2-0.cBdrp")
label_profile = profile.get_attribute("innerHTML")
print(label_profile)

assert "jab66" in label_profile

browser.quit()
