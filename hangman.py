''' Project #2: Hangman


Details:
Have you ever played hangman? It's a children's game, normally played by kids when they're supposed to be doing homework instead. 
If you've never played here are the rules:
https://www.youtube.com/watch?v=cGOeiQfjYPk


For this assignment, we want to play hangman in 2-player mode. The game should start by prompting player 1 to pick a word. 
Then the screen should clear itself so that player 2 can't see the word
hint: print(chr(27) + "[2J") 
After the screen is clear, the "gallows" and the empty letter spaces should be drawn, and player 2 should be 
allowed to guess letters until they either win, or lose. As they choose correct letters, the letters should appear on the screen in 
place of the blank space (clear and redraw the whole screen). As they choose wrong letters, the "man" himself should come end up being 
drawn, piece by piece. How many guesses they get before losing is up to you (depending on how complicated of a man you want to draw).

Extra Credit:
Try finding a large list of dictionary words and embedding them in your application. When the game starts, instead of 
player 1 choosing the word to play with, the computer should pick a random word from the dictionary. This will allow you to play 
against the computer instead of only 2-player mode. When the game starts, the user should be prompted to choose between 1-player or 
2-player mode.'''
import tkinter as tk
import turtle as t
global lsWord, word, strikes
import time as time

strikes = 0
#draw dashes for every letter in word
def dashes():
    global lsWord
    t.penup()
    t.setx(-350)
    t.sety(-300)
    for i in range(len(lsWord)):
        t.pendown()
        t.pensize(5) 
        t.fd(50)
        t.penup()
        t.fd(30)
        t.pendown()
        t.penup()

#draw gallows
def gallows():
    t.penup()
    t.setx(250)
    t.sety(-200)
    t.pendown()
    t.pensize(5)   
    t.lt(180)
    t.fd(100)
    t.lt(180)
    t.fd(200)
    t.lt(180)
    t.fd(100)
    t.rt(90)
    t.forward(300)
    t.lt(90)
    t.forward(200)
    t.lt(90)
    t.forward(50)

#draw head after 1st miss
def head():
        t.color('black')
        t.penup()
        t.setx(50)
        t.sety(50)
        t.dot(50)
        t.penup()
        t.color('white')

#draw body after 2nd miss
def body():
        t.color('black')
        t.penup()
        t.setx(50)
        t.sety(50)
        t.down()
        t.pendown()
        t.pensize(5)
        t.forward(125)
        t.penup()
        t.color('white')

#draw left leg after 3rd miss
def leftLeg():
    t.color('black')
    t.penup()
    t.setx(50)
    t.sety(-75)
    t.down()
    t.pendown()
    t.rt(30)
    t.fd(50)
    t.penup()
    t.color('white')

#draw right leg after 4th miss
def rightLeg():
    t.color('black')
    t.penup()
    t.setx(50)
    t.sety(-75)
    t.pendown()
    t.down()
    t.lt(60)
    t.fd(50)
    t.penup()
    t.color('white')

#draw left arm after 5th miss
def leftArm():
    t.color('black')
    t.penup()
    t.setx(50)
    t.sety(-25)
    t.pendown()
    t.down()
    t.rt(150)    
    t.fd(50)
    t.penup()
    t.color('white')

#draw right arm after 6th miss
def rightArm():
    t.color('black')
    t.penup()
    t.setx(50)
    t.sety(-25)
    t.pendown()
    t.down()
    t.rt(120)    
    t.fd(50)
    t.penup()

#send a nice message to the person who lost the game =)
def youDied():
    t.penup()
    t.setx(-200)
    t.sety(200)
    t.pendown()
    t.down()
    t.color('red')
    t.write('Player 2 is the loser', font=("Arial", 48, "normal"))

def youWon():
    t.penup()
    t.setx(-200)
    t.sety(200)
    t.pendown()
    t.down()
    t.color('red')
    t.write('Player 2 is the winner!', font=("Arial", 48, "normal"))
    time.sleep(5)
    exit()

#position of letters 0-8
def letter0():
    t.color('black')
    t.penup()
    t.setx(-350)
    t.sety(-300)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(guess, font=("Arial", 48, "normal"))
    t.color('white')

def letter1():
    t.color('black')
    t.penup()
    t.setx(-270)
    t.sety(-300)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(guess, font=("Arial", 48, "normal"))
    t.color('white')

def letter2():
    t.color('black')
    t.penup()
    t.setx(-190)
    t.sety(-300)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(guess, font=("Arial", 48, "normal"))
    t.color('white')

def letter3():
    t.color('black')
    t.penup()
    t.setx(-110)
    t.sety(-300)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(guess, font=("Arial", 48, "normal"))
    t.color('white')

def letter4():
    t.color('black')
    t.penup()
    t.setx(-30)
    t.sety(-300)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(guess, font=("Arial", 48, "normal"))
    t.color('white')

def letter5():
    t.color('black')
    t.penup()
    t.setx(50)
    t.sety(-300)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(guess, font=("Arial", 48, "normal"))
    t.color('white')

def letter6():
    t.color('black')
    t.penup()
    t.setx(130)
    t.sety(-300)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(guess, font=("Arial", 48, "normal"))
    t.color('white')

def letter7():
    t.color('black')
    t.penup()
    t.setx(210)
    t.sety(-300)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(guess, font=("Arial", 48, "normal"))
    t.color('white')

#counter for strikes
def strikez():
    if strikes == 1:
        head()
    elif strikes == 2:
        body()
    elif strikes == 3:
        leftLeg()
    elif strikes == 4:
        rightLeg()
    elif strikes == 5:
        leftArm()
    elif strikes == 6:
        rightArm()
        youDied()
        time.sleep(5)
        exit()



function_dict = {'letter0':letter0, 'letter1':letter1, 'letter2':letter2, 'letter3':letter3, 'letter4':letter4, 'letter5':letter5, 
                'letter6':letter6, 'letter7':letter7 }

#Allow player 1 to pick a word and then check for spaces and numbers.Save word as list - lsWord
while(True):
    word = input('Player 1, please pick a word less than 8 characters long.').upper()
    if word.isalpha():
        if len(word) > 8:
            print('Please pick a word only 8 characters long.')
        else:
            global lsWord
            lsWord = []
            for x in word:
                lsWord.append(x)
                winList = lsWord.copy()
            break
    elif " " in word:
        print('Please only use one word.')
    else:
        print("Please only use letters.")

dashes()
gallows()

while(strikes < 6):
    guess = input('Player 2, please make your guess.').upper()
    if guess.isalpha():
        if len(guess) > 1 or len(guess) < 1:
            print('Only enter 1 letter.')
        else:
            indices = [i for i, x in enumerate(lsWord) if x == guess]
            if guess in lsWord:
                print('Got it! ' + guess + ' is in there. Keep going! \n')
                for i in indices:
                    letterPosition = str('letter' + str(i))
                    function_dict[letterPosition]()
                    winList.remove(guess)
                    if len(winList) == 0:
                        youWon()
                        
            else:
                print('\nMissed that one bud. Try again. \n')
                strikes += 1
                strikez()
                time.sleep(1)
    

    elif " " in guess:
        print('Please only use 1 letter.')
    else:
        print("Please only use 1 letter.")







func = input('>')  #raw_input on python2.x




def letter1():
    t.penup()
    t.setx(-340)
    t.sety(-275)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(alphabet[0], font=("Arial", 48, "normal"))
    t.color('white')

def letter2():
    t.penup()
    t.setx(-260)
    t.sety(-275)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(alphabet[1], font=("Arial", 48, "normal"))
    t.color('white')

def letter3():
    t.penup()
    t.setx(-180)
    t.sety(-275)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(alphabet[2], font=("Arial", 48, "normal"))
    t.color('white')

def letter4():
    t.penup()
    t.setx(-100)
    t.sety(-275)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(alphabet[3], font=("Arial", 48, "normal"))
    t.color('white')

def letter5():
    t.penup()
    t.setx(-20)
    t.sety(-275)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(alphabet[4], font=("Arial", 48, "normal"))
    t.color('white')

def letter6():
    t.penup()
    t.setx(60)
    t.sety(-275)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(alphabet[5], font=("Arial", 48, "normal"))
    t.color('white')

def letter7():
    t.penup()
    t.setx(140)
    t.sety(-275)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(alphabet[6], font=("Arial", 48, "normal"))
    t.color('white')

def letter8():
    t.penup()
    t.setx(220)
    t.sety(-275)
    t.pendown()
    t.down()
    t.color('blue')
    t.write(alphabet[7], font=("Arial", 48, "normal"))
    t.color('white')

function_dict = {'letter1':letter1, 'letter2':letter2, 'letter3':letter3, 'letter4':letter4, 'letter5':letter5, 'letter6':letter6, 
                'letter7':letter7, 'letter8':letter8 }

alphabet = ['a','b','c','d','e','f','g','h']

dashes()
gallows()
head()
body()
leftLeg()
rightLeg()
leftArm()
rightArm()
youDied()
letter1()
letter2()
letter3()
letter4()
letter5()
letter6()
letter7()
letter8()

print(t.position())
print(lsWord)
# while(True):
#     for r in len(word):
#         guess = input('What letter do you want to guess?')


#Turtle

# word = str(input('word'))
# wordLen = len(word)
# lsWord = [word]

# t.circle(120, 180)  # draw a semicircle
# t.position()
# t.heading()

# t.write('string', font=("Arial", 36, "normal"))

# #draw spaces for word chosen
# for i in range(wordLen):
    
#     t.fd(30)
#     t.penup()
#     t.fd(30)
#     t.pendown()

t.mainloop()
