#!/usr/bin/python
# -*- coding: utf-8 -*-

# Password generator by Fr4nkl1n 1k3h
# The randomChar module was designed by Fr4nkl1n 1k3h

from random import shuffle
import randomChar as rc

randomLetter = rc.letter()
randomNumber = rc.digit()
randomSymbol = rc.symbol()
randomUpperCaseLetter = rc.upcase()


def generatePassword(length):
    """This function generates a password with random characters"""
    charList = []

    for i in range(length):
        charList.append(rc.all())

    shuffle(charList)
    return ''.join(charList)


print("""
	#####################
	## Welcome to my   ##
	## random password ##
	## generator       ##
	#####################
	""")
passwordLength = int(input('Type in the length of your password: '))
password = generatePassword(passwordLength)
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
