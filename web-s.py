from selenium import webdriver 
from bs4 import BeautifulSoup
import pandas as pd 

driver = webdriver.Chrome("/usr/bin/chromedriver")

products = []
prices = []
ratings = []
driver.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2')


content = driver.page_source 
soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
	name = a.find('div', attrs={'class':'_3wU53n'})
	price = a.find('div', attrs={'class':'_6BWGkk'})
	rating = a.find('div', attrs={'class':'niH0FQ'})
	products.append(name.text)
	prices.append(price.text)
	ratings.append(rating.text)


df =  pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')