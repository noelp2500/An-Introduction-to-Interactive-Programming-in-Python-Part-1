#Guess the Number game
#Author - Noel Pereira
#Submission link - http://www.codeskulptor.org/#user47_tlxfaASyB0w2V8F.py

#############################################################################################



import simplegui
import random
import math

num_range = 100
count = 0
number = 7

# helper function to start and restart the game
# if value is entered, it assumes a [0,100) range
print "New game. Guess a number"
print "First step is to select a range and then input the number"
print " "
print "Remaining number of tries:", number

def new_game(a=0): 
    global number
    global secret_number
    global b
    b = a
    
    if b == 0:
        secret_number = random.randrange(0, 100)
        
    else:
        secret_number = random.randrange(0, 1000)
        
    global count
    count = 0
    
    
    
    
# define event handlers for control panel
def range100():
    new_game(0)
    print " "
    print "Range selected is [0,100)"
    print " "
    
    
def range1000():
    new_game(1)
    print " "
    print "Range selected is [0,1000)"
    print " "
    
    
def input_guess(guess):
    
    global number
    global count
    
    if count < number:
        global secret_number
        count = count + 1
        number_guess = int(guess)
        
        print "Guess was", number_guess
        
        if secret_number < number_guess:
            print "Lower"
            print "Remaining tries:", number - count
            print " "
            
        if secret_number > number_guess:
            print "Higher"
            print "Remaining tries:", number - count
            print " "
            
        if secret_number == number_guess:
            print "Correct guess"
            print "Remaining tries:", number - count 
            print "You win! start new game!"
            print " "
            
            new_game()
            
        if count == number:
            print "You ran out of tries!"
            print "Correct answer is", secret_number
            print " "
            new_game()
      
# create frame
frame = simplegui.create_frame('Guess the number!', 200, 200)

# create control elements

frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess!", input_guess, 200)

# call new_game 
new_game()