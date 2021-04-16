# Scrapy settings for splash_based_project project

BOT_NAME = 'splash_based_project'

SPIDER_MODULES = ['splash_based_project.spiders']
NEWSPIDER_MODULE = 'splash_based_project.spiders'



SPLASH_URL = 'http://127.0.0.1:8050'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
COOKIES_ENABLED = True 
SPLASH_COOKIES_DEBUG = False
SPIDER_MIDDLEWARES = {    
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    'splash_based_project.middlewares.SplashBasedProjectSpiderMiddleware': 543,
}
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
}

USER_AGENTS = [("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
               "Chrome/83.0.4103.116 Safari/537.36"),  # chrome
               ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",  # firefox
               "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko"),  # internet explorer
               ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
               "Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61")]  # microsoft edge