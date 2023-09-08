from bot import InternetSpeedTwitterBot


PROMISED_DOWN = 150
PROMISED_UP = 10

CHROME_DRIVER_PATH = '/Users/mona/PycharmProjects/chromedriver'

TWITTER_USER = 'blahblahbl34231'
TWITTER_PW = 'pnx_xaf2yar1vqz4RCM'

speed_bot = InternetSpeedTwitterBot()
speed_bot.get_internet_speed()
speed_bot.tweet_at_provider(user=TWITTER_USER, pw=TWITTER_PW, down=PROMISED_DOWN, up=PROMISED_UP)