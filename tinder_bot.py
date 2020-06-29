from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self, chromedriver_path, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        self.driver.implicitly_wait(15)

    def login(self):
        self.driver.get('https://tinder.com')

        i_accept_btn = self.driver.find_element_by_xpath('//button/span[text()=\'I Accept\']')
        i_accept_btn.click()
        
        sleep(4)
        fb_btn = self.driver.find_element_by_xpath('//span[text()=\'Log in with Facebook\']')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(self.username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(self.password)

        login_btn = self.driver.find_element_by_xpath('//input[@value=\'Log In\']')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        popup_1 = self.driver.find_element_by_xpath('//span[text()=\'Allow\']')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//span[text()=\'Enable\']')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//button[@aria-label=\'Like\']')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//button[@aria-label=\'Nope\']')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(2)
            try:
                self.like()
            except Exception:
                try:
                    self.close_all_likes_exhausted_popup()
                except Exception:
                    try:
                        self.close_add_interest_popup()
                    except Exception:
                        self.close_match()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def close_all_likes_exhausted_popup(self):
        no_thanks_btn = self.driver.find_element_by_xpath('//span[text()=\'No Thanks\']')
        no_thanks_btn.click()

    def close_add_interest_popup(self):
        not_interested_lnk = self.driver.find_element_by_xpath('//span[text()=\'Not interested\']')
        not_interested_lnk.click()