import simplegui
import random
import math


# helper function to start and restart the game
def new_game():
    global secret_number
    secret_number = random.randrange(1,100)
    print ("New game. Range is [0,100)")
    print ("Number of remaining guesses is 7")
    print ("")
    global counter
    counter = 0
    global n
    n = 7
    # initialize global variables used in your code here

    # remove this when you add your code    


# define event handlers for control panel
def range100(): #n = 7
    
    global secret_number
    
    secret_number = random.randrange(1,100)
    
    global counter
    
    counter = 0
    
    global n
    
    n = 7

    print ("New game. Range is [0,100)")
    
    print ("Number of remaining guesses is 7")
    
    print ("")
    
 
    
def range1000(): 
    
    global secret_number
    
    secret_number = random.randrange(1,1000)
    
    global counter
    
    counter = 0
    
    global n
    
    n = 10

    print ("New game. Range is [0,1000)")
    
    print ("Number of remaining guesses is 10")
    
    print ("")
    
def input_guess(guess):
    
    guess = int(guess)
    
    global counter
    
    counter += 1
    
    if n != counter:
        print ("Guess was " + str(guess))

        print ("Number of remaining guesses is " + str(n - counter))

        if guess > secret_number:
            
            print ("Lower!")
            
        elif guess < secret_number:
            
            print ("Higher!")
        
        else:
            print ("Correct!")
            
            print ("")
            
            print ("Game Over")
            
            print ("")
            
            if n == 10: 
                
                range1000()
            else:
                range100()
                

        print ("")
        
    else:
            print ("Guess was " + str(guess))
            
            if guess == secret_number:
                
                print ("Correct!")
                
            elif guess != secret_number:
                
                print ("You ran out of guesses. The number was " + str(secret_number))
                
            else:

                print ("Number of remaining guesses is " + str(n - counter))
            
            print ("")
        
            print ("Game Over")
        
            print ("")
        
            if n == 10: 
                
                range1000()
            else:
                range100()
                
# create frame
f = simplegui.create_frame("Guess The Number", 200, 200)

# register event handlers for control elements and start frame
f.add_input("Your guess", input_guess, 200)
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
# call new_game 
new_game()
