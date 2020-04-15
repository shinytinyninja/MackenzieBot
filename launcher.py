import tkinter as tk
import initalBookParse as initalBookParse

class launcher:
    allButtons = []
    allLabels = []
    allTextEntrys = []
    fileName = ""

    def __init__(self, master):
        self.master = master
        self.upperFrame = tk.Frame(self.master)
        self.midFrame = tk.Frame(self.master)
        self.lowerFrame = tk.Frame(self.master)
        self.displayMenu()

    def clearScreen(self):
        for label in self.allLabels:
            label.destroy()

        for button in self.allButtons:
            button.destroy()

        for text in self.allTextEntrys:
            text.destroy()

    def menuBar(self):
        self.master.title("Simple menu")

        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label="Exit")
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Edit", menu=fileMenu)
        menubar.add_cascade(label="Print", menu=fileMenu)

    def displayMenu(self):
        self.clearScreen()
        self.menuBar()
        self.displayFormat()

        self.upperFrame.pack()
        self.midFrame.pack()
        self.lowerFrame.pack()

        self.startButton = tk.Button(self.midFrame, text="Start New Session", pady=10, command=self.displayStartNewMenu)
        self.contineButton = tk.Button(self.midFrame, text="Continue Last Session", pady=10, command=self.displayContinueMenu)
        self.AlertButton = tk.Button(self.midFrame, text="Display Alerts", pady=10, command=self.displayAlert)
        
        self.allButtons.extend((self.startButton, self.contineButton, self.AlertButton))

        self.startButton.pack(side="left")
        self.contineButton.pack(side="left")
        self.AlertButton.pack(side="left")

    def displayStartNewMenu(self):
        self.clearScreen()
        self.menuBar
        self.displayFormat()

        self.upperFrame.pack()
        self.midFrame.pack()
        self.lowerFrame.pack()

        self.fileEntry = tk.Entry(self.midFrame)
        self.status = tk.Label(self.midFrame, text=" ")
        self.enterButton = tk.Button(self.midFrame, text="Enter")
        self.viewAll = tk.Button(self.midFrame, text="View All HTML Files", command=self.displayAllHtmlFiles)
        
        self.allButtons.extend((self.startButton, self.contineButton))
        self.allTextEntrys.append(self.fileEntry)

        self.fileEntry.pack()
        self.status.pack()
        self.enterButton.pack()
        self.viewAll.pack()
        self.master.bind('<Return>', self.enterSubmitInfo)

    def enterSubmitInfo(self, event):
        self.submitInfo()
    
    def submitInfo(self):
        self.fileName = str(self.fileEntry.get())

    def displayContinueMenu(self):
        print("Hello")

    def displayAllHtmlFiles(self):
        self.clearScreen()
        self.displayFormat()

    def displayAlert(self):
        print("displayAlerts")

    def displayFormat(self):
        self.title = tk.Label(self.upperFrame, text="Mackenzie Bot Auctions", pady = 15)
        self.title.pack()
        self.footer = tk.Label(self.lowerFrame, text="Mackenzie Auctions Bot Built By Jeffrey and Bartek", pady = 15)
        self.footer.pack()
        self.allLabels.extend((self.title, self.footer))

    def getHtmlFile(self):
        return (initalBookParse.initialBookParse(self.fileName))

def main(): 
    root = tk.Tk()
    w = '600'
    h = '300'
    root.geometry('{}x{}'.format(w, h))

    background_image=tk.PhotoImage(file = "background.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    launcher(root)
    root.mainloop()

if __name__ == '__main__':
    main()