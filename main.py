from bot import InternetSpeedTwitterBot


PROMISED_DOWN = 'YOUR PROMISED INTERNET DOWNLOAD SPEED'
PROMISED_UP = 'YOUR PROMISED INTERNET UPLOAD SPEED'

CHROME_DRIVER_PATH = '/Users/mona/PycharmProjects/chromedriver'

TWITTER_USER = 'YOUR TWITTER NAME'
TWITTER_PW = 'YOUR TWITTER PASSWORD'

speed_bot = InternetSpeedTwitterBot()
speed_bot.get_internet_speed()
speed_bot.tweet_at_provider(user=TWITTER_USER, pw=TWITTER_PW, down=PROMISED_DOWN, up=PROMISED_UP)
