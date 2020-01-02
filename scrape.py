#! python3

from selenium import webdriver
import time
import sys

if len(sys.argv) > 1:
    # Get address from command line.
    token = ''.join(sys.argv[1:])
else:
  print("provide a token")
  sys.exit(1)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.binary_location = "/usr/bin/google-chrome"

driver = webdriver.Chrome(chrome_options=options)
driver.get(f"https://www.dailycodingproblem.com/solution/1?token={token}")


js = 'document.querySelector("button.cta.mobile.yellow").click()'
driver.execute_script(js)

js = 'document.querySelector("div.banner").style.display = "none"'
driver.execute_script(js)

js = 'document.querySelector("div.nav").style.display = "none"'
driver.execute_script(js)

js = 'document.querySelector("footer").style.display = "none"'
driver.execute_script(js)

js = 'return document.querySelector("header").innerText.split("#")[1]'
problem_number = driver.execute_script(js)

print(problem_number)

js = '[...document.querySelectorAll("script")].forEach(e => e.remove())'
driver.execute_script(js)

time.sleep(3)

js = 'return document.querySelector("header").innerText.split("#")[1]'
problem_number = driver.execute_script(js)

html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
html = f"<html>{html}</html>"

html_file = open(f"problem_{problem_number}.html", "w")
html_file.write(html)
html_file.close()
