UAV Image Manipulation Tutorial

"As a programmer unfamiliar with OpenCV, I want to do the Geometric Transformations of Images tutorial, so that I can familiarize myself with OpenCV."

This program is contained within 2 files:

-base.py	: This file contains all the functions for each of the Image Manipulations 
		  that we can perform and has a list of test code that will use the images 
		  in the repository to test them.
-program.py	: This file is the main program, containing the code that will ask the user
		  to input a file using a tkinter fiel selection interface and will ask them
		  what kind of transformation they would like to do to the chosen image.

Changes left:
Force window to the front


The following functions are the ones in base.py:

->default(Image):
Takes an image that has been imputed and displays it in a window.

->translation(Image, Move down, Move right):
Takes an image that has been imputed and changes its size down and to the right by the specified amount.

->rotation(Image, Angle):
Takes an image that has been imputed and rotates it by a specified angle.

->affine(Image, Top Right stretch Down, Top Right stretch Right, Bottom Left stretch Down, Bottom Left stretch Right):
Takes an image that has been imputed and stretches a point that is located in the top right down and to the right by a specified amount, and does the
same thing for a point located in the bottom left of the image.

->perspective(Image, ):
Takes an image that has been imputed and makes the user specify 4 points on the image to form a "square" then zooms into the points specified and forms
a new image in the form of a 300x300 square.
