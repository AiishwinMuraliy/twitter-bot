# File: Twitter Bot
# Author: Aiishwin Muraliy
# Date: Jan 6, 2021
# Decription: This script is able to use selenium and send a tweet in an automated fashion

from selenium import webdriver
import time

username = input("Username: ")
password = input("Password: ")
tweet = input("Tweet: ")

# Launcing the browser
PATH = "/YOUR PATH/" # Setting the path to the chromedriver - Replace the quotes with your path
driver = webdriver.Chrome(PATH)
driver.get('https://twitter.com/i/flow/login') # Opening Twitter
time.sleep(5)

# Entering username and password
username = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
username.send_keys(username)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span/span").click()
time.sleep(2)
password = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input")
password.send_keys(password)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/span/span").click()
time.sleep(3)

# Sending the tweet
tweet_area = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
tweet_area.send_keys(tweet)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()