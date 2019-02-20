'''
This is the file that contains all the base functions used to perform each of the image manipulations.
The functions do take away all the colour present in the images.
By pressing a key on the keyboard, the test code will advance ot the next transformation.
'''



import cv2
import numpy as np
import time

def default(Img):
    '''Default image "printing", will open a window with the image imputed without changing it.'''
    cv2.imshow("Default", Img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def translation(Img, down, side):
    '''Function to apply a translation transformation to the image that was chosen.'''
    rows, cols = Img.shape

    M = np.float32([[1, 0, side], [0, 1, down]])
    dst = cv2.warpAffine(Img, M, (cols, rows))


    cv2.imshow('Translation', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotation(Img, angle):
    '''Functions to apply a rotation to the image chosen.'''
    rows, cols = Img.shape

    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    dst = cv2.warpAffine(Img, M, (cols, rows))

    cv2.imshow('Rotation', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def affine(Img, stretchDown1, stretchRight1, stretchDown2, stretchRight2):
    '''Function to apply an affine tranformation to the image chosen'''
    rows, cols = Img.shape

    pts1 = np.float32([[0, 0], [200, 0], [0, 200]])
    pts2 = np.float32([[0, 0], [200+stretchRight1, 0+stretchDown1], [0+stretchRight2, 200+stretchDown2]])

    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(Img, M, (cols, rows))


    cv2.imshow("Affine",dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def perspective(Img, topLeftDown, topLeftRight, topRightDown, topRightRight, bottomLeftDown, bottomLeftRight, bottomRightDown, bottomRightRight):
    '''Function to apply a change of perspective to teh image chosen'''
    rows, cols = Img.shape

    pts1 = np.float32([[0+topLeftRight, 0+topLeftDown], [300+topRightRight, 0+topRightDown], [0+bottomLeftRight, 300+bottomLeftDown], [300+bottomRightRight, 300+bottomRightDown]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(Img, M, (300, 300))

    cv2.imshow("Perspective",dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__== "__main__" :
    print("Beginning testing of code\n")

    print("Grabbing test images")
    time.sleep(2)
    inputImg = cv2.imread("testGraphics/neo.png",0)
    inputImg2 = cv2.imread("testGraphics/red.png",0)
    inputImg3 = cv2.imread("testGraphics/grid.png",0)

    print("Showing default versions of the images")
    time.sleep(2)
    default(inputImg)
    default(inputImg2)
    default(inputImg3)

    print("Now applying translation transformation, with a down movement of 50 and a side movement of 100")
    translation(inputImg, 50, 100)

    print("Now applying rotation transformation with 90 degrees")
    rotation(inputImg2, 90)

    print("Now applying affine transformation")
    affine(inputImg3, 50, 0, 60, 100)

    print("Now applying perspective transformation")
    perspective(inputImg3, 65, 56, 52, 68, 87, 28, 89, 120)

    print("\nTest code finished. Have a nice day")