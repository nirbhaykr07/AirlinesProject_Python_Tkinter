import tkinter as tk
LARGE_FONT = ("Verdana", 12)

import sqlite3
import sys
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
 

class MainWindow(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title("Airlines reservation system") 
		self.geometry("700x500") 
 
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)   
		container.grid_columnconfigure(0,weight=1) 
		self.frames = {} 
 
		for F in (WelcomePage, SignInPage, SignUpPage, MenuPage, FlightPage, TicketsPage):
			frame = F(container, self) 
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
 
		self.show_frame(WelcomePage)
 
	def show_frame(self, name):
		frame = self.frames[name]
		frame.tkraise()
		

		
class WelcomePage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
 
		label = tk.Label(self, text="WELCOME TO THE AIRLINES RESERVATION SYSTEM", font=LARGE_FONT)
		label.grid(column=10,row=0)

		signInButton = tk.Button(self, text = "Sign In", command=lambda : controller.show_frame(SignInPage))
		signInButton.grid(column=10,row=2)

		signUpButton = tk.Button(self, text = "Sign Up", command=lambda : controller.show_frame(SignUpPage))
		signUpButton.grid(column=10,row=3)
		
		
class SignUpPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)		  
		
		label = tk.Label(self, text="AIRLINES RESERVATION SYSTEM - Sign Up", font=LARGE_FONT)
		label.grid(column=10,row=0)
		
		CustomerId		= tk.StringVar()
		FirstName		= tk.StringVar()
		LastName		= tk.StringVar()
		Dob				= tk.StringVar()
		Mobile			= tk.StringVar()
		Gender			= tk.StringVar()
		Address 		= tk.StringVar()
		Password 		= tk.StringVar()
		
		tk.Label(self, text="Customer Id: ").grid(row=4,column=9, sticky=tk.W)
		tk.Label(self, text="First Name: ").grid(row=5,column=9, sticky=tk.W)
		tk.Label(self, text="Last Name: ").grid(row=6,column=9, sticky=tk.W)
		tk.Label(self, text="Date of Birth: ").grid(row=7,column=9, sticky=tk.W)
		tk.Label(self, text="Mobile No.: ").grid(row=8,column=9, sticky=tk.W)
		tk.Label(self, text="Gender: ").grid(row=9,column=9, sticky=tk.W)
		tk.Label(self, text="Address: ").grid(row=10,column=9, sticky=tk.W)
		tk.Label(self, text="Password: ").grid(row=11,column=9, sticky=tk.W)
		
		entryCustomerId	= tk.Entry(self,  text = CustomerId)
		entryFirstName	= tk.Entry(self,  text = FirstName)
		entryLastName	= tk.Entry(self,  text = LastName)
		entryDob 		= DateEntry(self, width=17, background='darkblue', foreground='white', borderwidth=2, year=2019)
		entryMobile		= tk.Entry(self,  text = Mobile)
		entryGender 	= tk.Entry(self,  text = Gender)
		entryAddress 	= tk.Entry(self,  text = Address)
		entryPassword 	= tk.Entry(self,  text = Password, show="*")
		
		entryCustomerId.grid(row=4, column=10)
		entryFirstName.grid(row=5, column=10)
		entryLastName.grid(row=6, column=10)
		entryDob.grid(row=7, column=10)
		entryMobile.grid(row=8, column=10)
		entryGender.grid(row=9, column=10)
		entryAddress.grid(row=10, column=10)
		entryPassword.grid(row=11, column=10)
		
		def Ok():
	
			dataCustomerId 	= "{}".format(entryCustomerId.get())
			dataFirstName 	= "{}".format(entryFirstName.get())
			dataLastName 	= "{}".format(entryLastName.get())
			dataDob 		= "{}".format(entryDob.get())
			dataMobile 		= "{}".format(entryMobile.get())
			dataGender 		= "{}".format(entryGender.get())
			dataAddress 	= "{}".format(entryAddress.get())
			dataPassword 	= "{}".format(entryPassword.get())
			
			if(len(dataCustomerId) == 0):
				messagebox.showinfo('Validation Failed','Please enter Customer ID')
				return;
				
			if(len(dataFirstName) == 0):
				messagebox.showinfo('Validation Failed','Please enter First name')
				return;
				
			if(len(dataLastName) == 0):
				messagebox.showinfo('Validation Failed','Please enter Last name')
				return;
				
			if(len(dataDob) == 0):
				messagebox.showinfo('Validation Failed','Please enter DOB')
				return;
				
			if(len(dataMobile) == 0):
				messagebox.showinfo('Validation Failed','Please enter Mobile Number')
				return;
				
			if(len(dataGender) == 0):
				messagebox.showinfo('Validation Failed','Please enter Gender')
				return;
				
			if(len(dataAddress) == 0):
				messagebox.showinfo('Validation Failed','Please enter Address')
				return;
				
			if(len(dataPassword) == 0):
				messagebox.showinfo('Validation Failed','Please enter Password')
				return;
				
			data = (dataCustomerId,dataFirstName, dataLastName, dataDob, dataMobile, dataGender, dataAddress, dataPassword)
			
			conn= sqlite3.connect('test2.db')
			cur	= conn.cursor()
			
			cur.execute('select * from passengers where CustomerId="' + dataCustomerId + '"')
			results=cur.fetchall()
			
			if results:
				messagebox.showinfo('Failure','Please choose a different Customer Id')
				return;
			else:
				cur.execute('insert into passengers values' + str(data))
				conn.commit()            
				messagebox.showinfo('Success','Account successfully created')
				controller.show_frame(WelcomePage)
			
			entryCustomerId.delete(0, tk.END)
			entryFirstName.delete(0, tk.END)
			entryLastName.delete(0, tk.END)
			entryDob.delete(0, tk.END)
			entryMobile.delete(0, tk.END)
			entryGender.delete(0, tk.END)
			entryAddress.delete(0, tk.END)
			entryPassword.delete(0, tk.END)
			
			cur.close()
			conn.close()
	
		def Cancel():
			entryCustomerId.delete(0, tk.END)
			entryFirstName.delete(0, tk.END)
			entryLastName.delete(0, tk.END)
			entryDob.delete(0, tk.END)
			entryMobile.delete(0, tk.END)
			entryGender.delete(0, tk.END)
			entryAddress.delete(0, tk.END)
			entryPassword.delete(0, tk.END)
			controller.show_frame(WelcomePage)
	
		button1 = tk.Button(self, text='Ok',  
							command=Ok)
		button1.grid(row=20, column=9)
		
		button2 = tk.Button(self, text='Cancel',  
							command=Cancel)
		button2.grid(row=20, column=10)

		
class SignInPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)		  
		
		label = tk.Label(self, text="AIRLINES RESERVATION SYSTEM - Sign In", font=LARGE_FONT)
		label.grid(column=10,row=0)
		
		CustomerId		= tk.StringVar()
		Password		= tk.StringVar()
		
		tk.Label(self, text="Customer Id: ").grid(row=4,column=9, sticky=tk.W)
		tk.Label(self, text="Password: ").grid(row=5,column=9, sticky=tk.W)
		
		entryCustomerId	= tk.Entry(self,  text = CustomerId)
		entryPassword	= tk.Entry(self,  text = Password, show="*")
		
		entryCustomerId.grid(row=4,column=10)
		entryPassword.grid(row=5,column=10)
				
		def Ok():
		
			dataCustomerId	= "{}".format(entryCustomerId.get())
			
			dataPassword	= "{}".format(entryPassword.get())
			
			if(len(dataCustomerId) == 0):
				messagebox.showinfo('Validation Failed','Please enter Customer Id')
				return;
				
			if(len(dataPassword) == 0):
				messagebox.showinfo('Validation Failed','Please enter Password')
				return;
			
			conn= sqlite3.connect('test2.db')
			cur	= conn.cursor()	
			cur.execute('select * from passengers where CustomerId="' + dataCustomerId + '" and password="' + dataPassword + '"')
			results=cur.fetchall()
			
			if results:
				conn.commit()
				messagebox.showinfo('Success','Successfully logged in')
				global Id
				Id=dataCustomerId
				controller.show_frame(MenuPage)
				
			else:
				messagebox.showinfo('Failure','Credentials Incorrect')
			
			entryCustomerId.delete(0, tk.END)
			entryPassword.delete(0, tk.END)
			cur.close()
			conn.close()
			
		def Cancel():
			entryCustomerId.delete(0, tk.END)
			entryPassword.delete(0, tk.END)
			controller.show_frame(WelcomePage)


		button1 = tk.Button(self, text='Ok',  
							command=Ok)
		button1.grid(row=12, column=9)
		
		button2 = tk.Button(self, text='Cancel', 
							command=Cancel)
		button2.grid(row=12, column=10)
		
		
class MenuPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self, text="AIRLINES RESERVATION SYSTEM - Menu page", font=LARGE_FONT)
		label.grid(column=10,row=0)
 
		button1 = tk.Button(self, text='Flights', 
							command=lambda : controller.show_frame(FlightPage))
		button1.grid(column=10,row=2)
		
		button2 = tk.Button(self, text='Tickets',  
							command=lambda:controller.show_frame(TicketsPage))
		button2.grid(column=10,row=3)
		
		button3 = tk.Button(self, text='Log Out',  
							command=lambda:controller.show_frame(WelcomePage))
		button3.grid(column=10,row=4)
		
		
class FlightPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self, text='Airlines Reservation System - Flight Booking', font=LARGE_FONT)
		label.grid(column=10,row=0)
 
		SourceFlight 		= tk.StringVar()
		DestFlight 			= tk.StringVar()
		DateFlight 			= tk.StringVar()
		NumFlightTickets 	= tk.StringVar()
		
		tk.Label(self, text="Source City: ").grid(row=4,column=9, sticky=tk.W)
		tk.Label(self, text="Dest City: ").grid(row=5,column=9, sticky=tk.W)
		tk.Label(self, text="Date of Flight: ").grid(row=7,column=9, sticky=tk.W)
		tk.Label(self, text="No. of Tickets: ").grid(row=8,column=9, sticky=tk.W)
		
		entryDateFlight = DateEntry(self, width=17, background='darkblue', foreground='white', borderwidth=2, year=2019)
		entryNumFlightTickets = tk.Entry(self, text=NumFlightTickets)
		
		conn= sqlite3.connect('test2.db')
		cur	= conn.cursor()	
		cur.execute('select distinct(source) from flights')
		results = cur.fetchall()
		source_list=[]
		for values in results:
				source_list.append(values[0])
				
		var_source = tk.StringVar(self)
		var_source.set(source_list[0])
		opt_source = tk.OptionMenu(self, var_source, *source_list)
		opt_source.config(width=9, font=('Helvetica', 12))
		opt_source.grid(row=4,column=10)
		results = cur.execute('select distinct(dest) from flights')
		dest_list=[]
		for values in results:
				dest_list.append(values[0])
				
		var_dest = tk.StringVar(self)
		var_dest.set(dest_list[0])
		opt_dest = tk.OptionMenu(self, var_dest, *dest_list)
		opt_dest.config(width=9, font=('Helvetica', 12))
		opt_dest.grid(row=5,column=10)
					
		entryDateFlight.grid(row=7,column=10)
		entryNumFlightTickets.grid(row=8,column=10)
		
		booking=tk.Label(self,text="")
		booking.grid(column=9,row=20)

		def ok():
			dataDateFlight 			= "{}".format(entryDateFlight.get())
			dataNumFlightTickets 	= "{}".format(entryNumFlightTickets.get())
			
			if(len(dataDateFlight) == 0):
				messagebox.showinfo('Validation Failed','Please enter Date Of Flight')
				return;
				
			if(len(dataNumFlightTickets) == 0):
				messagebox.showinfo('Validation Failed','Please enter number of flight tickets')
				return;
						
			conn		= sqlite3.connect('test2.db')
			cur			= conn.cursor()				
			cur.execute('select seats,company,flight_num,date,price from flights where source="' + var_source.get() + '" and dest="' + var_dest.get() + '" and date="' + dataDateFlight + '" and seats >=' + dataNumFlightTickets)					
			results		= cur.fetchone()
			global Id
			Customer=Id
			
			if results:
				seats 		= results[0]
				company		= results[1]
				flight_num	= results[2]
				date		= results[3]
				price		= results[4]
				num 		= int(seats) - int(dataNumFlightTickets)
				cur.execute('update flights set seats = '+ str(num) +' where source="' + var_source.get() + '" and dest="' + var_dest.get() + '" and date="' + dataDateFlight + '"')							
				conn.commit()
				booking.configure(text=str(dataNumFlightTickets) + ' Flight seat(s) successfully booked from ' + str(var_source.get()) + ' to ' + str(var_dest.get()) )
				messagebox.showinfo('Success','Flight seat(s) successfully booked')
				
				data = (Customer, company, flight_num, date, price,var_source.get(), var_dest.get(), dataNumFlightTickets)				
				cur.execute('insert into tickets values' + str(data))
				conn.commit()            
				messagebox.showinfo('Success','Ticket record updated successfully')
				
			else:
				messagebox.showinfo('Failure','Seats not available')
			
			entryDateFlight.delete(0, tk.END)
			entryNumFlightTickets.delete(0, tk.END)
			
			cur.close()
			conn.close()
			
		def Back():
			entryDateFlight.delete(0, tk.END)
			entryNumFlightTickets.delete(0, tk.END)
			booking.configure(text="")
			controller.show_frame(MenuPage)
		
		
		button1 = tk.Button(self, text='Ok', 
							command=ok)
		button1.grid(row=15, column=9)
		
		button2 = tk.Button(self, text='Back',  
							command=Back)
		button2.grid(row=15, column=10)
		
		
class TicketsPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='Airlines Reservation System - Tickets', font=LARGE_FONT)
		label.grid(column=10,row=0)
		
		conn= sqlite3.connect('test2.db')
		cur	= conn.cursor()
		
		my_label = tk.Text(self)
		my_label.grid(column=10,row=5)
		
		def ok():
			
			global Id
			Customer=Id
			
			cur.execute('select * from tickets where CustomerId="' + str(Customer)+'"')
			results		= cur.fetchall()
			
			if results:

				my_label.insert(tk.END, "Flight"+"    "+"Flight No."+"  "+"Date"+" "+"   Source"+"   "+" Dest"+ "  "+" Fare"+ "    "+" Tickets"+"\n")
				my_label.insert(tk.END, "----------------------------------------------------------------------------"+"\n")
				for row in results:
					
					flightName 		= row[1]
					flightNum		= row[2]
					flightDate		= row[3]
					flightfare		= row[4]
					flightSource	= row[5]
					flightDest		= row[6]
					flighttickets	= row[7]
					
					text=str(flightName)+"    "+str(flightNum)+"    "+str(flightDate)+"    "+str(flightSource)+"    "+str(flightDest)+"    "+str(flightfare)+"    "+str(flighttickets)
					my_label.insert(tk.END, text+"\n")
				
			else:
				messagebox.showinfo('No Booking','No Booking has been done')
			
				
		def Back():
			my_label.delete(1.0, tk.END)
			controller.show_frame(MenuPage)
			
		button1 = tk.Button(self, text='View Tickets',  
							command=ok)
		button1.grid(column=10,row=2)
		
		button2 = tk.Button(self, text='Back',  
							command=Back)					
		button2.grid(column=10,row=3)
 

if __name__ == '__main__':
	app = MainWindow()
	app.mainloop()
	Id=0