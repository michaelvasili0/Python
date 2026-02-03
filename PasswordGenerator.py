# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Michael Vasilio
# Created Date: 3/12/22
# version ='0.0.2'
# ---------------------------------------------------------------------------

from customtkinter import CTk  # External Libraries
from customtkinter import CTkButton
from customtkinter import CTkLabel
from customtkinter import CTkSwitch
from customtkinter import CTkComboBox
from customtkinter import CTkFrame
from customtkinter import CTkEntry

from tkinter import Menu

from customtkinter import set_appearance_mode
from customtkinter import set_default_color_theme

from customtkinter import INSERT

from customtkinter import TOP
from customtkinter import LEFT
from customtkinter import RIGHT

from customtkinter import CENTER
from customtkinter import SW
from customtkinter import SE

from tkinter import messagebox

from string import digits  # Standard Libraries
from string import ascii_uppercase
from string import ascii_lowercase

from pyperclip import copy

import random

__author__ = "Michael Vasilio"
__copyright__ = "Copyright 2022, The Basic Project"
__credits__ = ["Michael Vasilio"]
__license__ = "GPL"
__version__ = "0.0.2"
__maintainer__ = "Michael Vasilio"
__email__ = "N/A"
__status__ = "Development"

# Variables
passwordLength = 7
symbols_basic = "&%$#@"
symbols_complex = "/.,<>;:][}{=+-)(*!"

use_upperON = False
use_lowerON = False
use_digitsON = False
use_symbolsBON = False
use_symbolsCON = False


# If the uppercase switch is enabled
def determineUpper():
    """Function will turn on and off uppercase."""
    global use_upperON

    if use_upperON:
        use_upperON = False
    else:
        use_upperON = True


# If the lowercase switch is enabled
def determineLower():
    """Function will turn on and off lowercase."""
    global use_lowerON

    if use_lowerON:
        use_lowerON = False
    else:
        use_lowerON = True


# If the digit switch is enabled
def determineDigits():
    """Function will turn on and off digits."""
    global use_digitsON

    if use_digitsON:
        use_digitsON = False
    else:
        use_digitsON = True


# If the symbols switch is enabled
def determineSymbolsB():
    """Function will turn on and off symbols."""
    global use_symbolsBON

    if use_symbolsBON:
        use_symbolsBON = False
    else:
        use_symbolsBON = True


# If the symbols switch is enabled
def determineSymbolsC():
    """Function will turn on and off symbols."""
    global use_symbolsCON

    if use_symbolsCON:
        use_symbolsCON = False
    else:
        use_symbolsCON = True


# Set the look and feel of window
set_appearance_mode("dark")
set_default_color_theme("green")

# Create a window
window = CTk()
window.geometry("600x400")
window.resizable(False, False)
window.title("Password Generator")


# Function that will generate the password
def generatePassword():
    """Function will generate the password, based on selected criteria."""
    dig = ""
    sym_basic = ""
    sym_complex = ""
    upp = ""
    low = ""

    if use_upperON:
        upp = ascii_uppercase

    if use_lowerON:
        low = ascii_lowercase

    if use_digitsON:
        dig = digits

    if use_symbolsBON:
        sym_basic = symbols_basic

    if use_symbolsCON:
        sym_complex = symbols_complex

    # This is the main logic for the function.
    try:
        # Clear the text field
        entry.delete(0, 'end')
        # Set the password , based on selected attributes
        password = "".join(random.choices(upp + sym_complex + low + dig + sym_basic, k=int(dropMenu.get())))
        # Insert the password into the text field
        entry.insert(INSERT, password)
    except IndexError:
        messagebox.showerror("Generator Error!", "You need to select valid options for the password.")


# Create a Left pane
frame_left = CTkFrame(master=window, width=100)
frame_left.pack(padx=5, pady=5, fill="both", expand=True)

# Create a label
label_1 = CTkLabel(master=frame_left, text_font="Roboto, 23", text="Password Generator")
label_1.pack(padx=5, pady=15, expand=True)

# Create a textarea
entry = CTkEntry(master=frame_left, text_font="Roboto", width=300, height=35, text_color="white")
entry.pack(padx=5, pady=30, side=TOP)

# Create Radio button for upper case inclusion
switch1 = CTkSwitch(master=frame_left, text_font="Roboto", text="Upper Case ( {} )".format(ascii_uppercase),
                    button_color="grey", button_hover_color="white", fg_color="red", command=determineUpper)
switch1.toggle()
switch1.pack(padx=10, pady=2, anchor=CENTER)

# Create Radio button for lower case inclusion
switch2 = CTkSwitch(master=frame_left, text_font="Roboto", text="Lower Case ( {} )".format(ascii_lowercase),
                    button_color="grey", button_hover_color="white", fg_color="red", command=determineLower)
switch2.toggle()
switch2.pack(padx=10, pady=2, anchor=CENTER)

# Create Radio button for digits case inclusion
switch3 = CTkSwitch(master=frame_left, text_font="Roboto", text="Numbers ( {} )".format(digits), button_color="grey",
                    button_hover_color="white", fg_color="red", command=determineDigits)
switch3.toggle()
switch3.pack(padx=10, pady=2, anchor=CENTER)

# Create Radio button for basic symbols case inclusion
switch4 = CTkSwitch(master=frame_left, text_font="Roboto", text="Basic Symbols ( {} )".format(symbols_basic),
                    button_color="grey", button_hover_color="white", fg_color="red", command=determineSymbolsB)
switch4.toggle()
switch4.pack(padx=10, pady=2, anchor=CENTER)

# Create Radio button for complex symbols case inclusion
switch5 = CTkSwitch(master=frame_left, text_font="Roboto", text="Adv Symbols ( {} )".format(symbols_complex),
                    button_color="grey", button_hover_color="white", fg_color="red", command=determineSymbolsC)
switch5.pack(padx=10, pady=2, anchor=CENTER)

# Drop down context menu items (replace this later)
v = ["7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
dropMenu = CTkComboBox(master=frame_left, values=v, width=70, text_font="Roboto, 15", button_hover_color="red",
                       dropdown_hover_color="red")
dropMenu.set("10")
dropMenu.pack(padx=10, pady=10, side=LEFT, anchor=SW)

# Create a button
button1 = CTkButton(master=frame_left, text_font="Roboto", text="Generate", width=200, height=55,
                    command=generatePassword, fg_color="grey", hover_color="red")
button1.pack(padx=10, pady=10, expand=True, side=RIGHT, anchor=SE)


def copy_password():
    copy(entry.get())


def clear_password():
    # Clear the text field
    entry.delete(0, 'end')


# Create a context menu
m = Menu(master=window, tearoff=0)
m.add_command(label="Copy", command=copy_password)
m.add_command(label="Clear", command=clear_password)


# Handles when the context menu will pop up
def create_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


# Set the context menu to be only used when you right-click the entry field
entry.bind("<Button-3>", create_popup)

# Main Game Loop
if __name__ == "__main__":
    window.mainloop()
