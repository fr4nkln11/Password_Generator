import random as r

ALPHABET = list('abcdefghijklmnopqrstuvwxyz')
ALPHABET_UPPER = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
NUMBERS = list('1234567890')
SYMBOLS = list(r"@#$%&-+=()*\"':;!?/.,{}][<>")

def all():
	randomCharList = [r.choice(ALPHABET), r.choice(NUMBERS), r.choice(SYMBOLS), r.choice(ALPHABET_UPPER)]
		
	return r.choice(randomCharList)
	
def letter():
	return r.choice(ALPHABET)
	
def letterUpper():
	return r.choice(ALPHABET_UPPER)
	
def number():
	return r.choice(NUMBERS)
	
def symbol():
	return r.choice(SYMBOLS)
		
		
if __name__ == "__main__":
	print("This module was created by FR4NKL1N_1K3H")
