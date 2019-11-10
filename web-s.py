from selenium import webdriver 
from BeautifulSoup import BeautifulSoup
import panda as pd 

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromiumdriver")

products = []
prices = []
ratings = []
driver.get("<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")


content = driver.page_source 
soup= BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_3wU53n'}):
	name=a.find('div', attrs={'class':'_3wU53n'})
	