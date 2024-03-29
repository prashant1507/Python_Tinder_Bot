from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random

class TinderBot:
    def __init__(self, chromedriver_path, username, password):
        self.username = username
        self.password = password
        self.right_counter = 0
        self.left_counter = 0
        self.counter = 0
        self.chromedriver_path = chromedriver_path

    def clean_up(self):
        self.driver = webdriver.Chrome(executable_path=self.chromedriver_path)
        self.driver.implicitly_wait(15)
        self.driver.delete_all_cookies()

    def launch_url(self):
        self.driver.get('https://tinder.com')
        self.driver.maximize_window()

    def login(self):
        
        i_accept_btn = self.driver.find_element_by_xpath('//button/span[text()=\'I Accept\']')
        i_accept_btn.click()
        
        sleep(4)
        login_btn = self.driver.find_element_by_xpath('//button/span[text()=\'Log in\']')
        login_btn.click()

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
        like_btn = self.driver.find_element_by_xpath('//button//span[text()=\'Like\']/..')
        like_btn.click()
        self.right_counter = self.right_counter + 1
        self.counter = self.counter + 1
        print ("Right Swipe: "+str(self.right_counter))\
        # Dislike after 5 likes
        if self.counter > 5:
            self.dislike()
            self.counter = 0

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//button//span[text()=\'Nope\']/..')
        dislike_btn.click()
        self.left_counter = self.left_counter + 1
        print ("Left Swipe: "+str(self.left_counter))

    def auto_swipe(self):
        while True:
            sleep(random.randint(2, 6))
            try:
                self.like()
            except Exception:
                try:
                    self.close_add_to_home_screen_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        try:
                            self.close_all_likes_exhausted_popup()
                        except Exception:
                            try:
                                self.send_super_like_popup()
                            except Exception:
                                    self.driver.refresh()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def close_all_likes_exhausted_popup(self):
        no_thanks_btn = self.driver.find_element_by_xpath('//span[text()=\'No Thanks\']')
        no_thanks_btn.click()

    def close_add_to_home_screen_popup(self):
        not_interested_lnk = self.driver.find_element_by_xpath('//span[text()=\'Not interested\']')
        not_interested_lnk.click()

    def unmatch_first_match(self):
        unmatch_tab = self.driver.find_element_by_xpath('//button[text()=\'Messages\']')
        unmatch_tab.click()

        first_msg_tab = self.driver.find_element_by_xpath('//div[@class=\'messageList\']/a[1]')
        first_msg_tab.click()

        unmatch_btn = self.driver.find_element_by_xpath('//button[text()=\'Unmatch\']')
        unmatch_btn.click()

        no_reason_option = self.driver.find_element_by_xpath('//div[text()=\'No Reason\']')
        no_reason_option.click()

        unmatch_confirm_btn = self.driver.find_element_by_xpath('//button/span[text()=\'Unmatch\']')
        unmatch_confirm_btn.click()
       
    def send_super_like_popup(self):
        no_thanks_btn = self.driver.find_element_by_xpath('//button/span[text()=\'No Thanks\']')
        no_thanks_btn.click()

    def close_email_verification_popup(self):
        print()
