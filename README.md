[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Password_Generator
A simple password generator made with the help of a module I created "randomchar".
The code has no GUI for now but I'm still working on it

# What the program does
The password generator asks the user to input the required length of the password
Then the program generates a random password with the given length

# How the program works
The program uses the randomchar module to generate random characters(letters,numbers and symbols),
when it takes in the password length from the input which is an integer,
It loops through the range(password length) and appends the generated characters,
To a character list which is later shuffled and joined to produce a final string(password).

The program now uses a modified version of the randomchar module
In this version passwords are created using the `randomchar.printable()` function.

[Check the repo](https://github.com/fr4nkl1n-1k3h/randomchar) for more information on how it works

