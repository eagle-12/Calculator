import ttk
from Tkinter import *
class Calculator:
	calc_value=0.0#last value stored
	
	#keeps a track of last math function called by user
	div=False
	mul=False
	sub=False
	add=False
	
	
	def button_press(self,value):
		
		entry_val=self.number_entry.get()
		entry_val += value
		self.number_entry.delete(0,"end")
		self.number_entry.insert(0,entry_val)
		#print float(self.entry_value.get())
	
	def isfloat(self,strv):
		try:
	            float(strv)
	            
	            return True
	            
	        except ValueError:
	        	return False
	        	     
	def mbutton_press(self,value):
		
		if self.isfloat(str(self.number_entry.get())):
				self.div=False
				self.mul=False
				self.sub=False
				self.add=False
				
				self.calc_value = float(self.entry_value.get())
				print self.calc_value
				if value=='/':
					self.div=True
			        
			        elif value=='*':
					self.mul=True
					
				elif value=='-':
					self.sub=True
					
				elif value=='+':
					self.add=True	
				
				#to clear number_entry once math operation has been entered	
				self.number_entry.delete(0,"end")
	
	def equalbutton_press(self):
		if self.add==True or self.sub==True or 	self.mul==True or self.div==True:
			if self.add==True:
				ans=self.calc_value + float(self.entry_value.get())
			
			elif self.sub==True:
				ans=self.calc_value - float(self.entry_value.get())
			
			elif self.mul==True:
				ans=self.calc_value * float(self.entry_value.get())
							
			elif self.div==True:
				ans=(self.calc_value / float(self.entry_value.get()))
			print ans
			self.number_entry.delete(0,"end")
			
			self.number_entry.insert(0,ans)			
	
	
	def __init__(self,root):
		
		self.entry_value = StringVar(root,value="")
		root.title("Calc")
		root.geometry("565x240")
		root.resizable(width=False, height=False)
		
		style = ttk.Style()
		style.configure("TButton",font="Serif 15",padding=10)
		style.configure("TEntry",font="Serif 18",padding=10)
		
		self.number_entry = ttk.Entry(root,textvariable=self.entry_value,width=50)
		self.number_entry.grid(row=0,columnspan=4)#used when we have to change value again
		
		#1st row of buttons
		self.b7=ttk.Button(root,text="7",command=lambda: self.button_press("7")).grid(row=1,column=0)
		self.b8=ttk.Button(root,text="8",command=lambda: self.button_press("8")).grid(row=1,column=1)
		self.b9=ttk.Button(root,text="9",command=lambda: self.button_press("9")).grid(row=1,column=2)
		self.bdiv=ttk.Button(root,text="/",command=lambda: self.mbutton_press("/")).grid(row=1,column=3)
		
		#2nd row of buttons
		self.b4=ttk.Button(root,text="4",command=lambda: self.button_press("4")).grid(row=2,column=0)
		self.b5=ttk.Button(root,text="5",command=lambda: self.button_press("5")).grid(row=2,column=1)
		self.b6=ttk.Button(root,text="6",command=lambda: self.button_press("6")).grid(row=2,column=2)
		self.bmul=ttk.Button(root,text="*",command=lambda: self.mbutton_press("*")).grid(row=2,column=3)
		
		#3rd row of buttons
		self.b1=ttk.Button(root,text="1",command=lambda: self.button_press("1")).grid(row=3,column=0)
		self.b2=ttk.Button(root,text="2",command=lambda: self.button_press("2")).grid(row=3,column=1)
		self.b3=ttk.Button(root,text="3",command=lambda: self.button_press("3")).grid(row=3,column=2)
		self.bsub=ttk.Button(root,text="-",command=lambda: self.mbutton_press("-")).grid(row=3,column=3)
		
		#4th row of buttons
		self.bclear=ttk.Button(root,text="AC",command=lambda: self.button_press("AC")).grid(row=4,column=0)
		self.b0=ttk.Button(root,text="0",command=lambda: self.button_press("0")).grid(row=4,column=1)
		self.bequal=ttk.Button(root,text="=",command=lambda: self.equalbutton_press()).grid(row=4,column=2)
		self.badd=ttk.Button(root,text="+",command=lambda: self.mbutton_press("+")).grid(row=4,column=3)
		
		
				
root =Tk()

calc=Calculator(root)
		
root.mainloop()		
