import organizer
import time
import globalVariables
from tkinter import messagebox


def initiate():
    while True:
        try:
            if globalVariables.loop_on:
                organizer.move_documents_to_folder()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            time.sleep(5)
            continue

        time.sleep(1)
