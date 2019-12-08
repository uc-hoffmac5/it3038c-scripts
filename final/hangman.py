#random is needed to pick the word
import random
#this function checks if the letter guessed in the word and its position and replaces it
#this is the only function cause it was getting way too indented and was hard to work with
def update_display(word, display, currentGuess):
    result=""
    for i in range(len(word)):
        if word[i] == currentGuess:
                result = result + currentGuess 
        else:
                result = result + display[i]
    return result
print("Let's play some Hangman!")
#promts the user to pick difficulty the response must be exactly E M or H
diff=input("What difficulty would you like to play?\n Type 'E' for easy, 'M' for medium, and 'H' for hard.")
if(diff=='E'):
    lives=5
    #preset list of 10 words. Using a dictionary made it slower and harder to test 
    wordList = ["deal","wing","gold","road","hill","myth","base","jail","silk","rule"]
    #picks a random word form the list
    word=random.choice(wordList)
    print("You will be guessing a random 4 letter noun. All letters entered must be lowercase")
    #variable to store the current guess
    currentGuess=""
    #an array to hold past guesses 
    pastGuesses=[]
    #the display is dashes times the length of the word
    display = "_" * 4
    #checks to see if either lives are used up or the word was guessed
    while (lives>0 and not display==word): 
            #skips 5 lines cause stuff was getting confusing during play
            print("\n \n \n \n \n")
            print("Here is your progress so far")
            print (display)
            print("You have already guessed:")
            print(pastGuesses)
            print ("You have "+ str(lives) + " lives left")
            currentGuess=input("What letter would you like to guess? \n")
            #check to see only one letter was added
            if len(currentGuess) > 1:
                    print('Please enter only one letter at a time')
            else:
                #checks for numbers, any number over 9 would be caught by the length check
                if (currentGuess is '1' or currentGuess is '2' or currentGuess is '3' or currentGuess is '4' or currentGuess is '5' or currentGuess is '6' or currentGuess is '7' or currentGuess is '8'  or currentGuess is '9' or currentGuess is '0' ):
                    print("Please enter a letter")
                else:  
                    #check if letter was already guessed  
                    if currentGuess in pastGuesses:
                        print("You have already guessed that letter")
                    elif currentGuess in word:
                        #correct guess adds the letter to the display
                        print ("That letter is in the word")
                        display = update_display(word, display, currentGuess)
                    else:
                        #incorrect guess subtracts a life
                        print("Sorry that letter is not in the word")
                        lives -= 1    
                    if currentGuess not in pastGuesses:
                        pastGuesses.append(currentGuess)

            
            
            if len(currentGuess) > 1:
                print('Please enter only one letter at a time')
            else:
            #check to see if the word was already guessed
                if currentGuess in pastGuesses:
                    print("You have already guessed that letter")
                  # a correct guess results in the function being called    
                elif currentGuess in word:
                     print ("That letter is in the word")
                     display = update_display(word, display, currentGuess)
                else:
                   #incorrect guess just subtracts a life
                  print("Sorry that letter is not in the word")
                  lives -= 1    
              #making sure the same letter doesnt appear twice in past guesses    
                if currentGuess not in pastGuesses:
                    pastGuesses.append(currentGuess)

        

    #check at the end to see which condition broke the loop
    if (lives == 0):
        print("\n \n \n \n \n")
        print("Sorry Looks like youre out of lives. \nThe word was " + word)
        print("Game Over")
    else:
        print("\n \n \n \n \n")
        print("You got it! The word was " + word)
        

#The next two sections are just for the other difficulties and the only differences
# are the word list and the ammount of dashses so I dont wanna repeat comments    

elif(diff=='M'):
    lives=5
    wordList = ["season","marble","thesis","copper","jockey","kettle","facade","spirit","detail","fossil"]
    word=random.choice(wordList)
    print("You will be guessing a random 6 letter noun. All letters entered must be lowercase")
    currentGuess=""
    pastGuesses=[]
    display = "_" * 6
    while (lives>0 and not display==word): 
            print("\n \n \n \n \n")
            print("Here is your progress so far")
            print (display)
            print("You have already guessed:")
            print(pastGuesses)
            print ("You have "+ str(lives) + " lives left")
            currentGuess=input("What letter would you like to guess? \n")
            
        
            if len(currentGuess) > 1:
                    print('Please enter only one letter at a time')
            else:
                if (currentGuess is '1' or currentGuess is '2' or currentGuess is '3' or currentGuess is '4' or currentGuess is '5' or currentGuess is '6' or currentGuess is '7' or currentGuess is '8'  or currentGuess is '9' or currentGuess is '0' ):
                    print("Please enter a letter")
                else:    
                    if currentGuess in pastGuesses:
                        print("You have already guessed that letter")
                    elif currentGuess in word:
                        print ("That letter is in the word")
                        display = update_display(word, display, currentGuess)
                    else:
                        print("Sorry that letter is not in the word")
                        lives -= 1    
                    if currentGuess not in pastGuesses:
                        pastGuesses.append(currentGuess)

   
    if (lives == 0):
        print("Sorry Looks like youre out of lives. \nThe word was " + word)
        print("Game Over")
    else:
        print("You got it! The word was " + word)
elif(diff=='H'):
    lives=5
    wordList = ["equation","patience","emphsis","threaten","unlikely","material","wardrobe","slippery","negative","collapse"]
    word=random.choice(wordList)
    print("You will be guessing a random 8 letter word. All letters entered must be lowercase")
    currentGuess=""
    pastGuesses=[]
    display = "_" * 8
    while (lives>0 and not display==word): 
            print("\n \n \n \n \n")
            print("Here is your progress so far")
            print (display)
            print("You have already guessed:")
            print(pastGuesses)
            print ("You have "+ str(lives) + " lives left")
            currentGuess=input("What letter would you like to guess? \n")
            
            if len(currentGuess) > 1:
                    print('Please enter only one letter at a time')
            else:
                if (currentGuess is '1' or currentGuess is '2' or currentGuess is '3' or currentGuess is '4' or currentGuess is '5' or currentGuess is '6' or currentGuess is '7' or currentGuess is '8'  or currentGuess is '9' or currentGuess is '0' ):
                    print("Please enter a letter")
                else:    
                    if currentGuess in pastGuesses:
                        print("You have already guessed that letter")
                    elif currentGuess in word:
                        print ("That letter is in the word")
                        display = update_display(word, display, currentGuess)
                    else:
                        print("Sorry that letter is not in the word")
                        lives -= 1    
                    if currentGuess not in pastGuesses:
                        pastGuesses.append(currentGuess)


        

   
    if (lives == 0):
        print("\n \n \n \n \n")
        print("Sorry Looks like youre out of lives. \nThe word was " + word)
        print("Game Over")
    else:
        print("\n \n \n \n \n")
        print("You got it! The word was " + word)
#If neither E M or H is picked the program closes
else:
    print("That was not one of the difficulties.")
    print("Launch the script again and please type either 'E' 'M' or 'H'")