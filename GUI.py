import tkinter as tk
from tkinter import *
from CiperText import compress,decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir = '/', title= "Select a File")
    return filename


def compression(i,o):
    compress(i,o)
    
def decompression(i,o):
    decompress(i,o)
    
window = tk.Tk()

window.title("Compression Engine")
window.geometry("600x400")



compress_button = tk.Button(window, text= "Compress",command=lambda:compression(open_file(), "Cipher.txt"))
compress_button.grid(row=2,column=1)

decompress_button = tk.Button(window, text= "Decompress",command=lambda:decompression(open_file(), "Plaintext.txt"))
decompress_button.grid(row=2,column=4)





window.mainloop()