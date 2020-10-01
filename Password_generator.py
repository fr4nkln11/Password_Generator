#!/usr/bin/python
# -*- coding: utf-8 -*-

# Password generator by Fr4nkl1n 1k3h
# The randomChar module was designed by Fr4nkl1n 1k3h

from randomchar import printable

print("""
	#####################
	## Welcome to my   ##
	## random password ##
	## generator       ##
	#####################
	""")
passwordLength = int(input('Type in the length of your password: '))
password = printable(passwordLength)
print("""
	######################################
	## Your newly generated password is ##
	######################################

\t\t{}

	######################################
	## Thanks for using my random       ##
	## password generator               ##
	######################################
	""".format(password))
