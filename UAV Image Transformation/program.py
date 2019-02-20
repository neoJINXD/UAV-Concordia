'''
This is the code that will run the program for the end user.
The user will be prompted to pick an image file to modify and then will get the chance to tell
the program how they want it to be transformed.
'''

import cv2
import base
from tkinter.filedialog import askopenfilename
import time

if __name__ == "__main__":
    print("Welcome to the Image Manipulator")
    while True:

        print("Please pick a file to apply the transformation to: ")
        time.sleep(2)
        file = askopenfilename()
        print()
        #Reads the image from the input given by user
        Img = cv2.imread(file, 0)
        #Breaks if no file picked
        if file == "":
            print("No file chosen")
            break

        #Gets transformation needed by the user
        print("What kind of transformation would you want to perform?")
        print()
        transformation = input("Translation, Rotation, Affine or Perspective?\n Enter \"stop\" to cancel and stop the program\n")
        #Ignores the case of the input
        transformation = transformation.lower()

        #Applies transformation chosen to the image chosen
        if transformation == "translation":
            down = input("How much movement down for the image: ")
            side = input("How much movement to the side for the image: ")
            base.translation(Img, down, side)

        elif transformation == "rotation":
            angle = int(input("Please enter the angle of how much you want the image to be rotated: "))
            base.rotation(Img, angle)

        elif transformation == "affine":
            print("An affine transformation places a triangle onto the image and changes the positions of the points.")
            down1 = int(input("\nHow far down do you want to stretch the top right: "))
            right1 = int(input("\nHow far to the right do you want to stretch the top right: "))
            down2 = int(input("\nHow far down do you want to stretch the bottom left: "))
            right2 = int(input("\nHow far to the right do you want to stretch the bottom left: "))
            base.affine(Img, down1, right1, down2, right2)

        elif transformation == "perspective":
            down1 = int(input("\nHow far down to stretch the top left corner: "))
            right1 = int(input("\nHow far to the right to stretch the top left corner: "))
            down2 = int(input("\nHow far down to stretch the top right corner: "))
            right2 = int(input("\nHow far to the right to stretch the top right corner: "))
            down3 = int(input("\nHow far down to stretch the bottom left corner: "))
            right3 = int(input("\nHow far to the right to stretch the bottom left corner: "))
            down4 = int(input("\nHow far down to stretch the bottom right corner: "))
            right4 = int(input("\nHow far to the right to stretch the bottom right corner: "))
            base.perspective(Img, down1, right1, down2, right2, down3, right3, down4, right4)

        elif transformation == "stop":
            break
        else:
            print("Invalid transformation indicated. Maybe check your spelling.\nTerminating program.")
            break


        #After the transformation is applied, asks the user if they want to repeat
        choice = input("Do you want to repeat with another image? (y/n)  ")
        if choice.lower() == "y":
            continue
        elif choice.lower() == "n":
            break
        else:
            print("Invalid choice. Terminating program.")
            break


    print("Thanks you for using the Image Manipulator!")