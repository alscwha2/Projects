import requests
import os
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

'''
	This is my attempt to also get the code to come with it. hasn't worked yet

'''


url = "https://leetcode.com/problems/reverse-integer/"

options = ChromeOptions()
options.headless = True

while True:
	try:
		driver = Chrome(executable_path='/home/aaron/Downloads/chromedriver', options=options)
		driver.get(url)
		wait = WebDriverWait(driver, 20)
		title = driver.find_element_by_class_name("css-v3d350").text
		description = driver.find_element_by_class_name("content__u3I1").get_attribute('innerHTML')
		# driver.execute_script("""
		# var l = document.getElementsByClassName("CodeMirror-gutter-wrapper");
		# for (let child of l)
		# 	child.parentNode.removeChild(child);
		# """)
		driver = excludeTagFromWebDriver(driver, ".CodeMirror-gutter-wrapper")
		code = driver.find_element(By.CLASS_NAME, "CodeMirror-code")
		soup = BeautifulSoup(code.get_attribute("innerHTML"), "html.parser")
		print(soup.prettify())
		# for tag in soup.find_all("div", "CodeMirror-linenumber CodeMirror-gutter-elt"):
		# 	tag.extract()
		# print(soup.get_text())
		# print(code.get_attribute("innerHTML"))
		print(code.text)
		break
	except NoSuchElementException as e:
		print(e)





'''

THIS IS THE CODE THAT I USED TO MAKE THE READMES FOR THE PROBLEMS THAT I ALREADY DID




options = ChromeOptions()
options.headless = True


links = {}
with open("links", "r") as f:
	links = json.load(f)

number_to_dir = {}
for problem in os.listdir('..'):
	if problem[0].isnumeric():
		number_to_dir[str(int(problem.split('.')[0]))] = problem



# print(sorted([int(j) for j in [str(i) for i in range(2361)] - links.keys()]))
# print(problem_numbers - links.keys())

for number in number_to_dir.keys():
	if number in links.keys():
		while True:
			try:
				url = links[number]
				driver = Chrome(executable_path='/home/aaron/Downloads/chromedriver', options=options)
				driver.get(url)
				description = driver.find_element_by_class_name("content__u3I1").get_attribute('innerHTML')
				full_path = f"/home/aaron/Projects/LeetCode/{number_to_dir[number]}/README.md"
				with open(full_path, "w") as f:
					print(description, file=f)
				print(full_path)
				print(description)
				break
			except NoSuchElementException as e:
				print(e)

				# <div data-cy="question-title" class="css-v3d350">2. Add Two Numbers</div>


'''



'''
THIS IS THE CODE THAT I USED TO GET ALL OF THE LINKS

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