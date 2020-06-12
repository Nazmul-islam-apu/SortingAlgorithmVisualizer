from tkinter import *
from tkinter import ttk
import random
from BubbleSort import bubble_sort
from MergeSort import  merge_sort

root = Tk()
root.title("Sorting Algorithm Visualization")
root.maxsize(900,600)
root.config(bg="black")

#Variables
selected_algo = StringVar()
dat = []

def drawData(data,colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width/(len(data)+1)
    offset = 10
    spacing = 5
    normalizedData = [i/max(data) for i in data]
    for i,height in enumerate(normalizedData):
        x0 =i*x_width+offset+spacing
        y0 =c_height-height*340
        x1 = (i+1)*x_width+offset
        y1 = c_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        #canvas.create_text(x0+2,y0,anchor = SW, text = str(data[i]))
    root.update_idletasks()

def Generate():
    global data
    min_value = int(min_entry.get())
    max_value = int(max_entry.get())
    size_value = int(size_entry.get())

    data = []
    for _ in range(size_value):
        data.append(random.randrange(min_value,max_value+1))
    drawData(data,["skyblue" for x in range(len(data))])

def StartAlgorithm():
    global data
    if not data:
        return
    if algo_menu.get()=="Bubble Sort":
        bubble_sort(data,drawData,speedScale.get())
    elif algo_menu.get()=="Merge Sort":
        merge_sort(data,drawData,speedScale.get())

    drawData(data, ["skyblue" for x in range(len(data))])


#frame/base Layout
UI_frame = Frame(root, width=600, height=200, bg = "grey")
UI_frame.grid(row=0,column=0, padx=10 ,pady=5)
canvas = Canvas(root,width=600, height= 380, bg = "white")
canvas.grid(row=1,column=0, padx=10, pady=5)

#User area
label = Label(UI_frame, text="Algorithm",bg="grey").grid(row=0,column=0,padx=5,pady=5,sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=selected_algo, values=["Bubble Sort","Merge Sort"])
algo_menu.grid(row=0,column=1,padx=5,pady=5)
algo_menu.current(0)
speedScale = Scale(UI_frame, from_=0.1,to = 1.0, length=200,digits = 2, resolution=0.02, orient = HORIZONTAL, label="Select Speed [S]" )
speedScale.grid(row=0,column = 2, padx=5,pady=5)
button = Button(UI_frame, text="start", command = StartAlgorithm, bg="skyblue").grid(row=0,column=3,padx=5,pady=5)


size_entry = Scale(UI_frame, from_=3,to = 100, resolution=1, orient = HORIZONTAL, label="Data Size" )
size_entry.grid(row=1, column=0,padx=5,pady=5)


min_entry = Scale(UI_frame, from_=0,to = 10, resolution=1, orient = HORIZONTAL, label="Min Value" )
min_entry.grid(row=1, column=1,padx=5,pady=5)


max_entry = Scale(UI_frame, from_=10,to = 100, resolution=1, orient = HORIZONTAL, label="Max Value" )
max_entry.grid(row=1, column=2,padx=5,pady=5)
button = Button(UI_frame, text="Generate", command = Generate, bg="skyblue").grid(row=1,column=3,padx=5,pady=5)
root.mainloop()