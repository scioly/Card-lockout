# essential Flask modules
from flask import Flask
from flask import request
from flask import render_template
# for reading the config file
import yaml
# for generating SQL queries in pure Python
import sql
# for interfacing with the PostgreSQL database
import psycopg2
# for generating JSON to send to the client
import json


# create the flask app
app = Flask( __name__ )

# a simple hello world route
@app.route( '/' )
def hello():
	return( "<h1><marquee>Hello, world!</marquee></h1>" )

# another route demoing how to use the request parameters
# try "http://localhost:5555/args?1=2&three=four"
@app.route( '/args' )
def returnArgs():
	return( str( request.args ) )

#################
# Server routes #
#################


@app.route( '/users', methods=['GET'] )
def users():
	"""
	This route will display the list of currently registered users, along with their authorizations, registration
	dates, and other info.
	"""
	return request.path


@app.route( '/users/add', methods=['POST'] )
def addUser():
	"""
	Responds with a webform to add a new user.
	"""
	return request.path


@app.route( '/users/new', methods=['POST'] )
def newUser():
	"""
	Accepts a request to add a user to the database.
	"""
	return request.path


@app.route( '/users/delete', methods=['POST'] )
def deleteUser():
	"""
	Deletes a user from the database.
	"""
	return request.path


@app.route( '/users/authorize', methods=['POST'] )
def authorizeUser():
	"""
	Adds an authorization to a specified user.
	"""
	return request.path


# run the app if the namespace is main
if __name__ == '__main__':
	with open( 'config.yaml' ) as f:
		config = yaml.load( f )

	# makes your life easier
	app.debug = True
	# and, run the app
	app.run( port=config['serverPort'] )
	# if you get errors, make sure to make a copy of `config_default.yaml` and
	# call it `config.yaml`
