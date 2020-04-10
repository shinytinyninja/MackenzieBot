import tkinter as tk

def displayMenu():
    print("hello")
    window = tk.Tk()
    window.title("Mackenzie Bot")

    tk.Button(window, text = "Start New Session")
    tk.Button(window, text = "Continue Last Session")
    window.mainloop()

def displayStartNewMenu():
    print("start Menu")

def displayContinueMenu():
    print("continue Menu")


#for testing purposes
displayMenu()