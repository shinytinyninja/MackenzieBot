import tkinter as tk
import initalBookParse as bp
import time
from datetime import datetime
from pytz import timezone

class launcher (tk.Frame):
    all_buttons = []
    all_labels = []
    all_textentrys = []
    file_name = ""

    # curr_zone = timezone('EST')
    # curr_time = datetime.now(curr_zone)

# Funcstions used universially used functions by all three sub-menu's.
#---------------------------------------------------------------------------------------------------------
    def __init__(self, master):
        self.master = master
        self.display_menu()
    
    # Clears the screen of all elements
    def clear_screen(self):
        for label in self.all_labels:
            label.destroy()

        for button in self.all_buttons:
            button.destroy()

        for text in self.all_textentrys:
            text.destroy()

    # Displays a menu bar used for naviation and saving work
    def menu_bar(self):
        self.master.title("Simple menu")

        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        fileMenu = tk.Menu(menu_bar)
        fileMenu.add_command(label="Forward")
        fileMenu.add_command(label="Backward")
        menu_bar.add_cascade(label="Movement", menu=fileMenu)

    # Displays the title and footer notes
    def display_format(self):
        self.title = tk.Label(self.master, text="Mackenzie Bot Auctions")
        self.title.grid(row=0,column=1)

        self.footer = tk.Label(self.master, text="Mackenzie Auctions Bot Built By Jeffrey and Bartek")
        self.footer.grid(row=3,column=1)

    def exit_program(self):
        self.master.destroy()

# Main menu presented to the user upon launching the program.
#---------------------------------------------------------------------------------------------------------
    def display_menu(self):
        self.clear_screen()
        self.display_format()

        self.start_button = tk.Button(self.master, text="Start New Session", pady=10,command=self.display_start_new_menu)
        self.start_button.config(height = 3)
        self.start_button.grid(row=2, column=0, sticky = tk.EW)
        
        self.continue_button = tk.Button(self.master,text="Continue Last Session", pady=10, command=self.display_continue_menu)
        self.continue_button.config(height = 3)
        self.continue_button.grid(row=2, column=1, sticky = tk.EW)

        self.quick_button = tk.Button(self.master,text="Display Alerts", pady = 10, command=self.display_alert)
        self.quick_button.config(height = 3)
        self.quick_button.grid(row=2, column=2, sticky = tk.EW)

        self.all_buttons.extend((self.start_button, self.continue_button, self.quick_button))

# Sub menu; start fresh and use new html data.
#---------------------------------------------------------------------------------------------------------
    def display_start_new_menu(self):
        self.clear_screen()
        self.display_format()
        self.data_entryframe = tk.Frame(self.master)
        self.data_entryframe.grid(row = 1, column = 1, sticky=tk.EW)
        
        self.instructions = tk.Label(self.data_entryframe, text="Enter HTML File Name")
        self.file_entry = tk.Entry(self.data_entryframe)

        self.status = tk.Label(self.data_entryframe, text = " ")
        
        self.entr_button = tk.Button(self.data_entryframe, text="Enter", command=self.submitInfo)
        
        self.v_all = tk.Button(self.data_entryframe, text="View All HTML Files", command=self.displayAllHtmlFiles)
        
        self.all_labels.append(self.status)
        self.all_buttons.extend((self.entr_button, self.v_all))
        self.all_textentrys.append(self.file_entry)

        self.instructions.pack()
        self.file_entry.pack()
        self.status.pack()
        self.entr_button.pack()
        self.v_all.pack()
        self.master.bind('<Return>', self.enterSubmitInfo)

    def enterSubmitInfo(self, event):
        print("working")
        self.submitInfo()
    
    def submitInfo(self):
        self.file_name = str(self.file_entry.get())
        try:
            self.status.config(text = "Searching for file", bg = "green")
            self.master.update()
            bp.initialBookParse(self.file_name).get_list()
        except OSError:
            time.sleep(1)
            self.status.config(text = "Error", bg = "red")
            self.file_name = ""
        else:
            time.sleep(1)
            self.status.config(text = "Success", bg = "green")


    def displayAllHtmlFiles(self):
        self.display_format()

        self.all_html_file_names = bp.initialBookParse(self.file_name).search_for()
        self.all_visible_files = tk.Listbox(self.master, height = 3)
        
        for name in self.all_html_file_names:
            self.all_visible_files.insert(tk.END, str(name))
        
        self.all_visible_files.grid(row=2, column=1, sticky = tk.NSEW)

    def get_html_file(self):
        return (bp.initialBookParse(self.file_name).get_list())

# Sub menu; continue last session.
#---------------------------------------------------------------------------------------------------------
    def display_continue_menu(self):
        self.exit_program()

# Sub menu; display any significant price increases defined by the user.
#---------------------------------------------------------------------------------------------------------   
    def display_alert(self):
        self.exit_program()

# Main function; initializes the root view and sets up grid weights.
#---------------------------------------------------------------------------------------------------------   
def main(): 
    root = tk.Tk()
    w = '700'
    h = '400'
    root.geometry('{}x{}'.format(w, h))

    background_image=tk.PhotoImage(file = "background.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)

    launcher(root)
    root.mainloop()

if __name__ == '__main__':
    main()