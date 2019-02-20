import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename

if __name__=="__main__":
    # #This creates the main window of an application
    # window = tk.Tk()
    # window.title("Choose your points")
    # window.geometry("1920x1080")
    # window.configure(background='grey')
    #
    # path = askopenfilename(title = "Choose an Image")
    #
    # #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    # img = ImageTk.PhotoImage(Image.open(path))
    #
    # #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    # panel = tk.Label(window, image = img)
    #
    # #The Pack geometry manager packs widgets in rows or columns.
    # panel.pack(side = "bottom", fill = "both", expand = "yes")
    #
    # #Start the GUI
    # window.mainloop()
    print(tk.TkVersion)