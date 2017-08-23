import requests
import yaml


def runLoop( config ):
	"""
	Runs indefinitely. On user input (card swipe), will gather the card number,
	send it to the server configured, and if it has been authorized, open the
	relay with a GPIO call.
	"""
	while True:
		swipe = input()

		# check to see that this assumption of ID length is correct
		cardNumber = swipe
		print( 'The last input was ' + cardNumber )

		try:
			res = queryServer( cardNumber, config )
		except requests.exceptions.Timeout:
			print( "Server timeout!" )
			continue

		if res['isAuthorized']:
			# open the relay here
			pass


def queryServer( cardNumber, config ):
	url = 'http://' + str( config['serverAddress'] ) + ':' + str( config['serverPort'] )

	req = requests.get( url, {
		'cardNumber': cardNumber,
		'machineID': config['machineID'],
		'machineType': config['machineType']
	}, timeout=config['timeout'] )

	return req.json()


if __name__ == '__main__':
	# read and return a yaml file (called 'config.yaml' by default) and give it
	# back as a dictionary
	with open( 'config.yaml' ) as f:
		config = yaml.load( f )

	# run the main loop
	runLoop( config )
