import requests
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from sys import argv
from os import mkdir

# url = argv[1]

options = ChromeOptions()
options.headless = True

while True:
	try:
		driver = Chrome(executable_path='/home/aaron/Downloads/chromedriver', options=options)
		driver.get("https://leetcode.com/problems/median-of-two-sorted-arrays/")
		wait = WebDriverWait(driver, 20)
		title = driver.find_element_by_class_name("css-v3d350").text
		description = driver.find_element_by_class_name("content__u3I1").get_attribute('innerHTML')
		break
	except NoSuchElementException as e:
		print(e)

title = title.split(".")
title = f"{int(title[0]):04d}.{title[1]}"
full_path = f"/home/aaron/Projects/LeetCode/{title}"
mkdir(full_path)
with open(f"{full_path}/s.py", mode='w') as f:
	print('from typing import List\nfrom sys import argv as argv\n\n\n\n# argv[1]\n# print(Solution())', file=f)
with open(f"{full_path}/README.md", mode='w') as f:
	print(description, file=f)