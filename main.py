from tkinter import *

root = Tk()
root.title("LiveTranscript")
rootWidth = 500
rootHeight = 200
root.geometry("500x200")
transcribe = Button(root, text ="Transcribe")
transcribe.place(relx=0.5, rely=0.5, anchor='center')
root.mainloop()