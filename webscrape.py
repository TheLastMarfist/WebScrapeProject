import requests
from bs4 import BeautifulSoup
import os
from twilio.rest import Client
from datetime import datetime, timedelta
import time
		


def main():
	# user inputs
	websiteurl = input("What is the website url of the website you want to track?")
	numofminutes = int(input("After how many minutes do you check the website?"))
	account_sid = input("What is your Twilio account sid?")
	auth_token  = input("What is you Twilio authentication token?")
	twiliophonenumber = int(input("What is your Twilio phone number? Don't forget the country code e.g. +1 for the US."))
	userphonenumber = int(input("What is you phone number? Don't forget the country code e.g. +1 for the US."))
	# setting up messaging
	client = Client(account_sid, auth_token)
	# scraping the website as it is when you run the script
	page = requests.get(websiteurl)
	soup = BeautifulSoup(page.content, 'html.parser')
	html = list(soup.children)[2]
	body = list(html.children)[1]
	p = list(body.children)[3]
	oldtext = p.get_text()


	while 1:
		#checking for changes
		page = requests.get(websiteurl)
		soup = BeautifulSoup(page.content, 'html.parser')
		html = list(soup.children)[2]
		body = list(html.children)[1]
		p = list(body.children)[3]
		newtext = p.get_text()
		#comparing if something has changed
		if newtext != oldtext:
			oldtext = newtext
			message = client.messages.create(
				to=userphonenumber, 
				from_=twiliophonenumber,
				body="Your website has changed.")
		else:
			print("nothing has changed")
		#setiing up the automation loop
		dt = datetime.now() + timedelta(minutes = numofminutes)
		while datetime.now() < dt:
			time.sleep(1)
if __name__== "__main__" :
    main()
