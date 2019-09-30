import random
randomNumber = random.randint(0, 11)
print("What number am I thinking of?")
numberGuess = int(input())
while numberGuess != randomNumber:
    if numberGuess > randomNumber:
        print("No thats too high.")
        numberGuess = int(input())
    else:
        print("No thats too low.")
        numberGuess = int(input())
        
print("Yes thats the number I was thinking of!")
