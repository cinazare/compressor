import tkinter as tk
from tkinter import filedialog
from encoder_decoder import decoder, encoder


root = tk.Tk()
root.geometry("800x500")
root.configure(background="lightblue")
root.title("file compressor")


title_in_root = tk.Label(
    root,
    text = "this is my file compressor",
    fg="black",
    background="lightblue",
    pady=30,
    font= ("arial", 30),
    
    ).place(x=180, y=25)

descrption = "you can choose a text file to be compressed, \n or a compressed file by this application to be decompressed. "
desc = tk.Label(
    root,
    text=descrption,
    font= ("arial", 12), 
    border=15,
    background="lightblue"
).place(x=180, y=125)

def import_txt():
    filepath = filedialog.askopenfile(mode='r', title='select a textfile to commpress', filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if filepath:
        encoder(filepath.name)
        print(filepath.name)
def import_bin():
    filepath = filedialog.askopenfile(mode='r', title='select a binfile to commpress', filetypes=[("bin files", "*.bin"), ("All files", "*.*")])
    
    if filepath:
        print(filepath.name)
        decoder(filepath.name)

de_compressor = tk.Button(
    root,
    activebackground = "#66d5ff",
    text = "decompress",
    font = ("arial", "15"),
    border = 4,
    width = 14,
    height = 6,
    highlightthickness = 5,
    highlightbackground = "gray",
    bg = "lightblue",
    command = lambda:import_bin()
    ).place(x=180,y=250)

compressor = tk.Button(
    root,
    activebackground = "#66d5ff",
    text = "compress",
    font = ("arial", "15"),
    border = 4,
    width = 14,
    height = 6,
    highlightthickness = 5,
    highlightbackground = "gray",
    bg = "lightblue",
    command = lambda:import_txt()
    ).place(x=430,y=250)


root.mainloop()