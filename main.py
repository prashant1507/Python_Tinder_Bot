from tinder_bot import TinderBot

if __name__ == '__main__':
    bot = TinderBot('./chromedriver', 'username', 'password')
    bot.clean_up()
    bot.launch_url()
    bot.login()
    bot.auto_swipe()
