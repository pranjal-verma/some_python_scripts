#insta_bot.py
from selenium import webdriver
import time
class InstaBot:
	def __init__(self,username,pwd):
		self.driver = webdriver.Chrome
		self.driver.get("https://www.instagram.com/")

new = webdriver.Chrome("path to your ChromeDriver") 
#InstaBot('prnjl','pwd')
new.get("https://www.instagram.com/")
time.sleep(5)
username = "user name"
pwd = "password"

enter_user  = new.find_element_by_xpath("//input[@name = \"username\"]").send_keys(username)
enter_pwd = new.find_element_by_xpath("//input[@name = \"password\"]").send_keys(pwd)
time.sleep(0.5)
new.find_element_by_xpath('//button[@type = "submit"] ').click()
time.sleep(5)
button = new.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]" )


button.click()

time.sleep(0.3)
profile = new.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')
profile.click()
time.sleep(2)
def get_names():
	followers = new.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
	followers.click()
	time.sleep(0.5)
	element = new.find_element_by_xpath("/html/body/div[4]/div/div[2]")
	#ew.execute_script('arguments[0].scrollIntoView')
	scroll_box = element
	last_height,height = 0 , 1
	while last_height != height:
		last_height = height
		time.sleep(1)
		height = new.execute_script("""
				arguments[0].scrollTo(0,arguments[0].scrollHeight);
				return arguments[0].scrollHeight;


			""",scroll_box)

	links = scroll_box.find_elements_by_tag_name('a')
	names = [name.text for name in links if name != '']
	time.sleep(0.5)
	new.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
	time.sleep(0.5)
	return names


def get_following():
	followers = new.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
	followers.click()
	time.sleep(0.5)
	element = new.find_element_by_xpath("/html/body/div[4]/div/div[2]")

	#ew.execute_script('arguments[0].scrollIntoView')
	scroll_box = element
	last_height,height = 0 , 1
	while last_height != height:
		last_height = height
		time.sleep(1)
		height = new.execute_script("""
				arguments[0].scrollTo(0,arguments[0].scrollHeight);
				return arguments[0].scrollHeight;


			""",scroll_box)

	links = scroll_box.find_elements_by_tag_name('a')
	following = [name.text for name in links if name != '']
	time.sleep(0.5)
	new.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
	return following
#print(get_following())
followers = get_names()
time.sleep(1.5)
follwing = get_following()

unfollowing = [user for user in follwing if user not in followers]
print(follwing)
print(unfollowing)

#print(names)
	#xpath('/html/body/div[4]/div/div[2]') #new.find_element_by_xpath("/html/body/div[4]/div/div[2]")
#new.execute_script('argument[0].scrollIntoView();',element)

#oldh = new.execute_script("return document.scroll	")
#new_height = 
#last_height = new.execute_script("return document.body.scrollHeight")
