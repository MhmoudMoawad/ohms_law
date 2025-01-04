import os
import sys
import customtkinter as ctk


os.environ['TCL_LIBRARY'] = r'c:/Users/moawa/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = r'c:/Users/moawa/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'
#
#=======================================================================================================
#
class WinApp(ctk.CTk):
    # class to create windows with list of options
    def __init__(self, win_title:str, call_back_fn:any, win_size:str = '640x240' )-> None:
        super().__init__()
        #
        self.option_selected  = -1
        self.title(win_title)
        self.geometry(win_size)
        self.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
        
        self.OPTION_VOLTAGE    = 1    # 1. Voltage
        self.OPTION_CURRENT    = 2    # 2. Current
        self.OPTION_RESISTANCE = 3    # 3. Resistance
        self.OPTION_EXIT       = 0    # 0. Exit
        #
        # Create user interface widgets
        self.lbl_header       = ctk.CTkLabel      (self, text="Electrical Calculator:",width=20, height=2,   font=("verdana", 24))
        self.rb_voltage       = ctk.CTkRadioButton(self, text="Voltage",     font=("verdana", 14), command=self.rb_voltage_callback)
        self.rb_current       = ctk.CTkRadioButton(self, text="Current",     font=("verdana", 14), command=self.rb_current_callback)
        self.rb_resistance    = ctk.CTkRadioButton(self, text="Resistance",  font=("verdana", 14), command=self.rb_resistance_callback)
        self.rb_exit          = ctk.CTkRadioButton(self, text="Exit",        font=("verdana", 14), command=self.rb_exit_callback)
        self.btn_run          = ctk.CTkButton     (self, text="Run",width=150, height=30, font=("verdana", 14, 'bold'), command=self.btn_run_callback)    
        self.lbl_status_bar   = ctk.CTkLabel      (self, text="",     font=("verdana", 14))
        
        self.input1    = ctk.CTkTextbox    (self,  width=50, height=15, font=("verdana", 14), border_width=2)
        self.input2     = ctk.CTkTextbox    (self, width=50, height=15, font=("verdana", 14), border_width=2)
        self.input3     = ctk.CTkTextbox    (self, width=50, height=15, font=("verdana", 14), border_width=2)
        self.input1_lbl = ctk.CTkLabel(self, width=50, text="",     font=("verdana", 14))
        self.input2_lbl = ctk.CTkLabel(self, width=50, text="",     font=("verdana", 14))
        self.input3_lbl = ctk.CTkLabel(self, width=50, text="",     font=("verdana", 14))
        #
        self.gui_elements = [
                               {"type":"RadioButton", "element":self.rb_voltage ,    "CallBack":self.rb_voltage_callback,    "desc":"Given Curent and Resistance calculate Voltage"}
                              ,{"type":"RadioButton", "element":self.rb_current ,    "CallBack":self.rb_current_callback,    "desc":"Given Voltage and Resistance calculate Current"}
                              ,{"type":"RadioButton", "element":self.rb_resistance , "CallBack":self.rb_resistance_callback, "desc":"Given Voltage and Current Calculate Resistance"}
                              ,{"type":"RadioButton", "element":self.rb_exit ,       "CallBack":self.rb_exit_callback,       "desc":"Exit program"}
        ]
        #
        # configure windows grid (one column and 7 rows)
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
        #
        # place widgets on the grid
        self.lbl_header.grid      (row=0, column=0, padx=10, pady= 5, sticky="w", columnspan=7 )
        self.rb_voltage.grid      (row=1, column=0, padx=30, pady= 5, sticky="w") 
        self.rb_current.grid      (row=2, column=0, padx=30, pady= 5, sticky="w") 
        self.rb_resistance.grid   (row=3, column=0, padx=30, pady= 5, sticky="w")
        self.rb_exit.grid         (row=4, column=0, padx=30, pady= 5, sticky="w")    
        self.btn_run.grid         (row=5, column=0, padx=10, pady=10, sticky="", columnspan=7) 
        self.lbl_status_bar.grid  (row=6, column=0, padx=5,  pady= 5, sticky="ew", rowspan=1, columnspan=7)    

    #
    # --------------------------------------------------------------------------------------------------
    #
    def display_text_input(self, row:int, caption:any):
        if self.option_selected != -1:
            self.input1.grid_forget()   
            self.input2.grid_forget()
            self.input3.grid_forget()
            self.input1_lbl.grid_forget()
            self.input2_lbl.grid_forget()
            self.input3_lbl.grid_forget()
        
        if row > 0:
            self.input1.grid (row=row, column=2, padx=10, pady= 5, sticky="w")   
            self.input2.grid (row=row, column=4, padx=10, pady= 5, sticky="w")
            self.input3.grid (row=row, column=6, padx=10, pady= 5, sticky="w")    

            if len(caption) > 0:            
                self.input1_lbl.configure(text=caption[0])
                self.input2_lbl.configure(text=caption[1])
                self.input3_lbl.configure(text=caption[2])
                
                self.input1_lbl.grid (row=row, column=1, padx=5, pady= 5, sticky="w")
                self.input2_lbl.grid (row=row, column=3, padx=5, pady= 5, sticky="w")  
                self.input3_lbl.grid (row=row, column=5, padx=5, pady= 5, sticky="w")
    #
    # --------------------------------------------------------------------------------------------------
    #
    def rb_voltage_callback(self):
        # TODO: [] rb_select_deselct add function dscription
        #
        widget = self.rb_voltage
        widget_text = widget.cget("text")
        #
        self.option_selected = self.OPTION_VOLTAGE
        self.rb_select_deselct(widget_text,self.gui_elements )
        self.btn_run.configure(text= 'Calculate Voltage')
        # display input text widgets
        self.display_text_input(row=1, caption=['Current', '* Resistance', '= Voltage'])
        
    #
    # --------------------------------------------------------------------------------------------------
    #
    def rb_current_callback(self):
        # TODO: [] rb_select_deselct add function dscription
        #
        widget = self.rb_current
        widget_text = widget.cget("text")
        #
        self.option_selected = self.OPTION_CURRENT
        self.rb_select_deselct(widget_text,self.gui_elements ) 
        self.btn_run.configure(text= 'Calculate Current')
        self.display_text_input(row=2, caption=['Voltage', '/ Resistance', '= Current'])
    #
    # --------------------------------------------------------------------------------------------------
    #
    def rb_resistance_callback(self):
        # TODO: [] rb_select_deselct add function dscription
        #
        widget = self.rb_resistance
        widget_text = widget.cget("text")
        #
        self.option_selected = self.OPTION_RESISTANCE
        self.rb_select_deselct(widget_text,self.gui_elements )
        self.btn_run.configure(text= 'Calculate Resistance')
        self.display_text_input(row=3, caption=['Voltage', '/ Current','= Resistance'])
        #
    # --------------------------------------------------------------------------------------------------
    #
    def rb_exit_callback(self):
        # TODO: [] rb_select_deselct add function dscription
        #
        widget = self.rb_exit
        widget_text = widget.cget("text")
        #
        self.option_selected = self.OPTION_EXIT
        self.rb_select_deselct(widget_text,self.gui_elements )
        self.display_text_input(row=0, caption=[])
        self.btn_run.configure(text= 'Exit!')
    # --------------------------------------------------------------------------------------------------
    #
    def btn_run_callback(self):
        match self.option_selected:
            case self.OPTION_VOLTAGE:
                ...
            case self.OPTION_CURRENT:   
                ...
            case self.OPTION_RESISTANCE:
                ...
            case self.OPTION_EXIT:
                sys.exit()     
        #
    #----------------------------------------------------------------------------------------------------------------
    #
    def rb_select_deselct(self, widget_text:str, all_widegets:any)-> None:
        # TODO: [] rb_select_deselct add function dscription
        #
        for item in all_widegets:
            if widget_text == item["element"].cget("text"):
                self.lbl_status_bar.configure(text= item["desc"])
            else:
                item["element"].deselect()