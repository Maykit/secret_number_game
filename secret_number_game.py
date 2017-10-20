# This is a "Geuss a secret nummber" game

secret = 6

guess = int(raw_input("Guess the secret number. Type it here if you dare: "))

if guess == 6:
    print "This is an excellent choice. You guessed right."
else:
    print "You are a fool. You will never guess the secret number, hahaha."
