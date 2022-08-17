# from pynput.keyboard import Key, Controller
from pynput import keyboard
from pynput.keyboard import Controller, Key
import time
from plyer import notification
import string
from random import randrange

c = Controller()

print("ALICE: Hi! I'm Alice, your personal keystrokes assistant. Below is a list of commands I currently support.")
print("git stage and prepare commit | 0 + g + s")
print("git commit and push main to origin | 0 + g + c")
print("setup itpedia dev environment | 0 + i + p")
print("setup google workspace | 0 + g + w")
print("type email footer | 0 + e + f")
print("close all applications | 0 + c + a")
print("print primary email | 0 + c + k")
print("open localhost in browser | 0 + l + h")
print("setup uglesoft workspace | 0 + u + w")
print("setup recording studio | 0 + r + s")
print("generate password | 0 + g + p")
print("setup finance workspace | 0 + f + w")
print("setup social media tabs | 0 + s + m")

def notif_begin(function_name):
	notification.notify(
		title = "Alice",
		message = function_name + " has been initiated!",
		app_icon = "",
		timeout  = 1
	)

def notif_end(function_name):
	notification.notify(
		title = "Alice",
		message = function_name + " is completed!",
		app_icon = "",
		timeout  = 1
	)

def git_stage():
	# Printing function initialization message
	print('Function <git stage> activated.')

	# Releasing activation keys
	c.release('0')
	c.release('g')
	c.release('s')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.2)

	# Staging changes
	c.type('git add .')
	time.sleep(.2)
	
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(.2)

	# Preparing commit
	c.type('git commit -m "')
	time.sleep(.2)

	# Printing function completion message
	notif_end("<git_stage>")
	print('Function <git stage> completed, please enter a commit message.')


def git_commit():
	# Printing function initialization message
	print('Function <git_commit> activated.')

	# Releasing activation keys
	c.release('0')
	c.release('g')
	c.release('c')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.2)

	# Completing commit
	c.type('"')
	time.sleep(.2)

	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(.2)

	# Checking commit status
	c.type('git status')
	time.sleep(.2)

	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(.2)

	# Pushing to origin
	c.type('git push origin main')
	time.sleep(.2)

	c.press(Key.enter)
	c.release(Key.enter)

	# Printing function completion message
	notif_end("<git_commit>")
	print('ALICE: Function <git_commit> completed.')


def itpedia():
	# Printing function initialization message
	print('ALICE: function <itpedia> activated.')

	# Releasing activation keys
	c.release('0')
	c.release('i')
	c.release('p')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(1)

	# Searching Windows
	c.press(Key.cmd_l)
	c.release(Key.cmd_l)
	time.sleep(1)
	c.type("cmd")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	# Navigating to D:
	c.type("D:")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	# Navigating to ITpedia
	c.type("cd /_uglesoft/uglesoft.com/itpedia.uglesoft.com")
	time.sleep(.2)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(.2)
	c.type("code .")
	time.sleep(.2)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(8)

	# Returning to terminal
	c.press(Key.alt)
	c.press(Key.tab)
	c.release(Key.alt)
	c.release(Key.tab)
	time.sleep(1)
	c.type("php artisan serve")
	time.sleep(.2)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	# Searching Windows
	c.press(Key.cmd_l)
	c.release(Key.cmd_l)
	time.sleep(1)
	c.type("chrome")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	# Searching Windows
	c.type("http://127.0.0.1:8000/")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	# Printing function completion message
	notif_end("<itpedia>")
	print('ALICE: Function <itpedia> completed.')


def google_workspace():
	# Printing function initialization message
	print('ALICE: function <google_workspace> activated.')

	# Releasing activation keys
	c.release('0')
	c.release('g')
	c.release('w')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(1)

	# Searching Windows
	c.press(Key.cmd_l)
	c.release(Key.cmd_l)
	time.sleep(1)
	c.type("chrome")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(2)

	c.type('https://music.youtube.com/playlist?list=RDCLAK5uy_kb7EBi6y3GrtJri4_ZH56Ms786DFEimbM')
	c.press(Key.enter)
	c.release(Key.enter)

	time.sleep(8)
	c.press(Key.tab)
	c.release(Key.tab)
	time.sleep(0.25)
	c.press(Key.tab)
	c.release(Key.tab)
	time.sleep(0.25)
	c.press(Key.tab)
	c.release(Key.tab)
	time.sleep(0.25)
	c.press(Key.tab)
	c.release(Key.tab)
	time.sleep(0.25)
	c.press(Key.enter)
	c.release(Key.enter)
	
	time.sleep(4)
	c.press(Key.ctrl)
	c.press('t')
	c.release(Key.ctrl)
	c.release('t')

	time.sleep(1)
	c.type('https://drive.google.com/drive/my-drive')
	c.press(Key.enter)
	c.release(Key.enter)

	time.sleep(1)
	c.press(Key.ctrl)
	c.press('t')
	c.release(Key.ctrl)
	c.release('t')

	time.sleep(1)
	c.type('https://calendar.google.com/calendar/u/0/r?pli=1')
	c.press(Key.enter)
	c.release(Key.enter)

	time.sleep(1)
	c.press(Key.ctrl)
	c.press('t')
	c.release(Key.ctrl)
	c.release('t')

	time.sleep(1)
	c.type('https://mail.google.com/mail/u/0/#inbox')
	c.press(Key.enter)
	c.release(Key.enter)

	# Printing function completion message
	notif_end("<google_workspace>")
	print('ALICE: Function <google_workspace> completed.')


def email_footer():
	# Printing function initialization message
	print('ALICE: function <email_footer> activated.')

	# Releasing activation keys
	c.release('0')
	c.release('e')
	c.release('f')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.2)

	# Typing Email footer
	c.type("Respectfully,")
	c.press(Key.enter)
	c.release(Key.enter)
	c.type("Christian Kesler")

	# Printing function completion message
	notif_end("<email_footer>")
	print('ALICE: Function <email_footer> completed.')


def close_all():
	# Printing function initialization message
	print('ALICE: function <close_all> activated.')

	# Releasing activation keys
	c.release('c')
	c.release('a')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.2)

	for z in range(10):
		c.press(Key.alt)
		c.press(Key.f4)
		c.release(Key.alt)
		c.release(Key.f4)
		print('--iteration' + str(z))
		time.sleep(.2)

	# Printing function completion message
	notif_end("<close_all>")
	print('ALICE: Function <close_all> completed.')


def primary_email():
	# Printing function initialization message
	print('ALICE: function <primary_email> activated.')

	# Releasing activation keys
	c.release('0')
	c.release('c')
	c.release('k')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.2)

	# Typing Email footer
	c.type("christian.j.kesler@gmail.com")
	
	# Printing function completion message
	notif_end("<primary_email>")
	print('ALICE: Function <primary_email> completed.')


def localhost():
	# Printing function initialization message
	print('ALICE: function <localhost> activated.')

	# Releasing activation keys
	c.release('0')
	c.release('l')
	c.release('h')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.2)


	# Searching Windows
	c.press(Key.cmd_l)
	c.release(Key.cmd_l)
	time.sleep(1)
	c.type("chrome")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	# Searching Windows
	c.type("http://127.0.0.1:8000/")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	# Printing function completion message
	notif_end("<localhost>")
	print('ALICE: Function <localhost> completed.')


def uglesoft_workspace():
	# Printing function initialization message
	print('ALICE: function <uglesoft_workspace> activated.')

	# Releasing activation keys
	c.release('0')
	c.release('u')
	c.release('w')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.2)

	# Searching Windows
	c.press(Key.cmd_l)
	c.release(Key.cmd_l)
	time.sleep(1)
	c.type("cmd")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	# Navigating to D:
	# c.type("D:")
	# time.sleep(.2)
	# c.press(Key.enter)
	# c.release(Key.enter)
	# time.sleep(.2)

	# Navigating to ITpedia
	c.type("cd C:/Users/chris/Documents/_uglesoft")
	time.sleep(.2)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(.2)
	c.type("code .")
	time.sleep(.2)
	c.press(Key.enter)
	c.release(Key.enter)

	# Printing function completion message
	notif_end("<uglesoft_workspace>")
	print('ALICE: Function <uglesoft_workspace> completed.')


def recording_studio():
	# Printing function initialization message
	print('ALICE: function <recording_studio> activated.')

	# Releasing activation keys
	c.release('0')
	c.release('r')
	c.release('s')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(1)

	# Searching Windows
	c.press(Key.cmd_l)
	c.release(Key.cmd_l)
	time.sleep(1)
	c.type("cmd")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	# Navigating to Videos
	c.type("cd /Users/chris/Videos")
	time.sleep(.2)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(.2)
	c.type("explorer .")
	time.sleep(.2)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(.2)


	# Searching Windows
	c.press(Key.cmd_l)
	c.release(Key.cmd_l)
	time.sleep(1)
	c.type("OBS")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	# Searching Windows
	c.press(Key.cmd_l)
	c.release(Key.cmd_l)
	time.sleep(1)
	c.type("Voicemod")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(1)

	# Printing function completion message
	notif_end("<recording_studio>")
	print('ALICE: Function <recording_studio> completed.')


def generate_password():
	# Printing function initialization message
	print('ALICE: function <generate_password> activated.')

	password_raw = ""
	password_shuffled = ""

	digits = "0123456789"

	characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + digits

	password_raw = string.ascii_lowercase[randrange(len(string.ascii_lowercase))] + string.ascii_uppercase[randrange(len(string.ascii_uppercase))] + string.punctuation[randrange(len(string.punctuation))]	+ digits[randrange(len(digits))]

	for x in range(12):
		password_raw = password_raw + characters[randrange(len(characters))]

	for x in range(len(password_raw)):
		index = randrange(len(password_raw))

		password_shuffled = password_shuffled + password_raw[index]
		password_raw = password_raw[0:index] + password_raw[(index+1):]

	bar = ""
	for x in range(32):
		bar = bar + "="

	print(bar)
	print(password_shuffled)
	print(bar)

	notif_end("generate_password")

	print('ALICE: Function <generate_password> completed.')


def finance_workspace():
	# Printing function initialization message
	print('ALICE: function <finance_workspace> activated.')

	# Releasing activation keys
	c.release('0')
	c.release('f')
	c.release('w')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(1)

	# Searching Windows
	c.press(Key.cmd_l)
	c.release(Key.cmd_l)
	time.sleep(1)
	c.type("chrome")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(2)

	c.type('https://www.google.com/publicdata/explore?ds=dhcr7fgrs7s0l_#!ctype=l&strail=false&bcs=d&nselm=h&met_y=infl_m&fdim_y=item_code:SA0&fdim_y=seasonality:U&scale_y=lin&ind_y=false&rdim=country&idim=country:US&ifdim=country&tstart=1576047600000&tend=1657522800000&hl=en_US&dl=en_US&ind=false')
	c.press(Key.enter)
	c.release(Key.enter)

	time.sleep(1)
	c.press(Key.ctrl)
	c.press('t')
	c.release(Key.ctrl)
	c.release('t')

	time.sleep(1)
	c.type('https://www.google.com/finance/quote/.INX:INDEXSP?hl=en')
	c.press(Key.enter)
	c.release(Key.enter)

	# Printing function completion message
	notif_end("<finance_workspace>")
	print('ALICE: Function <finance_workspace> completed.')


def social_media():
	# Printing function initialization message
	print('ALICE: function <social_media> activated.')

	# Releasing activation keys
	c.release('0')
	c.release('s')
	c.release('m')
	# Deleting activation output
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(1)

	# Searching Windows
	c.press(Key.cmd_l)
	c.release(Key.cmd_l)
	time.sleep(1)
	c.type("chrome")
	time.sleep(1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(2)

	c.type('https://www.facebook.com/')
	c.press(Key.enter)
	c.release(Key.enter)

	time.sleep(1)
	c.press(Key.ctrl)
	c.press('t')
	c.release(Key.ctrl)
	c.release('t')

	time.sleep(1)
	c.type('https://www.linkedin.com/in/christian-kesler/')
	c.press(Key.enter)
	c.release(Key.enter)

	time.sleep(1)
	c.press(Key.ctrl)
	c.press('t')
	c.release(Key.ctrl)
	c.release('t')

	time.sleep(1)
	c.type('https://twitter.com/home')
	c.press(Key.enter)
	c.release(Key.enter)

	# Printing function completion message
	notif_end("<social_media>")
	print('ALICE: Function <social_media> completed.')


with keyboard.GlobalHotKeys(
	{
		'0+g+s': git_stage,
		'0+g+c': git_commit,
		'0+i+p': itpedia,
		'0+g+w': google_workspace,
		'0+e+f': email_footer,
		'0+c+a': close_all,
		'0+c+k': primary_email,
		'0+l+h': localhost,
		'0+u+w': uglesoft_workspace,
		'0+r+s': recording_studio,
		'0+g+p': generate_password,
		'0+f+w': finance_workspace,
		'0+s+m': social_media
	}
) as h:
	h.join()