"""
Title : GST Yearly Integrator

Team WIZARDSs
Group Info

   Name 				   Roll no.
1. Prathmesh Patil			A45
2. Kshitij Sangar			A52
3. Ruturaj Sankpal			A54
4. Shailesh Mohite			A55

"""


import eel
import tkinter as tk
from tkinter import filedialog, Tk
import os
import time
import Backend


eel.init('static')
Final_filename = 'NONE'
Final_foldername = 'NONE'
@eel.expose
def browsefile():
    global Final_filename
    Final_filename = fileOpen()
    print(Final_filename)
    return Final_filename

@eel.expose
def browsefolder():
    global Final_foldername
    Final_foldername = folderOpen()
    print("\n\n\n Folder" + Final_foldername)
    return Final_foldername

def fileOpen():
    root = tk.Tk()
    #root.withdraw()
    filename = filedialog.askopenfilename(initialdir= Final_foldername + '/', title="Select File", filetypes=(
        ("Excel files", "*.xlsx"), ("Image file", "*.jpg"), ("Image file", "*.jpeg"), ("Image file", "*.png"),
        ("all files", "*.*")))
    return str(filename)

def folderOpen():
    root = tk.Tk()
    #root.withdraw()
    foldername = filedialog.askdirectory(title="Select Folder")
    return str(foldername)

@eel.expose
def files(mainFile):
    l = []
    l = mainFile
    print("\n\n\n File : " + mainFile + "\n\n\n\n")
    Backend.backend(l)

@eel.expose
def RunBackend():
    print("\n\n Folder = " + Final_foldername)
    print("\n File = " + Final_filename)
    Backend.backend(Final_foldername, Final_filename)
eel.start('Home.html')

