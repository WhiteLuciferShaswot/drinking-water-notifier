import time
from plyer import notification

if __name__ == "__main__":
	while True:
	notification.notify(
	title = "please drink water",
	message = "from jarvis."
	timeout=10
	)
	time.sleep(60*60)
	
	### need to install plyer and after installing plyer use the above source code and after that open terminal of python and write pythonw ./main.py and this program will run automatic without terminal and python software and to stop this you should go to task manager and stop the app that name will related to python word ....
	