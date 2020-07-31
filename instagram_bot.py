from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        # login_button = driver.find_element_by_xpath("//a[@href'/accounts/login/']")
        # login_button.click()
        # time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(2)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # searching for pic link
        hrefs = driver.find_element_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in href ]
        print(hashtag + " photos: "+str(len(pic_hrefs)))



myIg = InstagramBot('hisnameispum', '4d88152f')
myIg.login()
myIg.like_photo("thaifood")