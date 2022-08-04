import requests
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from sys import argv
from os import mkdir
from selenium.webdriver.common.by import By
import json
from time import sleep

'''
	parse through all of the problems that I've done
	make a list of the numbers
	go to website
	get a url for each item that I need
	for each:
		download description
		create readme file in the diretory
		put description in there

	Begin here: https://leetcode.com/problemset/all/?page=1

'''



options = ChromeOptions()
options.headless = True


links = {}

current_page = [1]

while current_page[0] < 49:
	try:
		url = f"https://leetcode.com/problemset/all/?page={current_page[0]}"
		driver = Chrome(executable_path='/home/aaron/Downloads/chromedriver', options=options)
		driver.get(url)

		sleep(10)
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		printed = False
		for link in soup.find_all("a", class_="h-5 hover:text-blue-s dark:hover:text-dark-blue-s"):
			print(f"{link.text} : https://leetcode.com{link.get('href')}")
			links[link.text.split('.')[0]] = f"https://leetcode.com{link.get('href')}"
		with open("links", "w") as f:
			json.dump(links, f)
		current_page[0] += 1
	except NoSuchElementException as e:
		print(e)


'''

<a href="/problems/two-sum" class="h-5 hover:text-blue-s dark:hover:text-dark-blue-s">1. Two Sum</a>
'''

# title = title.split(".")
# title = f"{int(title[0]):04d}.{title[1]}"
# full_path = f"/home/aaron/Projects/LeetCode/{title}"
# mkdir(full_path)
# with open(f"{full_path}/s.py", mode='w') as f:
# 	print('from typing import List\nfrom sys import argv as argv\n\n\n\n# argv[1]\n# print(Solution())', file=f)
# with open(f"{full_path}/README.md", mode='w') as f:
# 	print(description, file=f)