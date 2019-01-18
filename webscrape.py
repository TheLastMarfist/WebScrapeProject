import requests
from bs4 import BeautifulSoup
import os
from twilio.rest import Client
from datetime import datetime, timedelta
import time
		


def main():
	websiteurl = input("What is the website url of the website you want to track?")
	numofminutes = int(input("After how many minutes do you check the website?"))
	account_sid = "ACf7a274e7d148a2036820f83f753ef12a"
	# Your Auth Token from twilio.com/console
	auth_token  = "a82c62ca2316987c134dd91f8fc3eb3b"
	client = Client(account_sid, auth_token)
	#https://thelastmarfist.github.io/WebScrapeProject/
	page = requests.get(websiteurl)
	soup = BeautifulSoup(page.content, 'html.parser')
	html = list(soup.children)[2]
	body = list(html.children)[1]
	p = list(body.children)[3]
	oldtext = p.get_text()


	while 1:
		page = requests.get(websiteurl)
		soup = BeautifulSoup(page.content, 'html.parser')
		html = list(soup.children)[2]
		body = list(html.children)[1]
		p = list(body.children)[3]
		newtext = p.get_text()
		if newtext != oldtext:
			oldtext = newtext
			message = client.messages.create(
				to="+19712843287", 
				from_="+13522898955",
				body="Your website has changed.")
		else:
			print("nothing has changed")

		dt = datetime.now() + timedelta(minutes = numofminutes)
		while datetime.now() < dt:
			time.sleep(1)
if __name__== "__main__" :
    main()