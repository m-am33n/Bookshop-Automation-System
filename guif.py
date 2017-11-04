#!/usr/bin/python
import sqlite3
import random
import datetime

connection = sqlite3.connect("BAS.db")

'''
Changes to be made:

1)Make main window bigger in size
2)Add moving text: main window+login page and wherever necessary
3)Add multiple books to a single order(Change Sales Records as well)
4)Add scrollers to search window+make search results bigger in size
5)Add images to background wherever necessary
6)Check for all entries(if any are blank)
'''

cursor = connection.cursor()
import sys
from Tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
global cart
cart=[]
#global price
#price=0

def confbkadd():
	global confirmb
	confirmb=Tk()
	confirmb.geometry('500x150+300+120')
    	confirmb.title('Confirm Book')
    	isbn=str(ei1.get())
	name=str(ei2.get())
	auth=str(ei3.get())
	price=str(ei4.get())
	cat=str(ei5.get())
	pub=str(ei6.get())
    	
	if( isbn!='' and name!='' and auth!='' and price!='' and cat!='' and pub!=''):
	
		l1=Label(confirmb,text='Are you sure you want to add this book?',font=(10))
		b1= Button(confirmb,text='Yes',width=10,height=3,command=bookadd)
		b2= Button(confirmb,text='No',width=10,height=3,command=confbdest)
		
	
		l1.place(x=60,y=20)
		b1.place(x=80,y=80)
		b2.place(x=320,y=80)

	else:
        	l7=Label(inv,text='Please enter all details',fg='red',font=(10))	
        	l7.place(x=150,y=440)
        	confirmb.destroy()
        	l7.after(3000, lambda: l7.place_forget() )
def confbdest():
	confirmb.destroy()

def bookadd():
	confirmb.destroy()
	isbn=str(ei1.get())
	name=str(ei2.get())
	auth=str(ei3.get())
	price=float(ei4.get())
	cat=str(ei5.get())
	pub=str(ei6.get())
	
	vis=Label(inv,text='Book Added successfully!',font=(8))
	vis.place(x=150,y=460)
	vis.after(3000, lambda: vis.place_forget() )
	cursor.execute('INSERT INTO Book VALUES (?,?,?,?,?,?)',(isbn,name,auth,price,cat,pub))
	connection.commit()
	return

	
def vsrec():
	
	cursor.execute("SELECT * FROM Sales")
	rows=cursor.fetchall()
		
	searchres=Tk()
	searchres.geometry('960x640+100+120')
	searchres.title('Sales Records')

	srl=Label(searchres,text='Sales Records:',font=('Sales Records:',13),bg='Moccasin',fg='black')
	srl.place(x=80,y=40)
          	
	
	l1=Label(searchres,text='Sales ID',font=('Sales ID',10))
	l2=Label(searchres,text='Customer ID',font=('Customer',10))
	l3=Label(searchres,text='Invoice No',font=('Invoice No',10))
	l4=Label(searchres,text='Sales Date',font=('Sales Date',10))
	l5=Label(searchres,text='Bill Amount',font=('Bill Amount',10))
	
	l1.place(x=60,y=80)
	l2.place(x=235,y=80)
	l3.place(x=410,y=80)
	l4.place(x=585,y=80)
	l5.place(x=760,y=80)
		
	col=100
	for r in rows:
		row=60
		for x in r:
			templabel=Label(searchres,text=x,font=(str(x),8))
			templabel.place(x=row,y=col)
			row=row+175
		col=col+15
		
	return
	 
def addinv():
	global inv
	inv=Tk()
	inv.geometry('480x480+500+120')
        inv.title('Book Inventory')
        wel=Label(inv,text='Add New Book',fg='black',bg='Moccasin',font=(16))
        global ei1,ei2,ei3,ei4,ei5,ei6
        l1=Label(inv,text='Book ISBN:',font=(10))
        l2=Label(inv,text='Book Name:',font=(10))
        l3=Label(inv,text='Author:',font=(10))
        l4=Label(inv,text='Price:',font=(10))
        l5=Label(inv,text='Category:',font=(10))
        l6=Label(inv,text='Publisher:',font=(10))
        
        ei1=Entry(inv,font=(10),bd=5)
        ei2=Entry(inv,font=(10),bd=5)
        ei3=Entry(inv,font=(10),bd=5)
        ei4=Entry(inv,font=(10),bd=5)
        ei5=Entry(inv,font=(10),bd=5)
        ei6=Entry(inv,font=(10),bd=5)
        
        b1= Button(inv,text='Add Book',width=20,height=3,command=confbkadd)
        wel.place(x=150,y=40)
        l1.place(x=70,y=80)	
        ei1.place(x=230,y=80)
        l2.place(x=70,y=120)	
        ei2.place(x=230,y=120)
        l3.place(x=70,y=160)	
        ei3.place(x=230,y=160)
        l4.place(x=70,y=200)	
        ei4.place(x=230,y=200)
        l5.place(x=70,y=240)	
        ei5.place(x=230,y=240)
        l6.place(x=70,y=280)	
        ei6.place(x=230,y=280)
        b1.place(x=150,y=380)
        return
 
def viewpur():
	cursor.execute("SELECT * FROM Purchase")
	rows=cursor.fetchall()
		
	searchres=Tk()
	searchres.geometry('840x640+100+120')
	searchres.title('Purchase Records')

	srl=Label(searchres,text='Purchase Records:',font=('Purchase Records:',13),bg='Moccasin',fg='black')
	srl.place(x=80,y=40)
          	
	
	l1=Label(searchres,text='Purchase ID',font=('Sales ID',10))
	l2=Label(searchres,text='Supplier ID',font=('Customer',10))
	l3=Label(searchres,text='Purchase Date',font=('Invoice No',10))
	l4=Label(searchres,text='Amount Paid',font=('Sales Date',10))
		
	l1.place(x=40,y=80)
	l2.place(x=240,y=80)
	l3.place(x=440,y=80)
	l4.place(x=640,y=80)
	
	col=100
	for r in rows:
		row=40
		for x in r:
			templabel=Label(searchres,text=x,font=(str(x),8))
			templabel.place(x=row,y=col)
			row=row+200
		col=col+15
		
	return
def puradd():
	confirmp.destroy()
	purid= str(ep1.get())
	supid= str(ep2.get())
	now=datetime.datetime.now()
	date=now.strftime("%Y-%m-%d")
	price= float(ep6.get())
	
	vis=Label(pur,text='Purchase Added successfully!',font=(8))
	vis.place(x=150,y=460)
	vis.after(3000, lambda: vis.place_forget() )
	cursor.execute('INSERT INTO Purchase VALUES (?,?,?,?)',(purid,supid,date,price))
	connection.commit()
	return 

def confpur():
	global confirmp
	confirmp=Tk()
	confirmp.geometry('500x150+300+120')
    	confirmp.title('Confirm Purchase')
    	purid= str(ep1.get())
	supid= str(ep2.get())
	price= str(ep6.get())
	
	if(purid!='' and supid!='' and price!=''):	
		l1=Label(confirmp,text='Are you sure you want to add this purchase?',font=(10))
		b1= Button(confirmp,text='Yes',width=10,height=3,command=puradd)
		b2= Button(confirmp,text='No',width=10,height=3,command=confdest)
	
		l1.place(x=40,y=20)
		b1.place(x=80,y=80)
		b2.place(x=320,y=80)
	else:
		l2=Label(pur,text='Please enter all details',font=(10),fg='red')
		l2.place(x=200,y=430)
		l2.after(3000, lambda: l2.place_forget() )
		confdest()

def confdest():
	confirmp.destroy()
	
def addpur():
	global pur
	pur=Tk()
	pur.geometry('640x480+500+120')
        pur.title('Book Purchase')
        wel=Label(pur,text='Add New Book',fg='black',bg='yellow',font=(16))
        global ep1,ep2,ep3,ep4,ep5,ep6
        l1=Label(pur,text='Purchase ID:',font=(10))
        l2=Label(pur,text='Supplier ID:', font=(10))
        l7=Label(pur,text='Price:',font=(10))
        
        ep1=Entry(pur,font=(10),bd=5)
        ep2=Entry(pur,font=(10),bd=5)
        ep6=Entry(pur,font=(10),bd=5)
        
        
        b1= Button(pur,text='Add Purchase Record',width=30,height=3,command=confpur)
        wel.place(x=150,y=40)
        l1.place(x=70,y=80)	
        ep1.place(x=230,y=80)
        l2.place(x=70,y=190)	
        ep2.place(x=230,y=190)
        l7.place(x=70,y=300)
        ep6.place(x=230,y=300)
        
        b1.place(x=170,y=350)
	return

def reqadd():
	confirmr.destroy()
	book= str(cb1.get())
	auth= str(ca1.get())
	
	vis=Label(request,text='Request made successfully!',font=(8))
	vis.place(x=150,y=460)
	vis.after(3000, lambda: vis.place_forget() )
	cursor.execute('INSERT INTO Request VALUES (?,?)',(book,auth))
	connection.commit()
	return 

def confreqdest():
	confirmr.destroy()

def confreq():
	global confirmr
	confirmr=Tk()
	confirmr.geometry('500x150+300+120')
    	confirmr.title('Confirm Request')
	
	l1=Label(confirmr,text='Are you sure you want to request this book?',font=(10))
	b1= Button(confirmr,text='Yes',width=10,height=3,command=reqadd)
	b2= Button(confirmr,text='No',width=10,height=3,command=confreqdest)
	
	l1.place(x=40,y=20)
	b1.place(x=80,y=80)
	b2.place(x=320,y=80)
	
def cusreq():
	global cb1,ca1
	global request
	request= Tk()
	request.geometry('640x480+700+120')
	request.title('Request Book')
	disp=Label(request,text='Request your book here:',fg='black',bg='Moccasin',font=(12))
	disp.place(x=200,y=70)
	sl1= Label(request,text='Book Title:',font=('Book Title:',10))
	cb1= Entry(request,font=(10),bd=5)

	sl2= Label(request,text='Author:',font=('Author:',10))
	ca1= Entry(request,font=(10),bd=5)

	sl1.place(x=100,y=140)
	cb1.place(x=210,y=140)

	sl2.place(x=100,y=220)
	ca1.place(x=210,y=220)

	sb= Button(request,text='Request Book',width=20,height=2,command=confreq)	
	sb.place(x=210,y=300)
	return

def logoutadm():
	admpg.destroy()
	return

def adminpage():
	global admpg
	user=str(ea1.get())
	pasw=str(ea2.get())

 	cursor.execute('SELECT Login_ID,Password,Admin_ID FROM Admin')
	rows=cursor.fetchall()
	flag=0
	
	for r in rows:
		if(user==r[0] and pasw==r[1]):
		
			var=Label(adm,text="Login Successful",font=("Login Successful",18),fg="green")
			var.place(x=150,y=400)
			adm.destroy()	
			admpg= Tk()
			admpg.geometry('640x480+500+120')
			admpg.title('AdminPage')
			var='Welcome  '+r[2]+'!'
			l1=Label(admpg,text=var,fg='black',bg='Moccasin',font=(var,16))
			l1.place(x=200,y=50)	

			b=Button(admpg,text="Log Out",fg='blue',width=5,height=1,command=logoutadm)
			b.place(x=540,y=50)

			b1=Button(admpg,text="View Sales Record",width=20,height=3,command=vsrec)
			b2=Button(admpg,text="Add to inventory", width=20,height=3,command=addinv)
			b3=Button(admpg,text="View Purchase Record",width=25,height=3,command=viewpur)
			b4=Button(admpg,text="Add Purchase Record",width=25,height=3,command=addpur)
			b5=Button(admpg,text="Customer Requests",width=20,height=3,command=request)
			b1.place(x=100,y=100)
			b2.place(x=400,y=100)
			b3.place(x=100,y=250)
			b4.place(x=400,y=250)
			b5.place(x=250,y=400)
			flag=1
		
	if(flag==0):
		var=Label(adm,text="Incorrect Username/Password",font=("Incorrect Username/Password",10),fg="black")
		var.place(x=150,y=420)
	return
		
def spacesearch(x):
	if (x==0):
		return 90
	elif x==1:
		return 276
	elif x==2:
		return 216
	elif x==3:
		return 90
	elif x==4:
		return 168		
	elif x==5:
		return 0
		
def sbookfun():
	var1=str(se1.get())
	#sql_command="SELECT * FROM Book WHERE Book_Name LIKE '%?%' "
	bname='%'+var1+'%'
	bname=bname.lower()
	
	var2=str(se2.get())
	auth='%'+var2+'%'
	auth=auth.lower()

	var3=str(se3.get())
	cat='%'+var3+'%'
	cat=cat.lower()

	cursor.execute("SELECT * FROM Book WHERE LOWER(Book_Name) LIKE ? AND LOWER(Author) LIKE ? AND LOWER(Category) LIKE ?",(bname,auth,cat))
	rows=cursor.fetchall()
		
	searchres=Tk()
	searchres.geometry('1280x640+100+120')
	searchres.title('Search Results')

	srl=Label(searchres,text='Search Results:',font=('Search Results:',13),bg='Moccasin',fg='black')
	srl.place(x=80,y=40)
	
	l1=Label(searchres,text='ISBN',font=('ISBN',12))
	l2=Label(searchres,text='Name',font=('Name',12))
	l3=Label(searchres,text='Author',font=('Author',12))
	l4=Label(searchres,text='Price',font=('Price',12))
	l5=Label(searchres,text='Category',font=('Category',12))
	l6=Label(searchres,text='Publisher',font=('Publisher',12))
	l1.place(x=65,y=80)
	l2.place(x=155,y=80)
	l3.place(x=431,y=80)
	l4.place(x=647,y=80)
	l5.place(x=737,y=80)
	l6.place(x=905,y=80)
	
	
	
	col=100
	for r in rows:
		row=65
		for x in range(len(r)):
			templabel=Label(searchres,text=r[x],font=(str(r[x]),10))
			templabel.place(x=row,y=col)
			row=row+spacesearch(x)
		col=col+20
		
	return
	
		
def sbook():
	global se1,se2,se3
	searchbk= Tk()
	searchbk.geometry('640x480+700+120')
	searchbk.title('Search Book')
	disp=Label(searchbk,text='Enter keywords for search',fg='black',bg='Moccasin',font=(12))
	disp.place(x=200,y=70)
	sl1= Label(searchbk,text='Book Title:',font=('Book Title:',10))
	se1= Entry(searchbk,font=(10),bd=5)

	sl2= Label(searchbk,text='Author:',font=('Author:',10))
	se2= Entry(searchbk,font=(10),bd=5)

	sl3= Label(searchbk,text='Category:',font=('Category:',10))
	se3= Entry(searchbk,font=(10),bd=5)

	sl1.place(x=100,y=140)
	se1.place(x=210,y=140)

	sl2.place(x=100,y=220)
	se2.place(x=210,y=220)

	sl3.place(x=100,y=300)
	se3.place(x=210,y=300)

	sb= Button(searchbk,text='Search Available Books',width=25,height=2,command=sbookfun)	
	sb.place(x=210,y=350)

	sl4= Label(searchbk,text="Can't find the book you're looking for?",font=("Can't find the book you're looking for?",10),fg='blue')
	sb1= Button(searchbk,text='Click Here',fg='blue',width=10,height=2,command=cusreq)

	sl4.place(x=100,y=420)
	sb1.place(x=390,y=410)
	return
def salord():
	salid='sal'+str(random.randint(1,10000))
	cusid=userc
	invo=random.randint(1,10000)
	now=datetime.datetime.now()
	date=now.strftime("%Y-%m-%d")
	isbn=str(epo1.get())
	#cursor.execute('SELECT Price from Book WHERE Book_ISBN=?',(isbn,))
	#rows=cursor.fetchall()
	
	cursor.execute('INSERT INTO Sales VALUES(?,?,?,?,?)',(salid,cusid,invo,date,pri))
	connection.commit()
	for book in cart:
		cursor.execute('DELETE FROM Book WHERE Book_ISBN=?',(book,))
		connection.commit()
		
	check.destroy()
	confirmch.destroy()
	show=Label(pord,text='Order placed successfully',font=(8))
	show.place(x=100,y=320)	
	show.after(3000, lambda: show.place_forget() )
	#cart=[]
	#pri=0
	return 
	
def delbook(pri,book,p):
	#print book
	#print count
	cart.remove(book)
	pri=pri-p
	check.destroy()
	viewcart()
	return
def cartdest():
	check.destroy()
	return

def space(x):
	if x==0:
		return 100
	elif x==1:
		return 400
	else:
		return 50
	
def confchdest():
	confirmch.destroy()
	return
	
def confcheck():
	global confirmch
	confirmch=Tk()
	confirmch.geometry('500x150+500+120')
    	confirmch.title('Confirm Checkout')
	
	l1=Label(confirmch,text='Are you sure you want to checkout?',font=(10))
	b1= Button(confirmch,text='Yes',width=10,height=3,command=salord)
	b2= Button(confirmch,text='No',width=10,height=3,command=confchdest)
	
	l1.place(x=60,y=20)
	b1.place(x=80,y=80)
	b2.place(x=320,y=80)

		
	
def viewcart():
	global pri
	pri=0
	global check
	check=Tk()
	check.geometry('840x700+500+200')
	check.title('Your Cart')
	disp=Label(check,text='Your Cart:',fg='black',bg='Moccasin',font=('Your Cart:',20))
	disp.place(x=130,y=70)
	
	backButton=Button(check,text='<-- Back',width=6,height=2,command=cartdest)
	backButton.place(x=20,y=40) 
	
	l1=Label(check,text='ISBN',font=('ISBN',15))
	l2=Label(check,text='Title',font=('Title',15))
	l3=Label(check,text='Price',font=('Price',15))
		
	l1.place(x=100,y=120)
	l2.place(x=200,y=120)
	l3.place(x=600,y=120)
	col=170
	for book in cart:
		cursor.execute('SELECT Book_ISBN,Book_Name,Price from Book where Book_ISBN=?',(book,))
		rows=cursor.fetchall()
		for r in rows:
			row=100
			for x in range(len(r)):
				templabel=Label(check,text=r[x],font=(str(r[x]),13))
				templabel.place(x=row,y=col)
				row=row+space(x)
			pri=pri+float(r[2])
		col=col+40
		
	tempButton=Button(check,text='Remove',width=6,height=1,command=lambda:delbook(pri,book,r[2]))
	tempButton.place(x=row+40,y=col-40)
	
	l4=Label(check,text='Bill Amount : ',font=('Bill Amount : ',12))
	l5=Label(check,text=str(pri),font=(str(pri),12))
	l4.place(x=450,y=500)
	l5.place(x=600,y=500)
	checkButton=Button(check,text='Checkout',width=6,height=1,command=confcheck)
	checkButton.place(x=400,y=600)
	return

def addtocart():
	global cart
	#cart=[]
	isbn=str(epo1.get())
	if isbn=='':
		l2=Label(pord,text='Please enter the ISBN',font=(8))
		l2.place(x=100,y=320)
		l2.after(3000, lambda: l2.place_forget() )
		return
	
	cursor.execute('SELECT * FROM Book where Book_ISBN=?',(isbn,))
	rows=cursor.fetchall()
	if len(rows)==0:
		l1=Label(pord,text='Book not in stock!',font=(8))
		l1.place(x=130,y=320)
		l1.after(3000, lambda: l1.place_forget() )
	else:
		cart.append(isbn)
		print cart
		l3=Label(pord,text='Added to Cart!',font=(8))
		l3.place(x=140,y=320)
		l3.after(3000, lambda: l3.place_forget() )
		
	
	return
def porder():
	global pord
	pord=Tk()
	pord.geometry('360x360+500+200')
	pord.title('Order')
	disp=Label(pord,text='Book Order',fg='black',bg='Moccasin',font=(12))
	disp.place(x=130,y=70)
	
	l1=Label(pord,text='ISBN:',font=(10))
	l2=Label(pord,text='Want to know ISBN of book?',font=('Want to know ISBN of Book?',10))
	
	global epo1	
	epo1=Entry(pord,font=(10),bd=5,width=10)
	b1=Button(pord,text='Click here',fg='blue',width=6,height=1,command=sbook)
	b2=Button(pord,text='Add To Cart',width=12,height=2,command=addtocart)
	b3=Button(pord,text='View Cart',width=12,height=2,command=viewcart)
	l1.place(x=40,y=145)
	epo1.place(x=130,y=140)
	l2.place(x=40,y=206)
	b1.place(x=230,y=200)
	b2.place(x=40,y=270)	
	b3.place(x=220,y=270)
	return
	
def viewcomporder():
	
	cursor.execute("SELECT Sales_ID,Invoice_no,S_Date,Bill_Amount FROM Sales WHERE Customer_ID=?",(userc,))
	rows=cursor.fetchall()
		
	searchres=Tk()
	searchres.geometry('840x640+100+120')
	searchres.title('Completed Orders')

	srl=Label(searchres,text='Completed Orders:',font=('Completed Orders:',13),bg='Moccasin',fg='black')
	srl.place(x=80,y=40)
          	
	
	l1=Label(searchres,text='Sales ID',font=('Sales ID',10))
	l2=Label(searchres,text='Invoice Number',font=('Invoice Number',10))
	l3=Label(searchres,text='Sales Date',font=('Sales Date',10))
	l4=Label(searchres,text='Bill Amount',font=('Bill Amount',10))
		
	l1.place(x=40,y=80)
	l2.place(x=240,y=80)
	l3.place(x=440,y=80)
	l4.place(x=640,y=80)
	
	col=100
	for r in rows:
		row=40
		for x in r:
			templabel=Label(searchres,text=x,font=(str(x),8))
			templabel.place(x=row,y=col)
			row=row+200
		col=col+15
		
	return
def request():
	requests= Tk()
	requests.geometry('640x480+700+120')
	requests.title('Book Requests')
	cursor.execute("SELECT * FROM Request")
	rows=cursor.fetchall()
		
	srl=Label(requests,text='Customer Book Requests:',font=('Customer Book Requests:',13),bg='Moccasin',fg='black')
	srl.place(x=80,y=40)
          		
	l1=Label(requests,text='Book Name',font=('Sales ID',10))
	l2=Label(requests,text='Author',font=('Customer',10))
	
	l1.place(x=60,y=80)
	l2.place(x=235,y=80)
	
		
	col=100
	for r in rows:
		row=60
		for x in r:
			templabel=Label(requests,text=x,font=(str(x),8))
			templabel.place(x=row,y=col)
			row=row+175
		col=col+15
		
	return

def logoutcust():
	cuspg.destroy()
	return


    
def custpage():
	global userc
	global cuspg
	#global stvar
	userc=str(ec1.get())
	paswc=str(ec2.get())
	
	cursor.execute('SELECT Customer_ID,Password,Customer_Name FROM Customer')
	rows=cursor.fetchall()
	flag=0	
	for r in rows:
		if(userc==r[0] and paswc==r[1]):
			var=Label(cust,text="Login Successful",font=("Login Successful",18),fg="green")
			var.place(x=150,y=400)
			cust.destroy()
			cuspg= Tk()
			cuspg.geometry('640x480+500+120')
			cuspg.title('CustPage')
			var='WELCOME '+r[2]+'!'
			
			

			l1=Label(cuspg,text=var,fg='black',bg='Moccasin',font=(var,16))
			l1.place(x=160,y=50)

			b=Button(cuspg,text="Log Out",fg='blue',width=5,height=1,command=logoutcust)
			b.place(x=540,y=50)

			b1=Button(cuspg,text="Search Books",width=20,height=3,command=sbook)
			b1.place(x=100,y=150)
	
			b2=Button(cuspg,text="Place Order",width=20,height=3,command=porder)
			b2.place(x=400,y=150)

			b3=Button(cuspg,text="View Completed Orders",width=20,height=3,command=viewcomporder)
			b3.place(x=100,y=300)

			b4=Button(cuspg,text="Request",width=20,height=3,command=cusreq)
			b4.place(x=400,y=300)
			flag=1		
	if(flag==0):				
		var=Label(cust,text="Incorrect Username/Password",font=("Incorrect Username/Password",10),fg="black")
		var.place(x=150,y=400)	
		
def admin():
	global adm
	adm=Tk()
	adm.geometry('480x480+500+120')
	adm.title('Admin')
		
	disa1= Label(adm,text='Admin ID',font=('Admin ID',10))
	disa2= Label(adm,text='Password',font=('Password',10))
	ba1= Button(adm,text='Login',width=5,height=2,command=adminpage)
	disa3= Label(adm,text='Welcome Admin',fg='black',bg='Moccasin',font=('Welcome Admin',16))
	global ea1
	ea1= Entry(adm,font=(10),bd=5)
	global ea2
	ea2= Entry(adm,font=(10),bd=5,show='*')
	disa3.place(x=150,y=100)
	disa1.place(x=70,y=230)
	disa2.place(x=70,y=290)
	ba1.place(x=200,y=370)
	ea1.place(x=150,y=230)
	ea2.place(x=150,y=290)
	return 		
def customer():				
        global cust
        cust= Tk()
        cust.geometry('480x480+500+120')
        cust.title('Customer')
        global ec1
        global ec2
        disc1= Label(cust,text='Customer ID',font=('Customer ID',10))
	disc2= Label(cust,text='Password',font=('Password',10))
	bc1= Button(cust,text='Login',width=5,height=2,command=custpage)
	disc3= Label(cust,text='Welcome Customer',fg='black',bg='Moccasin',font=('Welcome Admin',16))
	ec1= Entry(cust,font=(10),bd=5)
	ec2= Entry(cust,font=(10),bd=5,show='*')
	disc3.place(x=150,y=100)
	disc1.place(x=70,y=230)
	disc2.place(x=70,y=290)
	bc1.place(x=200,y=370)
	ec1.place(x=180,y=230)
	ec2.place(x=180,y=290)
	return 	

def sinpg():
	cusid=str(es1.get())
	pasw1=str(es2.get())
	pasw2=str(es21.get())
	cname=str(es3.get())
	city=str(es4.get())
	stre=str(es5.get())
	stat=str(es6.get())
	phno=str(es7.get())
	
	if(pasw1!=pasw2):
		vis=Label(sig,text='  Passwords  dont  match',font=(8))
		vis.place(x=150,y=460)
		vis.after(3000, lambda: vis.place_forget() )
	elif(cusid=='' or pasw1=='' or pasw2=='' or cname=='' or city=='' or stre=='' or stat=='' or phno==''):
		l1=Label(sig,text='Please fill all details',font=(8),fg='red')
		l1.place(x=150,y=460)
		l1.after(3000, lambda: l1.place_forget())
	else :
		vis=Label(sig,text='Account Created successfully',font=(8))
		vis.place(x=150,y=460)
		vis.after(3000, lambda: vis.place_forget() )
		cursor.execute('INSERT INTO Customer VALUES (?,?,?,?,?,?,?)',(cusid,pasw1,cname,city,stre,stat,phno))
		connection.commit()	
	return	
def signup():
	global sig
	sig=Tk()
	sig.geometry('480x480+500+120')
        sig.title('Customer')
        wel=Label(sig,text='Customer SignUp',fg='black',bg='Moccasin',font=(16))
        global es1,es2,es21,es3,es4,es5,es6,es7
        l1=Label(sig,text='Customer ID',font=(10))
        l2=Label(sig,text='Password', font=(10))
        l21=Label(sig,text='Re-enter Password',font=(10))
        l3=Label(sig,text='Name',font=(10))
        l4=Label(sig,text='City',font=(10))
        l5=Label(sig,text='Street',font=(10))
        l6=Label(sig,text='State',font=(10))
        l7=Label(sig,text='Phone No',font=(10))
        
        es1=Entry(sig,font=(10),bd=5)
        es2=Entry(sig,font=(10),bd=5,show='*')
        es21=Entry(sig,font=(10),bd=5,show='*')
        es3=Entry(sig,font=(10),bd=5)
        es4=Entry(sig,font=(10),bd=5)
        es5=Entry(sig,font=(10),bd=5)
        es6=Entry(sig,font=(10),bd=5)
        es7=Entry(sig,font=(10),bd=5)
        
        b1= Button(sig,text='Sign Up',width=20,height=3,command=sinpg)
        wel.place(x=150,y=40)
        l1.place(x=70,y=80)	
        es1.place(x=230,y=80)
        l2.place(x=70,y=120)	
        es2.place(x=230,y=120)
        l21.place(x=70,y=160)	
        es21.place(x=230,y=160)
        l3.place(x=70,y=200)	
        es3.place(x=230,y=200)
        l4.place(x=70,y=240)	
        es4.place(x=230,y=240)
        l5.place(x=70,y=280)	
        es5.place(x=230,y=280)
        l6.place(x=70,y=320)	
        es6.place(x=230,y=320)
        l7.place(x=70,y=360)	
        es7.place(x=230,y=360)
        b1.place(x=150,y=400)
        return
global gui         
gui= Tk()

gui.geometry('1080x700+200+0')
gui.title('Bookshop')
image = Image.open('bg.jpg')
photo_image = ImageTk.PhotoImage(image)
label = Label(gui, image = photo_image)
label.pack()

deli = 120          
svar = StringVar()
labl = Label(gui, textvariable=svar, height=3,width=60,bg='Moccasin',fg='red',font=(svar,15))

def shif():
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    gui.after(deli, shif)

shif.msg = '                          WELCOME TO BOOKSHOP AUTOMATION SYSTEM                          '
shif()
labl.place(x=155,y=140)

#dis= Label(gui,text='Bookshop Automation System',fg='black',bg='Moccasin',font=('Bookshop Automation System',32))
disp= Label(gui,text='New User?',fg='blue',font=('New User?',15))
b1= Button(gui,text='Admin Login',width=25,height=3,command=admin,font=('Admin Login',15))
b2= Button(gui,text='Customer Login',width=25,height=3,command=customer,font=('Customer Login',15))
b3= Button(gui,text='Customer Signup',width=25,height=3,command=signup,font=('Customer Signup',15))
#dis.place(x=200,y=140)
b1.place(x=100, y=530)
b2.place(x=630,y=530)
b3.place(x=360,y=360)
disp.place(x=483,y=325)

gui.mainloop()

