from tkinter import Button, Tk, BOTH
import miscs
import organizerLoop
import globalVariables
import os


def start_stop():
    if globalVariables.loop_on:
        loop_button["text"] = "Start"
        globalVariables.loop_on = False
    else:
        globalVariables.loop_on = True
        loop_button["text"] = "Stop"


root = Tk()

window_width = 250
window_height = 100

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry("250x100+" + str(int(x)) + "+" + str(int(y)))
if os.path.isfile("icon/organizer.ico"):
    root.iconbitmap("icon/organizer.ico")
root.title("File Organizer")
root.resizable(False, False)

loop_button = Button(root, text="Start", height=2, width=10, font=("Arial", 25, "bold"), command=start_stop)
loop_button.pack(fill=BOTH, expand=True, padx=5, pady=5)

miscs.multithreading(lambda: organizerLoop.initiate())

root.mainloop()
