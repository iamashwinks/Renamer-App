import tkinter as tk
from tkinter import filedialog
import os


class FilesRenamer(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.geometry("380x300+10+10")
		self.select = tk.Button(self, text="Choose Folder", command=self.on_choose)
		self.save = tk.Button(self, text="Save to Folder", command=self.on_save)
		self.rename = tk.Button(self, text="Rename", command=self.rename)
		self.tb1 = tk.Text(self, width=30, height=1)
		self.tb2 = tk.Text(self, width=30, height=1)
		self.tb3 = tk.Text(self, width=45, height=10)
		
		# PACKING ELEMENTS INTO GRID
		self.select.grid(column=0, row=0)
		self.save.grid(column=0, row=1)
		self.tb1.grid(column=1, row=0)
		self.tb2.grid(column=1, row=1)
		self.tb3.grid(column=0, row=2, columnspan=2, sticky="NSEW", padx=5, pady=10)
		self.rename.grid(column=1, row=3)

	def on_choose(self):
		self.from_dir = filedialog.askdirectory() + "/"
		self.tb1.insert('0.0',self.from_dir)

	
	def on_save(self):
		self.to_dir = filedialog.askdirectory() + "/"
		self.tb2.insert('0.0',self.to_dir)

	def rename(self):
		for i, image in enumerate(os.listdir(self.from_dir)):
		    if image.endswith('.png') | image.endswith('.jpg'):
		        self.tb3.insert(f"{i}.0", f"Renaming {image} to {i}.jpg\n")
		        os.rename(self.from_dir + image, self.to_dir + str(i) + ".jpg")


app = FilesRenamer()
app.mainloop()