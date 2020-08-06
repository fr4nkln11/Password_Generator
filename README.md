# Password_Generator
A simple password generator made with the help of a module I created "randomChar".
The code also uses the shuffle function from the random library to shuffle lists.
The code has no GUI for now but I'm still working on it

# What the program does
The password generator asks the user to input the required length of the password
Then the program generates a random password with the given length

# How the program works
The program uses the randomChar module to generate random characters(letters,numbers and symbols),
when it takes in the password length from the input which is an integer,
It loops through the range(password length) and appends the generated characters,
To a character list which is later shuffled and joined to produce a final string(password).

