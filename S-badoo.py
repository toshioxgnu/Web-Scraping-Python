from selenium import webdriver 
from bs4 import BeautifulSoup
import pandas as pd 
import requests
from lxml import html
import json


session_requests = requests.session()

login_url = 'https://badoo.com/signin/'


with open("payload.json") as data:

	result = session_requests.post(
		login_url, data = json.load(data) ,
		headers = dict( referer=login_url )

		)
	url = 'https://badoo.com/search'
	result = session_requests.get(
		url, 
		headers = dict(referer = url)
	)	

	driver = webdriver.Chrome("/usr/bin/chromedriver")

	names = []
	ages = []
	images = []
	driver.get('https://badoo.com/search')


	content = driver.page_source 
	soup = BeautifulSoup(content, features="html.parser")
	for a in soup.findAll('a',href=True, attrs={'class':'user-card__content'}):
		name = a.find('div', attrs={'class':'user-card-caption__name'})
		age = a.find('div', attrs={'class':'user-card-caption__age'})
		image = a.find('img', attrs={'src':'user-card__img'})
		urllib.urlretrieve(src, image)
		name.append(name.text)
		age.append(age.text)


	df =  pd.DataFrame({'Nombre':names,'Age':ages})
	df.to_json('GenteCerca.json')