import requests
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = ChromeOptions()
options.headless = True

driver = Chrome(executable_path='/home/aaron/Downloads/chromedriver', options=options)
driver.get("https://leetcode.com/problems/add-two-numbers/")

# element = driver.find_element_by_class_name("css-v3d350")
# print(element.text)


# html_string = requests.get("https://leetcode.com/problems/add-two-numbers/").text

wait = WebDriverWait(driver, 10)
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "css-v3d350")))
element = driver.find_element_by_class_name("css-v3d350")
print(element.text)
doc = BeautifulSoup(driver.page_source, "html.parser")
# print(doc)

#<div data-cy="question-title" class="css-v3d350">2. Add Two Numbers</div>
'''
<div class="content__u3I1 question-content__JfgR"><div><p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;">
<pre><strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>
</div></div>
'''