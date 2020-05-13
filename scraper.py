#scraper.py
import requests
from bs4 import BeautifulSoup
import  smtplib
import time
#from email.mime.te
def price_scraper():


	URL = 'https://www.amazon.in/Corsair-Vengeance-3000Mhz-Motherboard-CMK8GX4M1D3000C16/dp/B07B4FRMGV/ref=sr_1_1?dchild=1&keywords=ram&qid=1589183504&sr=8-1'
	header = {} #add useragent here
	#"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
	
	page = requests.get(URL,headers = header)
	soup = BeautifulSoup(page.content,'html.parser')
	title = soup.find(id = "productTitle").get_text()
	price = soup.find(id = "priceblock_ourprice").get_text()
	price = price[2:].replace(',','')

	converted = float(price)
	if converted < 4000:
		send_mail()

	print(converted)
	print(type(converted))
def send_mail():
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('example@gmail.com','randomwkdklsjfflsd')
	subject = "Price fell down"
	body = "https://www.amazon.in/Corsair-Vengeance-3000Mhz-Motherboard-CMK8GX4M1D3000C16/dp/B07B4FRMGV/ref=sr_1_1?dchild=1&keywords=ram&qid=1589183504&sr=8-1"

	message = f"Subject:{subject} \n\n\n {body}"
	server.sendmail('sendermail',
		'receivers mail',message

		)
	print("email sent")
	server.quit()


	#server_smtp = "smtp.mailtrap.io"
	#port = 2525

	#login, password = 


price_scraper()
while(True):
	price_scraper()
	time.sleep(86400)