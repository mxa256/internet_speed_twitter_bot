import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(4)
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        time.sleep(50)
        back_to_test = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        back_to_test.click()
        time.sleep(1)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text


    def tweet_at_provider(self, user, pw, down, up):
        self.driver.get('https://twitter.com')
        time.sleep(3)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div')
        log_in.click()
        time.sleep(3)
        user_name_entry = self.driver.find_element(By.NAME, 'text')
        user_name_entry.send_keys(user)
        user_name_entry.send_keys(Keys.ENTER)
        time.sleep(3)
        pw_entry = self.driver.find_element(By.NAME, 'password')
        pw_entry.send_keys(pw)
        pw_entry.send_keys(Keys.ENTER)
        time.sleep(3)
        try:
            security_pop = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div')
            security_pop.click()
        except NoSuchElementException:
            pass
        tweet_entry = self.driver.find_element(By.CSS_SELECTOR, 'div[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')

        if float(self.down) < float(down) or float(self.up) < float(up):
            print("Internet speed is bad. Tweeting.")
            message = f"Hey internet provider, why is my internet speed {self.down}down/{self.up}up when I pay for {down}down/{up}up?"
            tweet_entry.send_keys(message)
            time.sleep(2)
            tweet_entry.send_keys(Keys.TAB+Keys.TAB+Keys.TAB+Keys.TAB+Keys.TAB+Keys.TAB+Keys.TAB+Keys.TAB+Keys.ENTER)
        else:
            print("Internet speed is good! No need to tweet.")


