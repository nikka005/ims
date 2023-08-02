import sqlite3
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import time
#========================================pages==========================
from user import usershow
from item import itemshow
from employe import employeshow
from category import categoryshow

from Supplier import Suppliershow
from Sales import saleshow
from dashboard import *
from bill import billclass
class nava():
   
    def __init__(self,main):
        self.main = main
        self.main.geometry("1900x1300")
        self.main.title("\t\t Developed by | Nikka005")
        self.main.iconbitmap("image\main1.ico")
        #--------------- img in back-----------
        
        
        self.img_back = Image.open("image/2.png")
        self.img_back = self.img_back.resize((1650,1000),Image.ANTIALIAS)
        self.img_back = ImageTk.PhotoImage(self.img_back)
        Label(self.main,image=self.img_back).pack(fill=X,side=BOTTOM)

         



        #titel____________
        title = Label(self.main,text="\tInoventry Management System",bg="blue",fg="white",font='arile 30 bold',anchor='w',padx=300,).place(x=0,y=0,relwidth=1,height=70)
        self.clock_lbl = Label(self.main,text="  Date:\t\t\t\tSr. Jogender Singh Pesticides pvt.Ltd \t\t\t  Time:",bg="#bfbbd9",fg="Black",font='arile 18',anchor='w')
        self.clock_lbl.place(x=250,y=70,relwidth=1,height=30)

        #=====btn logout=======
        self.img_logout = Image.open("image/7.png")
        self.img_logout = self.img_logout.resize((142,62),Image.ANTIALIAS)
        self.img_logout = ImageTk.PhotoImage(self.img_logout)

        btn_logout = Label(self.main,image=self.img_logout,bg="blue",activebackground="blue",bd=0).place(x=1390 ,y=0,height=70)

        self.start_img = Image.open("image/8.png")
        self.start_img = self.start_img.resize((150,62),Image.ANTIALIAS)
        self.start_img = ImageTk.PhotoImage(self.start_img)

        btn_logout = Label(self.main,image=self.start_img,bg="blue",activebackground="blue",bd=3).place(x=2 ,y=0,height=70)

        #--------leftside frame----------
        leftframe = Frame(self.main,bd=0,relief=RAISED,bg="#ccebc4")
        leftframe.place(x=0,y=70,width=250,height=1080)
         
        #----------left menu img/lbl----------------------------------------------
        self.img_top = Image.open("image/inventry (1).png")
        self.img_top = self.img_top.resize((250,150),Image.ANTIALIAS)
        self.img_top = ImageTk.PhotoImage(self.img_top)
        lbl_top = Label(leftframe,bg="white",text="logo",image=self.img_top,font="arile 60 bold",fg="black",cursor="hand2").place(x=0,y=0,height=150,width=250)


        #----------left menu frame btn-------

        btn_Dashbord = Button(leftframe,text="Dashboard",fg="black",bg="#b3de69",font="arile 15 ",cursor="hand2",
        
        )
        btn_Dashbord.place(x=0,y=150,width=250,height=40)
        btn_user = Button(leftframe,text="User",fg="black",bg="#56B4E9",font="arile 15 ",cursor="hand2",command=self.user)
        btn_user.place(x=0,y=192,width=250,height=40)
        btn_sale = Button(leftframe,text="Sales",fg="black",bg="#8b8b8b",font="arile 15 ",cursor="hand2",command=self.Sale)
        btn_sale.place(x=0,y=234,width=250,height=40)
        btn_item = Button(leftframe,text="Item",fg="black",bg="#feffb3",font="arile 15 ",cursor="hand2",command=self.item)
        btn_item.place(x=0,y=276,width=250,height=40)
        btn_Supplier = Button(leftframe,text="Supplier",fg="black",bg="#8dd3c7",font="arile 15 ",cursor="hand2",command=self.Supplier)
        btn_Supplier.place(x=0,y=318,width=250,height=40)
        btn_bill = Button(leftframe,text="Bill",fg="black",bg="#6d904f",font="arile 15 ",cursor="hand2",command=self.bill)
        btn_bill.place(x=0,y=360,width=250,height=40)
        btn_Employs = Button(leftframe,text="Employs",fg="black",bg="#ccebc4",font="arile 15 ",cursor="hand2",command=self.employe)
        btn_Employs.place(x=0,y=402,width=250,height=40)
        btn_Category = Button(leftframe,text="Categroy",fg="black",bg="#fa8174",font="arile 15 ",cursor="hand2",command=self.category)
        btn_Category.place(x=0,y=442,width=250,height=40)
       



        self.img_bottom = Image.open("image/main1.jpeg")
        self.img_bottom = self.img_bottom.resize((250,210),Image.ANTIALIAS)
        self.img_bottom = ImageTk.PhotoImage(self.img_bottom)
        lbl_btom = Label(leftframe,bg="white",text="logo",image=self.img_bottom,font="arile 60 bold",fg="black",cursor="hand2").place(x=0,y=482,width=250)

        
        #-----------btn for dashbord front--------
        self.btn_Item1 = StringVar() 
        self.btn_user1 = StringVar() 
        self.btn_supp1 = StringVar() 
        self.btn_Emp1 = StringVar() 
        self.btn_sale1 = StringVar() 
        self.btn_cate1 = StringVar() 
        btn_User1 = Button(self.main,textvariable=self.btn_user1,font='arile 20 bold',bg="#56B4E9",cursor="hand2",bd=5,command=self.user,)
        btn_User1.place(x=400 ,y=150,width=200,height=100)
        btn_Item1 = Button(self.main,textvariable=self.btn_Item1,font='arile 20 bold',bg="#feffb3",cursor="hand2",bd=5,command=self.item)
        btn_Item1.place(x=650 ,y=150,width=200,height=100)
        btn_Supplier1= Button(self.main,textvariable=self.btn_supp1,font='arile 20 bold',bg="#8dd3c7",cursor="hand2",bd=5,command=self.Supplier)
        btn_Supplier1.place(x=900 ,y=150,width=200,height=100)
        btn_Employs1 = Button(self.main,textvariable=self.btn_Emp1,command=self.employe,font='arile 20 bold',bg="#ccebc4",cursor="hand2",bd=5)
        btn_Employs1.place(x=1150 ,y=150,width=200,height=100)
        btn_sale1 = Button(self.main,textvariable=self.btn_sale1,font='arile 20 bold',bg="#8b8b8b",cursor="hand2",bd=5,command=self.Sale)
        btn_sale1.place(x=400 ,y=300,width=200,height=100)
        btn_categrey1 = Button(self.main,textvariable=self.btn_cate1,command=self.category,font='arile 20 bold',bg="#fa8174",cursor="hand2",bd=5)
        btn_categrey1.place(x=650 ,y=300,width=200,height=100)
        btn_bill1 = Button(self.main,text="Bill",font='arile 20 bold',bg="#6d904f",cursor="hand2",bd=5,command=self.bill)
        btn_bill1.place(x=900 ,y=300,width=200,height=100)

        self.update_content()
        #-------------------foter---------------
        
        self.foter_lbl = Label(self.main,text="Contact for any Technical issue\t\t\tName : Gurpreet singh \t\t\tPhoneno. 09024444869\t\t",bg="#8EBA42"
                    ,fg="Black",font='Tahoma 15 ',anchor=W,cursor="hand2",padx=150).place(x=0,y=760,relwidth=1,height=35)
#================================================user========================================================
        
#================================================user========================================================
    def user(self):
        self.user = Toplevel(self.main)
        self.user = usershow(self.user)
        
        
#=====================================================item============================================
    def item(self):
        self.item = Toplevel(self.main)
        self.item = itemshow(self.item)
#=============================================employes=========================================
    def employe(self):
        self.employe = Toplevel(self.main)
        self.employe = employeshow(self.employe)
#===============================================category====================================
    def category(self):
        self.category = Toplevel(self.main)
        self.category = categoryshow(self.category)
#==============================================stock=============================
#===========================purchase============================
    def Supplier(self):
        self.Supplier = Toplevel(self.main)
        self.Supplier = Suppliershow(self.Supplier)
#=================================================================seller==========================
    def Sale(self):
        self.Sale = Toplevel(self.main)
        self.Sale = saleshow(self.Sale)
#===================================================setting========================
    def bill(self):
        self.bill = Toplevel(self.main)
        self.bill = billclass(self.bill)


    def update_content(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
           cur.execute("select * from additem")
           item = cur.fetchall()
           self.btn_Item1.set(f'Item\n({str(len(item))})')
    
           cur.execute("select * from user")
           user = cur.fetchall()
           self.btn_user1.set(f'User\n({str(len(user))})')
         

           cur.execute("select * from employe")
           emp = cur.fetchall()
           self.btn_Emp1.set(f'Employs\n({str(len(emp))})')
    

           cur.execute("select * from Supplier")
           sup = cur.fetchall()
           self.btn_supp1.set(f'Suppliers\n({str(len(sup))})')
          

           cur.execute("select * from category")
           cate = cur.fetchall()
           self.btn_cate1.set(f'Category\n({str(len(cate))})')
           bill = len(os.listdir('bill'))
           self.btn_sale1.set(f'Sales\n({str(bill)})')

           time_ = time.strftime("%H:%M:%S")
           date_ = time.strftime("%d-%m-%Y")

           self.clock_lbl.config(text=f"    Date:{str(date_)}\t\t\t  Sr.Jogender Singh Pesticides pvt.Ltd\t\t\tTime:{str(time_)}")
           self.clock_lbl.after(200,self.update_content)
           

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.main)
           

if __name__ == "__main__":
    main = Tk() 
    main.state('zoomed')
    ob = nava(main)
    main.mainloop()