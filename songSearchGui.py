from tkinter import *

#setup window
window = Tk() 
window.title("Music Search")
window.geometry('350x200')

#create a label entry
lbl = Label(window, text = "What would you like to search by?", font =("Arial Bold", 16))
lbl.grid(column=0, row=0) 

#create a text box
txt = Entry(window,width=10)
txt.grid(column = 1, row = 0)

#handle button click events
def clickedArtist():
    lbl.configure(text="Enter an Artists name:")
    btnEnter = Button(window, text="Enter")
    btnEnter.grid(column=2, row =0)

def clickedSongName():
    lbl.configure(text="Enter song name:")
    btnEnter = Button(window, text="Enter")
    btnEnter.grid(column=2, row =0)




#add buttons
btnArtist = Button(window, text="Artist", command=clickedArtist, bg="orange", fg="red")
btnArtist.grid(column=0, row=1)

btnSongName = Button(window, text = "Song Name", command=clickedSongName)
btnSongName.grid(column = 0, row = 2)






#keep window running forever
window.mainloop()