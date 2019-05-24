"""
Jacky Chen
TDQ User Interface Executable Instructions
1. Users specify the data file to be read by clicking the 'Open file' button and selecting the data file. (required)
2. Users specify the target file name and location by clicking 'Save as...'. (required)
3. Users specify the delimiter in the entry box. (required)
4. Users select the constraints for the TDQ constraints file (Constraints can be left blank). (optional)
5. Once all inputs have been entered the user will click 'Generate' to create the targetfile in the designated path.
6. Users can then select Clear to reset all fields and generate another file.

"""
## Import all widgets necessary  for app
from tkinter import filedialog, Frame, Label, Button, Text, Tk, Checkbutton, StringVar, messagebox, END, ttk     #ttk is used for styling
from tkinter import TOP, W, E, X   #Import all config properties for positioning and formatting widgets
import TDQ_CONFIG_GENERATORv2 as tdq

class Application(Frame):
    ## Opens file box to search for the data file
    def input_file_path(self):
        filetype = [("Excel File", "*.csv")]
        self.input_filename = filedialog.askopenfilename(initialdir = "/Documents", 
                                                        title = "Open File", 
                                                        filetypes = filetype)
        if len(self.input_filename) > 0:
            self.input_path["text"] = self.input_filename[:30] + "..."
        else:
            self.input_path = "Select data file"
            
    ## Opens file box to create the new file name and where to Save as.
    def output_file_path(self):
        filetype = [("JSON File", ".json")]
        self.output_filename = filedialog.asksaveasfilename(initialdir = "/Documents", 
                                                        title = "File Save",
                                                        filetypes = filetype, defaultextension=".json")
        if len(self.output_filename) > 0:    
            self.output_path["text"] = str(self.output_filename)
        else:
            self.output_path = "Select output file path"

    ## Function to clear all inputs once the 'Clear' butotn is clicked
    def clearselection(self):
        self.input_filename = ""
        self.output_filename = ""
        self.delimiter_box.delete(0, END)
        self.input_path["text"] = "Select data file"
        self.output_path["text"] = "Select output file path"
        self.var1.set("")
        self.var2.set("")
        self.var3.set("")
        self.var4.set("")
        self.var5.set("")
        self.var6.set("")
        self.var7.set("")
        self.var8.set("")
        self.var9.set("")
    
    ## Changes the 'Generate' button to 'Processing...' until the constraints file is produced to let the user know the file is being created
    def generate_btn(self):
        self.generate_btn["text"] = ["Processing..."]
        self.generate_btn.after(100, self.generate)
    
    ## Actions to run once the user clicks 'Generate' 
    def generate(self):
        ## Dictionary to convert the constraint names to what's required by the TDQ_CONFIG_GENERATOR script
        constraints_dict = {
            'datatype': 'type',
            'min': 'min',
            'max': 'max',
            'min_length': 'min_length',
            'max_length': 'max_length',
            'sign': 'sign',
            'nullable': 'max_nulls',
            'listofvalues': 'allowed_values' ,
            'duplicate_check': 'no_duplicates',
            'rex': 'rex'
            }
        ## Constraints to be produced in JSON constraints file  
        constraints_list = []
        for constraints in self.varlist:
            for key, value in constraints_dict.items():
                if constraints.get() == key:
                    constraints_list.append(value)
        
        ## Setting variables to be read in by TDQ_CONFIG_GENERATOR.py script to produce the constraints file
        if self.input_path["text"] != "Select data file":
            filename = self.input_filename
        
        if self.output_path["text"] != "Select output file path":
            targetfile = self.output_filename

        if len(self.delimiter_box.get()) > 0:
            delimiter = self.delimiter_box.get()
        
        ## Success message once file has been created and also error message if inputs are missing 
        try:
            tdq.run(filename, targetfile, delimiter, constraints_list)
            messagebox.showinfo("Success", "Document generation successful.")
        except Exception as error:
            messagebox.showinfo("Error", "Inputs still required.")
        self.generate_btn["text"] = "Generate"

    def createWidgets(self, master=None):
        ## Vertical and horizontal gaps in pixels between widgets of the GUI grid
        v_gaps = 25  
        h_gaps = 40

        ## Create a main frame within the master window for the widgets
        self.main_frame = Frame(self)
        self.main_frame.pack(side = TOP, fill=X, padx = 20, pady = 30) # Padding between widgets and edge of the window

        ## Frame for input file selection and input file path within main frame
        self.input_subframe = Frame(self.main_frame)
        self.input_subframe.grid(pady = (0,v_gaps), row = 1, column = 0, sticky = W)
        ## Create a button to select the input file to be read 
        self.open_file_btn = ttk.Button(self.input_subframe, text = "Open file", command = self.input_file_path)
        self.open_file_btn.grid(row = 0, column = 0, sticky = W)
        ## Create a box for the input file path 
        self.input_path = Label(self.input_subframe, text = "Select data file", font = "Calibri 10")
        self.input_path.grid(padx = (h_gaps, 0), row = 0, column = 1, sticky = W)

        ## Frame for user to type in output file name
        self.output_subframe = Frame(self.main_frame)
        self.output_subframe.grid(pady = (0,v_gaps), row = 2, column = 0, sticky = W)
        ## Create a button for the user to designate the path the output file will be saved 
        self.output_file_btn = ttk.Button(self.output_subframe, text = "Save as...",
                                                                command = self.output_file_path)
        self.output_file_btn.grid(row = 0, column = 0, sticky = W)
        ## Create a label for the user to define output file name
        self.output_path = Label(self.output_subframe, text = "Select output file path", font = "Calibri 10")
        self.output_path.grid(padx = (h_gaps, 0), row = 0, column = 1, sticky = W)

        ## Frame for the user to specify the delimiter
        self.delimiter_subframe = Frame(self.main_frame)
        self.delimiter_subframe.grid(pady = (0, 10), row = 3 , column = 0, stick = W)
        ## Create a label for Delimiter 
        self.delimiter_label= Label(self.delimiter_subframe, text = "Delimiter:", font = "Calibri 10 bold")
        self.delimiter_label.grid(row = 0, column = 0, sticky = W)
        ## Create a box for the user to specify the delimiter
        self.delimiter_box = ttk.Entry(self.delimiter_subframe, width = 5, justify = 'center')
        self.delimiter_box.grid(padx = (54, 0), row = 0, column = 1, sticky = W)
        ## Create a help label for Delimiter
        self.delimiter_help = Label(self.delimiter_subframe, text = 'Help: Do not specify delimiter between ""', font = "Calibri 10 bold")
        self.delimiter_help.grid(padx = (51,0), row = 1, column = 1, sticky = W)

        ## Frame for Constraints checkbox 
        self.constraints_subframe = Frame(self.main_frame)
        self.constraints_subframe.grid(pady = (0, v_gaps), row = 4, column = 0, stick = W)
        ## Create a label for Constraints
        self.constraints_label = Label(self.constraints_subframe, text = "Constraints:", font = "Calibri 10 bold")
        self.constraints_label.grid(row = 0, column = 0, sticky = W)
        ## Create checkboxes for the user to select constraints
        self.var1 = StringVar()
        self.check_btn_1 = Checkbutton(self.constraints_subframe, text = "datatype", variable = self.var1, onvalue = "datatype", offvalue ="")
        self.check_btn_1.grid(padx = (42,0), row= 0 , column = 1, stick = W)
        self.var2 = StringVar()
        self.check_btn_2 = Checkbutton(self.constraints_subframe, text = "listofvalues", variable = self.var2, onvalue = "listofvalues", offvalue ="")
        self.check_btn_2.grid(padx = (42,0), row= 1 , column = 1, stick = W)
        self.var3 = StringVar()
        self.check_btn_3 = Checkbutton(self.constraints_subframe, text = "min_length", variable = self.var3, onvalue = "min_length", offvalue ="")
        self.check_btn_3.grid(padx = (42,0), row= 2 , column = 1, stick = W)
        self.var4 = StringVar()
        self.check_btn_4 = Checkbutton(self.constraints_subframe, text = "max_length", variable = self.var4, onvalue = "max_length", offvalue ="")
        self.check_btn_4.grid(padx = (42,0), row= 3 , column = 1, stick = W)
        self.var5 = StringVar()
        self.check_btn_5 = Checkbutton(self.constraints_subframe, text = "nullable", variable = self.var5, onvalue = "nullable", offvalue ="")
        self.check_btn_5.grid(padx = (42,0), row= 4 , column = 1, stick = W)
        self.var6 = StringVar()
        self.check_btn_6 = Checkbutton(self.constraints_subframe, text = "min", variable = self.var6, onvalue = "min", offvalue ="")
        self.check_btn_6.grid(padx = (42,0), row= 5 , column = 1, stick = W)
        self.var7 = StringVar()
        self.check_btn_7 = Checkbutton(self.constraints_subframe, text = "max", variable = self.var7, onvalue = "max", offvalue ="")
        self.check_btn_7.grid(padx = (42,0), row= 6 , column = 1, stick = W)
        self.var8 = StringVar()
        self.check_btn_8 = Checkbutton(self.constraints_subframe, text = "sign", variable = self.var8, onvalue = "sign", offvalue ="")
        self.check_btn_8.grid(padx = (42,0), row= 7 , column = 1, stick = W)
        self.var9 = StringVar()
        self.check_btn_9 = Checkbutton(self.constraints_subframe, text = "duplicate_check", variable = self.var9, onvalue = "duplicate_check", offvalue ="")
        self.check_btn_9.grid(padx = (42,0), row= 8 , column = 1, stick = W)
        self.varlist.append(self.var1)
        self.varlist.append(self.var2)
        self.varlist.append(self.var3)
        self.varlist.append(self.var4)
        self.varlist.append(self.var5)
        self.varlist.append(self.var6)
        self.varlist.append(self.var7)
        self.varlist.append(self.var8)
        self.varlist.append(self.var9)
        
        ## Frame for Clear and Generate buttons
        self.generate_btn_subframe = Frame(self.main_frame)
        self.generate_btn_subframe.grid(pady = (0,0), row = 5, column = 0, sticky = E)
        self.generate_btn = ttk.Button(self.generate_btn_subframe, text = "Generate", command = self.generate_btn)
        self.generate_btn.grid(padx = 10, row = 0, column = 1, sticky = W)
        self.clear_btn = ttk.Button(self.generate_btn_subframe, text = "Clear", command = self.clearselection)
        self.clear_btn.grid(row = 0, column = 0, sticky = W )


    ## Create widgets
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.varlist = []
        self.pack()
        self.createWidgets(master)


root = Tk() # creating a blank window 
root.resizable(False, False)
app = Application(master=root)
app.master.title("TDQ Generator")
app.mainloop()