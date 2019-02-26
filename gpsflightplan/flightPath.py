from tkinter import *
from tkinter.filedialog import askopenfilename
from Graph import Graph
from PIL import Image, ImageTk

event2canvas = lambda e, c: (c.canvasx(e.x), c.canvasy(e.y))


def getPos(array):
    '''Creates a Tkinter window with an image to get mouse clicks for positions to visit'''
    # Adding position gotten into an array
    def addToArray(input, array):
        array.append(input)

    root = Tk()

    # Setting up tkinter window
    root.geometry('1280x720')
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E + W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N + S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N + S + E + W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH, expand=1)

    # Getting image
    File = askopenfilename(parent=root, initialdir="M:/", title='Choose an image.')
    print("opening %s" % File)
    img = ImageTk.PhotoImage(Image.open(File))
    #img = PhotoImage(file=File)
    canvas.create_image(0, 0, image=img, anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    # Local function to getting position of mouse
    def getCoords(event):
        cx, cy = event2canvas(event, canvas)
        addToArray((cx, cy), array)
        # Test for printing as soon as position is gotten
        # print("(%d, %d)" % (cx, cy))

    # Left mouse is pressed down
    canvas.bind("<ButtonPress-1>", getCoords)
    # Main loop for tkinter
    root.mainloop()


# Old manual path finding code
'''
def getDistance(start, end, array):
    #Pythagorus theorem to get distance between 2 points
    distance = (((array[end][0]-array[start][0])**2)+((array[end][1]-array[start][1])**2))**0.5
    #Printing for testing
    print(distance)
    return distance

#Outputs order of the path
def getPath(inp, output):
    #Assuming to set starting point as first point
    output.append(inp[0])
    end = inp[0]
    min = inp[0]
    for i in range(len(inp)-1):
        inp.remove(min)
        newmin = inp[0]
        for j in range(len(inp)-2):
            if getDistance(inp.index(min), j+1, inp)<getDistance(inp.index(min),j+2,inp):
                newmin = inp[j+1]
            elif getDistance(inp.index(min), j+1, inp)>getDistance(inp.index(min),j+2,inp):
                newmin = inp[j+2]


        output.append(newmin)
        min = newmin

    output.append(end)
    print("\nprinting order")
    print(output)
    #return output
'''


def newGraph(input, graph):
    '''Function to add all (x,y) coordinates from an input list into a graph'''
    for x, y in enumerate(input):
        # print(x)
        # print("reee")
        # print(y)
        graph.add_vertex(x, y[0], y[1])
    for i in range(len(input)):
        for j in range(len(input)):
            if i == j:
                continue
            else:
                graph.add_edge(i, j)


def pathFinder(graph):
    '''Generates a path to follow. Loosely based on Dijkstra's Algorithm
       Takes starting point, finds closest node, goes to it and adds previous position to the visited list.
       Outputs a list containing the path'''
    visited = []
    out = []
    s = -1
    end = -1

    for i in graph:
        temp = 999999999999999999999
        if s == -1:
            s = i
        if i in visited:
            continue
        for j in s.get_connections():

            if j in visited:
                continue
            if s == j:
                continue
            else:
                if s.get_weight(j) < temp:
                    temp = s.get_weight(j)
                    end = j
        out.append((s.get_id(), end.get_id()))
        visited.append(s)
        s = end
    out.append((end.get_id(), 0))
    return out


def drawPath(path):
    '''IN PROGRESS
       Generates a new image with the path drawn'''
    return


#Main
if __name__ == "__main__":
    #Create empty lists for positions and output path
    array = []
    out = []
    #Creates an empty graph
    g = Graph()

    #Get all the positions from the user
    getPos(array)
    #Print for testing
    print(array)

    #Sets up the graph with
    newGraph(array, g)

    #Test code to see all the connections in the graph
    #    for i in g:
    #        for j in i.get_connections():
    #            s = i.get_id()
    #            e = j.get_id()
    #            print('(%s, %s, %3d)' % (s, e, i.get_weight(j)))

    out = pathFinder(g)
    print(out)
