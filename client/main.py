import requests


def watchInput():
	while True:
		swipe = input()

		# check to see that this assumption of ID length is correct
		cardNumber = swipe[4:11]
		print( 'The last input was ' + cardNumber )


def queryServer():
	# r = requests.post( {} )
	pass


if __name__ == '__main__':
	watchInput()
