from selenium import webdriver
from selenium.webdriver.common.by import By
import re,urllib.request

browser = webdriver.Chrome()

browser.get("http://www.baidu.com")
browser.close();