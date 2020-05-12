#chrome_trex.py
import numpy as np 
import time,pyautogui
from PIL import ImageGrab, ImageOps

class coordinates():
	replaybutton = (488,264)
	#running.runner-canvas 600X150
	dinosaur = (177,294)

def restart_game():
	pyautogui.click(coordinates.replaybutton)
	pyautogui.keyDown('down')

def press_space():
	pyautogui.keyUp('down')
	pyautogui.keyDown('space')
	time.sleep(0.05)
	print("jump")
	pyautogui.keyUp('space')
	pyautogui.keyDown('down')

def image_grab():
	box = (coordinates.dinosaur[0] + 30, 
		coordinates.dinosaur[1], coordinates.dinosaur[0] + 120,
		coordinates.dinosaur[1] + 2)

	image = ImageGrab.grab(box)
	grayimage = ImageOps.grayscale(image)
	a = np.array(grayimage.getcolors())
	print(a.sum())
	return a.sum()
time.sleep(0.5)
restart_game()
while True:
	if(image_grab() != 435):
		press_space()
		time.sleep(0.1)

	
