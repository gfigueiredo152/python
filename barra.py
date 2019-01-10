import tkinter as tk
from tkinter import ttk

class SampleApp(tk.Tk):

 def _init_(self,*args,**kwargs):
 	tk.Tk._init_(self,*args,**kwargs)
 	self.button = ttk.Button(text="INICIO",command=self.start)
 	self.button.pack()
 	self.progress = ttk.progressbar(self,orient="horizontal",length=800,mode="determinate")
 	
 	self.progress.pack()
 	
 	self.bytes = 0
 	self.maxbytes = 0
 	
 def start(self):
 	self.progress ["value"]=0
 	self.maxbytes =50000
 	self.progress ["maximum"]=50000
 	self.read_bytes()
 
 def read_bytes(self):
 	self.bytes += 500
 	self.progress["value"]=self.bytes
 	
 	if self.bytes < self.maxbytes:
 		self.after(50,self.read_bytes)
 		
 		
app = SampleApp()
app.mainloop()