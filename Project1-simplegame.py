# Project #1: Connect 4

'''
Details:
 
Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro company. In this project, your task is create a Connect 4 game in Python. 
Before you get started, please watch this video on the rules of Connect 4:

https://youtu.be/utXzIFEVPjA

Once you've got the rules down, your assignment should be fairly straightforward. You'll want to draw the board, and allow two players to take turns 
placing their pieces on the board (but as you learned above, they can only do so by choosing a column, not a row). The first player to get 4 across or 
diagonal should win!

Normally the pieces would be red and black, but you can use X and O instead.


Extra Credit:

Want to try colorful pieces instead of X and O? First you'll need to figure out how to import a package like termcolor into your project. 
We're going to cover importing later in the course, but try and see if you can figure it out on your own. Or you might be able to find unicode 
characters to use instead, depending on what your system supports. Here's a hint: print(u'\u2B24')

Assuming a 7 wide x 6 high board:
   a b c d e f g
   _ _ _ _ _ _ _
1 |_|_|_|_|_|_|_|
2 |_|_|_|_|_|_|_|
3 |_|_|_|_|_|_|_|
4 |_|_|_|_|_|_|_|
5 |_|_|_|_|_|_|_|
6 |_|_|_|_|_|_|_|

 Possible winning combinations: 
    Vertical: 21 solutions A-G (1-4, 2-5, 3-6)
    Horizontal: 24 solutions 1-6 (a-d, b-e, c-f, d-g)
    Diagional: