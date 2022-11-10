from twitter_scraper_selenium import scrap_keyword
#scrap 10 posts by searching keyword "india" from date 30th August till date 31st August
cancer = scrap_keyword(keyword="smoking cancer chemotherapy", browser="chrome",
                      tweets_count=1,output_format="json" ,until="2023-08-31", since="2021-08-30")
print(cancer)


from twitter_scraper_selenium import scrape_profile

microsoft = scrape_profile(twitter_username="AspRobin22",output_format="json",browser="firefox",tweets_count=10)
print(microsoft)

# import tweepy #Library required for Twitter API
# import csv, re
# import pandas as pd
# import os
# import wget
# import logging
#
# # api_key = "1nYngvVObOhkHQDkvHPSMVYQE"
# # api_key_secret = "nmYJ8FFyZEVTeqkoKCrUsvUXbo1VH2vpOhxsDSayVrRaEvbOix"
# #
# # access_token = "772342298919043076-tq4KgRa6ffrkzefG4m1CTiwC0sXXb7i"
# # access_token_secret = "vD0I9OPxw8HOzgEpUrOqWKWYbmojyZf9QowVX7TMZ9hLd"
#
# consumer_key = "1nYngvVObOhkHQDkvHPSMVYQE"
# consumer_secret = "nmYJ8FFyZEVTeqkoKCrUsvUXbo1VH2vpOhxsDSayVrRaEvbOix"
# access_key = "772342298919043076-tq4KgRa6ffrkzefG4m1CTiwC0sXXb7i"
# access_secret = "vD0I9OPxw8HOzgEpUrOqWKWYbmojyZf9QowVX7TMZ9hLd"
#
# #Creating an empty dataframe to store the information
# tweets =pd.DataFrame(columns=["id","created_at","text","media_url","location"])
#
# tweets.columns
#
# import datetime, time
# last_week = datetime.date.today() - datetime.timedelta(9)
# since_tweets = datetime.datetime.strptime(time.strftime("%Y-%m-%d"), "%Y-%m-%d")
# print (since_tweets)
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key, access_secret)
# api = tweepy.API(auth,wait_on_rate_limit=True)
#
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")
#
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")
