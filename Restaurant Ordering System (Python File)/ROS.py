from tkinter import *
from tkinter import filedialog,messagebox
from tkinter import ttk
import random
import time
import Food




root = Tk()
root.geometry("1280x690")
root.resizable(0,0)
root.title("Restaurant Ordering System")
root.config(bg="#00008B")

topFrame = Frame(root,bd = 10,relief = RIDGE,bg = "#00008B")
topFrame.pack(side = TOP)

labelTitle = Label(topFrame,text = "Restaurant Management System",font=("arial",30,"bold"),fg = "black",bd = 6,bg = "#ADD8E6",width = 52)
labelTitle.grid(row=0,column=0)

bottomFrame = Frame(root,bd = 10,relief = RIDGE,bg = "#00008B",pady = 10)
bottomFrame.pack(side=BOTTOM)

menuFrame=Frame(root,bd = 10,relief = RIDGE,bg = "#00008B")

mycanvas = Canvas(menuFrame)
mycanvas.pack(side=LEFT, fill="both", expand="yes")

yscrollbar = ttk.Scrollbar(menuFrame, orient = "vertical", command = mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand = yscrollbar.set)

mycanvas.bind("<Configure>", lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")))

foodFrame = LabelFrame(mycanvas, text = "MENU", font = ("arial",19,"bold"))
mycanvas.create_window((0,0), window = foodFrame)

menuFrame.pack(side=LEFT, fill="both", expand="yes")

rightFrame=Frame(root,bd = 15,relief = RIDGE,bg = "#00008B")
rightFrame.pack(side=RIGHT)

recieptFrame=Frame(rightFrame,bd = 4,relief = RIDGE,bg = "#00008B")
recieptFrame.pack()




#Functions

def reset():
    textReceipt.config(state=NORMAL)
    textReceipt.delete(1.0,END)
    textReceipt.config(state=DISABLED)
    t_m1.set("0")
    t_m2.set("0")
    t_m3.set("0")
    t_m4.set("0")
    t_m5.set("0")
    t_m6.set("0")
    t_m7.set("0")
    t_m8.set("0")
    t_m9.set("0")
    t_m10.set("0")
    t_m11.set("0")
    t_m12.set("0")
    t_m13.set("0")
    t_m14.set("0")
    t_m15.set("0")
    t_m16.set("0")
    t_m17.set("0")
    t_m18.set("0")
    t_m19.set("0")
    t_m20.set("0")
    t_m21.set("0")
    t_m22.set("0")
    t_m23.set("0")
    t_m24.set("0")
    t_m25.set("0")
    t_m26.set("0")
    t_m27.set("0")
    t_m28.set("0")
    t_m29.set("0")
    t_m30.set("0")
    t_m31.set("0")
    t_m32.set("0")
    t_m33.set("0")
    t_m34.set("0")
    t_m35.set("0")
    t_m36.set("0")
    payCash.set("0.0")

    textm1.config(state=DISABLED)
    textm2.config(state=DISABLED)
    textm3.config(state=DISABLED)
    textm4.config(state=DISABLED)
    textm5.config(state=DISABLED)
    textm6.config(state=DISABLED)
    textm7.config(state=DISABLED)
    textm8.config(state=DISABLED)
    textm9.config(state=DISABLED)
    textm10.config(state=DISABLED)
    textm11.config(state=DISABLED)
    textm12.config(state=DISABLED)
    textm13.config(state=DISABLED)
    textm14.config(state=DISABLED)
    textm15.config(state=DISABLED)
    textm16.config(state=DISABLED)
    textm17.config(state=DISABLED)
    textm18.config(state=DISABLED)
    textm19.config(state=DISABLED)
    textm20.config(state=DISABLED)
    textm21.config(state=DISABLED)
    textm22.config(state=DISABLED)
    textm23.config(state=DISABLED)
    textm24.config(state=DISABLED)
    textm25.config(state=DISABLED)
    textm26.config(state=DISABLED)
    textm27.config(state=DISABLED)
    textm28.config(state=DISABLED)
    textm29.config(state=DISABLED)
    textm30.config(state=DISABLED)
    textm31.config(state=DISABLED)
    textm32.config(state=DISABLED)
    textm33.config(state=DISABLED)
    textm34.config(state=DISABLED)
    textm35.config(state=DISABLED)
    textm36.config(state=DISABLED)
    textPayment.config(state=DISABLED)
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    var31.set(0)
    var32.set(0)
    var33.set(0)
    var34.set(0)
    var35.set(0)
    var36.set(0)

    subTotalVar.set("")
    taxVar.set("")
    totalCostVar.set("")
    
    


def payment():
    global payCash
    try:
        payment = float(textPayment.get())
        if payment > totalcost:
            payCash.set(round(payment,2))
            textPayment.config(state = DISABLED)
        else:
            messagebox.showerror("Error","Insufficient Funds.")
    except:
        messagebox.showerror("Error","Please Input Numbers Only.")
        



def totalcost():
    global priceOfFood,subTotalOfFood, priceOfFoods, totalcost
    while var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or  var25.get() != 0 or var26.get() != 0 or var27.get() != 0 or var28.get() != 0 or var29.get() != 0 or var30.get() != 0 or var31.get() != 0 or var32.get() != 0 or var33.get() != 0 or var34.get() != 0 or var35.get() != 0 or var36.get() != 0:
        
        item1=float(t_m1.get())
        item2=int(t_m2.get())
        item3=int(t_m3.get())
        item4 = int(t_m4.get())
        item5 = int(t_m5.get())
        item6 = int(t_m6.get())
        item7 = int(t_m7.get())
        item8 = int(t_m8.get())
        item9 = int(t_m9.get())
        item10 = int(t_m10.get())
        item11 = int(t_m11.get())
        item12 = int(t_m12.get())
        item13 = int(t_m13.get())
        item14 = int(t_m14.get())
        item15 = int(t_m15.get())
        item16 = int(t_m16.get())
        item17 = int(t_m17.get())
        item18 = int(t_m18.get())
        item19 = int(t_m19.get())
        item20 = int(t_m20.get())
        item21 = int(t_m21.get())
        item22 = int(t_m22.get())
        item23 = int(t_m23.get())
        item24 = int(t_m24.get())
        item25 = int(t_m25.get())
        item26 = int(t_m26.get())
        item27 = int(t_m27.get())
        item28 = int(t_m8.get())
        item29 = int(t_m29.get())
        item30 = int(t_m30.get())
        item31 = int(t_m31.get())
        item32 = int(t_m32.get())
        item33 = int(t_m33.get())
        item34 = int(t_m34.get())
        item35 = int(t_m35.get())
        item36 = int(t_m36.get())


        LOF = Food.listOfFoods()
        
        
        priceOfFoods=(item1*LOF[0][2]) + (item2*LOF[1][2]) + (item3*LOF[2][2]) + (item4*LOF[3][2]) + (item5*LOF[4][2]) + (item6 * LOF[5][2]) + (item7 * LOF[6][2]) \
                    + (item8 * LOF[7][2]) + (item9 * LOF[8][2] + item10*LOF[9][2]) + (item11*LOF[10][2]) + (item12*LOF[11][2]) + (item13*LOF[12][2]) + (item14*LOF[13][2]) + (item15 * LOF[14][2]) + (item16 * LOF[15][2]) \
                    + (item17 * LOF[16][2]) + (item18 * LOF[17][2]) + (item19*LOF[18][2]) + (item20*LOF[19][2]) + (item21*LOF[20][2]) + (item22*LOF[21][2])+ (item23*LOF[22][2]) + (item24 * LOF[23][2]) + (item25 * LOF[24][2]) \
                    + (item26 * LOF[25][2]) + (item27 * LOF[26][2]) + (item28*LOF[27][2]) + (item29*LOF[28][2]) + (item30*LOF[29][2]) + (item31*LOF[30][2])+ (item32*LOF[31][2]) + (item33 * LOF[32][2]) + (item34 * LOF[33][2]) \
                    + (item35 * LOF[34][2]) + (item36 * LOF[35][2])


        stringPrice = round(priceOfFoods,2)
        priceOfFood.set(str(priceOfFoods))
        
        subTotalOfFood=round(priceOfFoods,2)
        subTotalVar.set("₱"+str(subTotalOfFood))
        
        taxVar.set("₱"+ str(round((priceOfFoods * 0.052),2)))

        totalcost=subTotalOfFood+ round((priceOfFoods * 0.052),2)
        totalCostVar.set("₱"+str(totalcost))
        textPayment.config(state = NORMAL)
        textPayment.delete(0,END)
        break

    else:
        messagebox.showerror("Error","No Food Is selected.")

        
def receipt():
    global restonum,date, payCash

    try:
        payment = float(textPayment.get())
        payCash.set(round(payment,2))
        textPayment.config(state = DISABLED)
        listOfNames = ["Jilbert Vasquez"]
        while priceOfFood.get() != "":
            textReceipt.config(state=NORMAL)
            textReceipt.delete(1.0,END)
            rannum=random.randint(100,10000)
            restonum="RESTO"+str(rannum)
            date=time.strftime("%d/%m/%Y")
            # ranname = random.randint(1,7)
            textReceipt.insert(END,"\n\t\t        JOLLIBEE\n\n")
            textReceipt.insert(END,"Receipt Ref No:\t\t"+restonum+"\t\t\t"+date+"\n")
            textReceipt.insert(END,"Cashier:\t  " + listOfNames[0] + "\t\t\t\n")
            textReceipt.insert(END,"***************************************************************************\n")
            textReceipt.insert(END,"Foods:\t\t\t\t\tCost\n")
            textReceipt.insert(END,"***************************************************************************\n")
            LOF = Food.listOfFoods()
            if t_m1.get()!="0":
                textReceipt.insert(END,LOF[0][1] + f"\t\t\t\t\tP {float(t_m1.get()) * 578.00}\n\n")

            if t_m2.get() !="0":
                textReceipt.insert(END,LOF[1][1] + f"\t\t\t\t\tP {float(t_m2.get()) * 964.00}\n\n")

            if t_m3.get() !="0":
                textReceipt.insert(END,LOF[2][1] + f"\t\t\t\t\tP {float(t_m3.get()) * 1544.00}\n\n")

            if t_m4.get() !="0":
                textReceipt.insert(END,LOF[3][1] + f"\t\t\t\t\tP {float(t_m4.get()) * 1447.00}\n\n")

            if t_m5.get() != '0':
                textReceipt.insert(END,LOF[4][1] + f"\t\t\t\t\tP {float(t_m5.get()) * 1592.00}\n\n")

            if t_m6.get() !="0":
                textReceipt.insert(END,LOF[5][1] + f"\t\t\t\t\tP {float(t_m6.get()) * 1737.00}\n\n")

            if t_m7.get() !="0":
                textReceipt.insert(END,LOF[6][1] + f"\t\t\t\t\tP {float(t_m7.get()) * 289.00}\n\n")

            if t_m8.get() !="0":
                textReceipt.insert(END,LOF[7][1] + f"\t\t\t\t\tP {float(t_m8.get()) * 337.00}\n\n")

            if t_m9.get() !="0":
                textReceipt.insert(END,LOF[8][1] + f"\t\t\t\t\tP {float(t_m9.get()) * 385.00}\n\n")

            if t_m10.get() !="0":
                textReceipt.insert(END,LOF[9][1] + f"\t\t\t\t\tP {float(t_m10.get()) * 433.00}\n\n")

            if t_m11.get() !="0":
                textReceipt.insert(END,LOF[10][1] + f"\t\t\t\t\tP {float(t_m11.get()) * 240.00}\n\n")

            if t_m12.get() !="0":
                textReceipt.insert(END,LOF[11][1] + f"\t\t\t\t\tP {float(t_m12.get()) * 607.00}\n\n")

            if t_m13.get() !="0":
                textReceipt.insert(END,LOF[12][1] + f"\t\t\t\t\tP {float(t_m13.get()) * 298.00}\n\n")

            if t_m14.get() !="0":
                textReceipt.insert(END,LOF[13][1] + f"\t\t\t\t\tP {float(t_m14.get()) * 361.00}\n\n")

            if t_m15.get() !="0":
                textReceipt.insert(END,LOF[14][1] + f"\t\t\t\t\tP {float(t_m15.get()) * 385.00}\n\n")

            if t_m16.get() !="0":
                textReceipt.insert(END,LOF[15][1] + f"\t\t\t\t\tP {float(t_m16.get()) * 289.00}\n\n")

            if t_m17.get() !="0":
                textReceipt.insert(END,LOF[16][1] + f"\t\t\t\t\tP {float(t_m17.get()) * 337.00}\n\n")

            if t_m18.get() !="0":
                textReceipt.insert(END,LOF[17][1] + f"\t\t\t\t\tP {float(t_m18.get()) * 192.00}\n\n")

            if t_m19.get() !="0":
                textReceipt.insert(END,LOF[18][1] + f"\t\t\t\t\tP {float(t_m19.get()) * 240.00}\n\n")

            if t_m20.get() !="0":
                textReceipt.insert(END,LOF[19][1] + f"\t\t\t\t\tP {float(t_m20.get()) * 313.00}\n\n")

            if t_m21.get() !="0":
                textReceipt.insert(END,LOF[20][1] + f"\t\t\t\t\tP {float(t_m21.get()) * 240.00}\n\n")

            if t_m22.get() !="0":
                textReceipt.insert(END,LOF[21][1] + f"\t\t\t\t\tP {float(t_m22.get()) * 361.00}\n\n")

            if t_m23.get() !="0":
                textReceipt.insert(END,LOF[22][1] + f"\t\t\t\t\tP {float(t_m23.get()) * 216.00}\n\n")

            if t_m24.get() !="0":
                textReceipt.insert(END,LOF[23][1] + f"\t\t\t\t\tP {float(t_m24.get()) * 337.00}\n\n")

            if t_m25.get() !="0":
                textReceipt.insert(END,LOF[24][1] + f"\t\t\t\t\tP {float(t_m25.get()) * 120.00}\n\n")

            if t_m26.get() !="0":
                textReceipt.insert(END,LOF[25][1] + f"\t\t\t\t\tP {float(t_m26.get()) * 48.00}\n\n")

            if t_m27.get() !="0":
                textReceipt.insert(END,LOF[26][1] + f"\t\t\t\t\tP {float(t_m27.get()) * 149.00}\n\n")

            if t_m28.get() !="0":
                textReceipt.insert(END,LOF[27][1] + f"\t\t\t\t\tP {float(t_m28.get()) * 96.00}\n\n")

            if t_m29.get() !="0":
                textReceipt.insert(END,LOF[28][1] + f"\t\t\t\t\tP {float(t_m29.get()) * 149.00}\n\n")

            if t_m30.get() !="0":
                textReceipt.insert(END,LOF[29][1] + f"\t\t\t\t\tP {float(t_m30.get()) * 96.00}\n\n")

            if t_m31.get() !="0":
                textReceipt.insert(END,LOF[30][1] + f"\t\t\t\t\tP {float(t_m31.get()) * 149.00}\n\n")

            if t_m32.get() !="0":
                textReceipt.insert(END,LOF[31][1] + f"\t\t\t\t\tP {float(t_m32.get()) * 96.00}\n\n")

            if t_m33.get() !="0":
                textReceipt.insert(END,LOF[32][1] + f"\t\t\t\t\tP {float(t_m33.get()) * 96.00}\n\n")

            if t_m34.get() !="0":
                textReceipt.insert(END,LOF[33][1] + f"\t\t\t\t\tP {float(t_m34.get()) * 110.00}\n\n")

            if t_m35.get() !="0":
                textReceipt.insert(END,LOF[34][1] + f"\t\t\t\t\tP {float(t_m35.get()) * 62.00}\n\n")

            if t_m36.get() !="0":
                textReceipt.insert(END,LOF[35][1] + f"\t\t\t\t\tP {float(t_m36.get()) * 73.00}\n\n")

            textReceipt.insert(END,"***************************************************************************\n")


            textReceipt.insert(END, f"Sub Total\t\t\t\t\tP{priceOfFoods}\n\n")
            textReceipt.insert(END, f"Tax\t\t\t\t\tP{str(round((priceOfFoods * 0.052),2))}\n\n")
            textReceipt.insert(END, f"Total Cost\t\t\t\t\tP{str(totalcost)}\n\n")
            textReceipt.insert(END, f"Payment\t\t\t\t\tP{str(round(payment,2))}\n\n")
            textReceipt.insert(END, f"Change Due\t\t\t\t\tP{str(round(payment-totalcost, 2))}\n\n")
            textReceipt.insert(END,"***************************************************************************\n")
            textReceipt.config(state=DISABLED)
            break
        else:
            messagebox.showerror("Error","No Food Is selected.")

    except:
        messagebox.showerror("Error","Please Input Your Cash.")



def save():
    if textReceipt.get(1.0,END)=="\n":
        pass
    else:
        path=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if path==None:
            pass
        else:

            orderreceipt=textReceipt.get(1.0,END)
            path.write(orderreceipt)
            path.close()
            messagebox.showinfo("Information","Your Receipt Is Succesfully Saved.")



def m1():
    if var1.get()==1:
        textm1.config(state=NORMAL)
        textm1.delete(0,END)
        textm1.focus()
    else:
        textm1.config(state=DISABLED)
        t_m1.set("0")

def m2():
    if var2.get()==1:
        textm2.config(state=NORMAL)
        textm2.delete(0,END)
        textm2.focus()
    else:
        textm2.config(state=DISABLED)
        t_m2.set("0")

def m3():
    if var3.get()==1:
        textm3.config(state=NORMAL)
        textm3.delete(0,END)
        textm3.focus()
    else:
        textm3.config(state=DISABLED)
        t_m3.set("0")

def m4():
    if var4.get()==1:
        textm4.config(state=NORMAL)
        textm4.delete(0,END)
        textm4.focus()
    else:
        textm4.config(state=DISABLED)
        t_m4.set("0")

def m5():
    if var5.get()==1:
        textm5.config(state=NORMAL)
        textm5.delete(0,END)
        textm5.focus()
    else:
        textm5.config(state=DISABLED)
        t_m5.set("0")

def m6():
    if var6.get()==1:
        textm6.config(state=NORMAL)
        textm6.delete(0,END)
        textm6.focus()
    else:
        textm6.config(state=DISABLED)
        t_m6.set("0")

def m7():
    if var7.get()==1:
        textm7.config(state=NORMAL)
        textm7.delete(0,END)
        textm7.focus()
    else:
        textm7.config(state=DISABLED)
        t_m7.set("0")

def m8():
    if var8.get()==1:
        textm8.config(state=NORMAL)
        textm8.delete(0,END)
        textm8.focus()
    else:
        textm8.config(state=DISABLED)
        t_m8.set("0")

def m9():
    if var9.get()==1:
        textm9.config(state=NORMAL)
        textm9.delete(0,END)
        textm9.focus()
    else:
        textm9.config(state=DISABLED)
        t_m9.set("0")

def m10():
    if var10.get()==1:
        textm10.config(state=NORMAL)
        textm10.delete(0,END)
        textm10.focus()
    else:
        textm10.config(state=DISABLED)
        t_m10.set("0")

def m11():
    if var11.get()==1:
        textm11.config(state=NORMAL)
        textm11.delete(0,END)
        textm11.focus()
    else:
        textm11.config(state=DISABLED)
        t_m11.set("0")

def m12():
    if var12.get()==1:
        textm12.config(state=NORMAL)
        textm12.delete(0,END)
        textm12.focus()
    else:
        textm12.config(state=DISABLED)
        t_m12.set("0")

def m13():
    if var13.get()==1:
        textm13.config(state=NORMAL)
        textm13.delete(0,END)
        textm13.focus()
    else:
        textm13.config(state=DISABLED)
        t_m13.set("0")

def m14():
    if var14.get()==1:
        textm14.config(state=NORMAL)
        textm14.delete(0,END)
        textm14.focus()
    else:
        textm14.config(state=DISABLED)
        t_m14.set("0")

def m15():
    if var15.get()==1:
        textm15.config(state=NORMAL)
        textm15.delete(0,END)
        textm15.focus()
    else:
        textm15.config(state=DISABLED)
        t_m15.set("0")

def m16():
    if var16.get()==1:
        textm16.config(state=NORMAL)
        textm16.delete(0,END)
        textm16.focus()
    else:
        textm16.config(state=DISABLED)
        t_m16.set("0")

def m17():
    if var17.get()==1:
        textm17.config(state=NORMAL)
        textm17.delete(0,END)
        textm17.focus()
    else:
        textm17.config(state=DISABLED)
        t_m17.set("0")

def m18():
    if var18.get()==1:
        textm18.config(state=NORMAL)
        textm18.delete(0,END)
        textm18.focus()
    else:
        textm18.config(state=DISABLED)
        t_m18.set("0")

def m19():
    if var19.get()==1:
        textm19.config(state=NORMAL)
        textm19.delete(0,END)
        textm19.focus()
    else:
        textm19.config(state=DISABLED)
        t_m19.set("0")

def m20():
    if var20.get()==1:
        textm20.config(state=NORMAL)
        textm20.delete(0,END)
        textm20.focus()
    else:
        textm20.config(state=DISABLED)
        t_m20.set("0")

def m21():
    if var21.get()==1:
        textm21.config(state=NORMAL)
        textm21.delete(0,END)
        textm21.focus()
    else:
        textm21.config(state=DISABLED)
        t_m21.set("0")

def m22():
    if var22.get()==1:
        textm22.config(state=NORMAL)
        textm22.delete(0,END)
        textm22.focus()
    else:
        textm22.config(state=DISABLED)
        t_m22.set("0")

def m23():
    if var23.get()==1:
        textm23.config(state=NORMAL)
        textm23.delete(0,END)
        textm23.focus()
    else:
        textm23.config(state=DISABLED)
        t_m23.set("0")

def m24():
    if var24.get()==1:
        textm24.config(state=NORMAL)
        textm24.delete(0,END)
        textm24.focus()
    else:
        textm24.config(state=DISABLED)
        t_m24.set("0")

def m25():
    if var25.get()==1:
        textm25.config(state=NORMAL)
        textm25.delete(0,END)
        textm25.focus()
    else:
        textm25.config(state=DISABLED)
        t_m25.set("0")

def m26():
    if var26.get()==1:
        textm26.config(state=NORMAL)
        textm26.delete(0,END)
        textm26.focus()
    else:
        textm26.config(state=DISABLED)
        t_m26.set("0")

def m27():
    if var27.get()==1:
        textm27.config(state=NORMAL)
        textm27.delete(0,END)
        textm27.focus()
    else:
        textm27.config(state=DISABLED)
        t_m27.set("0")

def m28():
    if var28.get()==1:
        textm28.config(state=NORMAL)
        textm28.delete(0,END)
        textm28.focus()
    else:
        textm28.config(state=DISABLED)
        t_m28.set("0")

def m29():
    if var29.get()==1:
        textm29.config(state=NORMAL)
        textm29.delete(0,END)
        textm29.focus()
    else:
        textm29.config(state=DISABLED)
        t_m29.set("0")

def m30():
    if var30.get()==1:
        textm30.config(state=NORMAL)
        textm30.delete(0,END)
        textm30.focus()
    else:
        textm30.config(state=DISABLED)
        t_m30.set("0")

def m31():
    if var31.get()==1:
        textm31.config(state=NORMAL)
        textm31.delete(0,END)
        textm31.focus()
    else:
        textm31.config(state=DISABLED)
        t_m31.set("0")

def m32():
    if var32.get()==1:
        textm32.config(state=NORMAL)
        textm32.delete(0,END)
        textm32.focus()
    else:
        textm32.config(state=DISABLED)
        t_m32.set("0")

def m33():
    if var33.get()==1:
        textm33.config(state=NORMAL)
        textm33.delete(0,END)
        textm33.focus()
    else:
        textm33.config(state=DISABLED)
        t_m33.set("0")

def m34():
    if var34.get()==1:
        textm34.config(state=NORMAL)
        textm34.delete(0,END)
        textm34.focus()
    else:
        textm34.config(state=DISABLED)
        t_m34.set("0")

def m35():
    if var35.get()==1:
        textm35.config(state=NORMAL)
        textm35.delete(0,END)
        textm35.focus()
    else:
        textm35.config(state=DISABLED)
        t_m35.set("0")

def m36():
    if var36.get()==1:
        textm36.config(state=NORMAL)
        textm36.delete(0,END)
        textm36.focus()
    else:
        textm36.config(state=DISABLED)
        t_m36.set("0")



        
totalFood = 36
for j in range(totalFood):
    globals()["var" + str(j+1)] = IntVar()


totalFood = 36
for k in range(totalFood):
    globals()["t_m" + str(k+1)] = StringVar()


t_m1.set("0")
t_m2.set("0")
t_m3.set("0")
t_m4.set("0")
t_m5.set("0")
t_m6.set("0")
t_m7.set("0")
t_m8.set("0")
t_m9.set("0")
t_m10.set("0")
t_m11.set("0")
t_m12.set("0")
t_m13.set("0")
t_m14.set("0")
t_m15.set("0")
t_m16.set("0")
t_m17.set("0")
t_m18.set("0")
t_m19.set("0")
t_m20.set("0")
t_m21.set("0")
t_m22.set("0")
t_m23.set("0")
t_m24.set("0")
t_m25.set("0")
t_m26.set("0")
t_m27.set("0")
t_m28.set("0")
t_m29.set("0")
t_m30.set("0")
t_m31.set("0")
t_m32.set("0")
t_m33.set("0")
t_m34.set("0")
t_m35.set("0")
t_m36.set("0")


stringPrice = DoubleVar()
priceOfFood=StringVar()
subTotalVar = StringVar()
taxVar=StringVar()
totalCostVar=StringVar()
payCash = DoubleVar()


tfood = Food.listOfFoods()
g=0
for f in tfood:
    g += 1
    globals()["food" + str(g)] = f[3] + f[1]


#Checkbutton and Print of Foods

L1=Label(foodFrame,text="Bucket Meal", justify=CENTER,font=("arial",16,"bold"), fg = "red")
L1.grid(row=0,column=0,sticky=W)
    
m1=Checkbutton(foodFrame,text=food1, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var1,command = m1)
m1.grid(row=1,column=0,sticky=W, padx = (16, 26))

m2=Checkbutton(foodFrame,text=food2, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var2,command = m2)
m2.grid(row=1,column=2,sticky=W, padx = (26, 16))

m3=Checkbutton(foodFrame,text=food3, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var3,command = m3)
m3.grid(row=2,column=0,sticky=W, padx = (16, 26))

m4=Checkbutton(foodFrame,text=food4, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var4,command = m4)
m4.grid(row=2,column=2,sticky=W, padx = (26, 16))

m5=Checkbutton(foodFrame,text=food5, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var5,command = m5)
m5.grid(row=3,column=0,sticky=W, padx = (16, 26))

m6=Checkbutton(foodFrame,text=food6, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var6,command = m6)
m6.grid(row=3,column=2,sticky=W, padx = (26, 16))

L2=Label(foodFrame,text="ChickenJoy", justify=CENTER,font=("arial",16,"bold"), fg = "red")
L2.grid(row=4,column=0,sticky=W)

m7=Checkbutton(foodFrame,text=food7, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var7,command = m7)
m7.grid(row=5,column=0,sticky=W, padx = (16, 26))

m8=Checkbutton(foodFrame,text=food8, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var8,command = m8)
m8.grid(row=5,column=2,sticky=W, padx = (26, 16))

m9=Checkbutton(foodFrame,text=food9, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var9,command = m9)
m9.grid(row=6,column=0,sticky=W, padx = (16, 26))

m10=Checkbutton(foodFrame,text=food10, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var10,command = m10)
m10.grid(row=6,column=2,sticky=W, padx = (26, 16))

L3=Label(foodFrame,text="Jolly Spaghetti", justify=CENTER,font=("arial",16,"bold"), fg = "red")
L3.grid(row=8,column=0,sticky=W)

m11=Checkbutton(foodFrame,text=food11, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var11,command = m11)
m11.grid(row=9,column=0,sticky=W, padx = (16, 26))

m12=Checkbutton(foodFrame,text=food12, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var12,command = m12)
m12.grid(row=9,column=2,sticky=W, padx = (26, 16))

L4=Label(foodFrame,text="Palabok Fiesta", justify=CENTER,font=("arial",16,"bold"), fg = "red")
L4.grid(row=10,column=0,sticky=W)

m13=Checkbutton(foodFrame,text=food13, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var13,command = m13)
m13.grid(row=11,column=0,sticky=W, padx = (16, 26))

L5=Label(foodFrame,text="Chicken Pairs", justify=CENTER,font=("arial",16,"bold"), fg = "red")
L5.grid(row=12,column=0,sticky=W)

m14=Checkbutton(foodFrame,text=food14, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var14,command = m14)
m14.grid(row=13,column=0,sticky=W, padx = (26, 16))

m15=Checkbutton(foodFrame,text=food15, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var15,command = m15)
m15.grid(row=13,column=2,sticky=W, padx = (16, 26))

L6=Label(foodFrame,text="Burger Steaks", justify=CENTER,font=("arial",16,"bold"), fg = "red")
L6.grid(row=14,column=0,sticky=W)

m16=Checkbutton(foodFrame,text=food16, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var16,command = m16)
m16.grid(row=15,column=0,sticky=W, padx = (26, 16))

m17=Checkbutton(foodFrame,text=food17, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var17,command = m17)
m17.grid(row=15,column=2,sticky=W, padx = (16, 26))

L7=Label(foodFrame,text="YumBurgers", justify=CENTER,font=("arial",16,"bold"), fg = "red")
L7.grid(row=16,column=0,sticky=W)

m18=Checkbutton(foodFrame,text=food18, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var18,command = m18)
m18.grid(row=17,column=0,sticky=W, padx = (26, 16))

m19=Checkbutton(foodFrame,text=food19, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var19,command = m19)
m19.grid(row=17,column=2,sticky=W, padx = (16, 26))

L8=Label(foodFrame,text="Chicken Dippers", justify=CENTER,font=("arial",16,"bold"), fg = "red")
L8.grid(row=18,column=0,sticky=W)

m20=Checkbutton(foodFrame,text=food20, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var20,command = m20)
m20.grid(row=19,column=0,sticky=W, padx = (26, 16))

L9=Label(foodFrame,text="Chicken Sandwich", justify=CENTER,font=("arial",16,"bold"), fg = "red")
L9.grid(row=20,column=0,sticky=W)

m21=Checkbutton(foodFrame,text=food21, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var21,command = m21)
m21.grid(row=21,column=0,sticky=W, padx = (16, 26))

m22=Checkbutton(foodFrame,text=food22, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var22,command = m22)
m22.grid(row=21,column=2,sticky=W, padx = (26, 16))

m23=Checkbutton(foodFrame,text=food23, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var23,command = m23)
m23.grid(row=22,column=0,sticky=W, padx = (16, 26))

m24=Checkbutton(foodFrame,text=food24, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var24,command = m24)
m24.grid(row=22,column=2,sticky=W, padx = (26, 16))

L10=Label(foodFrame,text="Side Dish", justify=CENTER,font=("arial",16,"bold"), fg = "red")
L10.grid(row=23,column=0,sticky=W)

m25=Checkbutton(foodFrame,text=food25, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var25,command = m25)
m25.grid(row=24,column=0,sticky=W, padx = (16, 26))

m26=Checkbutton(foodFrame,text=food26, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var26,command = m26)
m26.grid(row=24,column=2,sticky=W, padx = (26, 16))

m27=Checkbutton(foodFrame,text=food27, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var27,command = m27)
m27.grid(row=25,column=0,sticky=W, padx = (16, 26))

m28=Checkbutton(foodFrame,text=food28, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var28,command = m28)
m28.grid(row=25,column=2,sticky=W, padx = (26, 16))

m29=Checkbutton(foodFrame,text=food29, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var29,command = m29)
m29.grid(row=26,column=0,sticky=W, padx = (16, 26))

m30=Checkbutton(foodFrame,text=food30, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var30,command = m30)
m30.grid(row=26,column=2,sticky=W, padx = (26, 16))

m31=Checkbutton(foodFrame,text=food31, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var31,command = m31)
m31.grid(row=27,column=0,sticky=W, padx = (16, 26))

m32=Checkbutton(foodFrame,text=food32, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var32,command = m32)
m32.grid(row=27,column=2,sticky=W, padx = (26, 16))

L11=Label(foodFrame,text="Dessert And Drinks", justify=CENTER,font=("arial",16,"bold"), fg = "red")
L11.grid(row=28,column=0,sticky=W)

m33=Checkbutton(foodFrame,text=food33, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var33,command = m33)
m33.grid(row=29,column=0,sticky=W, padx = (16, 26))

m34=Checkbutton(foodFrame,text=food34, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var34,command = m34)
m34.grid(row=29,column=2,sticky=W, padx = (26, 16))

m35=Checkbutton(foodFrame,text=food35, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var35,command = m35)
m35.grid(row=30,column=0,sticky=W, padx = (16, 26))

m36=Checkbutton(foodFrame,text=food36, justify=LEFT,
               font=("arial",12,"bold"),onvalue=1,offvalue=0,variable=var36,command = m36)
m36.grid(row=30,column=2,sticky=W, padx = (26, 16))



#Input

textm1=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m1)
textm1.grid(row=1,column=1)

textm2=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m2)
textm2.grid(row=1,column=3)

textm3=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m3)
textm3.grid(row=2,column=1)

textm4=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m4)
textm4.grid(row=2,column=3)

textm5=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m5)
textm5.grid(row=3,column=1)

textm6=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m6)
textm6.grid(row=3,column=3)

textm7=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m7)
textm7.grid(row=5,column=1)

textm8=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m8)
textm8.grid(row=5,column=3)

textm9=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m9)
textm9.grid(row=6,column=1)

textm10=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m10)
textm10.grid(row=6,column=3)

textm11=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m11)
textm11.grid(row=9,column=1)

textm12=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m12)
textm12.grid(row=9,column=3)

textm13=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m13)
textm13.grid(row=11,column=1)

textm14=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m14)
textm14.grid(row=13,column=1)

textm15=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m15)
textm15.grid(row=13,column=3)

textm16=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m16)
textm16.grid(row=15,column=1)

textm17=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m17)
textm17.grid(row=15,column=3)

textm18=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m18)
textm18.grid(row=17,column=1)

textm19=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m19)
textm19.grid(row=17,column=3)

textm20=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m20)
textm20.grid(row=19,column=1)

textm21=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m21)
textm21.grid(row=21,column=1)

textm22=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m22)
textm22.grid(row=21,column=3)

textm23=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m23)
textm23.grid(row=22,column=1)

textm24=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m24)
textm24.grid(row=22,column=3)

textm25=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m25)
textm25.grid(row=24,column=1)

textm26=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m26)
textm26.grid(row=24,column=3)

textm27=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m27)
textm27.grid(row=25,column=1)

textm28=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m28)
textm28.grid(row=25,column=3)

textm29=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m29)
textm29.grid(row=26,column=1)

textm30=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m30)
textm30.grid(row=26,column=3)

textm31=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m31)
textm31.grid(row=27,column=1)

textm32=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m32)
textm32.grid(row=27,column=3)

textm33=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m33)
textm33.grid(row=29,column=1)

textm34=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m34)
textm34.grid(row=29,column=3)

textm35=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m35)
textm35.grid(row=30,column=1)

textm36=Entry(foodFrame,font=("arial",12,"bold"),bd=6,width=8,state=DISABLED,textvariable=t_m36)
textm36.grid(row=30,column=3)



#Label

labelSubTotal = Label(bottomFrame, font=("arial",13,"bold"), text = "SubTotal", bg="#00008B",fg="white")
labelSubTotal.grid(row=0,column=0)

textSubTotal=Entry(bottomFrame,font=("arial",13,"bold"),bd=6,width=12,state="readonly",textvariable=subTotalVar)
textSubTotal.grid(row=0,column=1,padx=9)

labelTax=Label(bottomFrame,text="Tax",font=("arial",13,"bold"),bg="#00008B",fg="white")
labelTax.grid(row=0,column=2)

textTax=Entry(bottomFrame,font=("arial",13,"bold"),bd=6,width=12,state="readonly",textvariable=taxVar)
textTax.grid(row=0,column=3,padx=9)

labelTotalCost=Label(bottomFrame,text="Total Cost",font=("arial",13,"bold"),bg="#00008B",fg="white")
labelTotalCost.grid(row=0,column=4)

textTotalCost=Entry(bottomFrame,font=("arial",13,"bold"),bd=6,width=12,state='readonly',textvariable=totalCostVar)
textTotalCost.grid(row=0,column=5,padx=9)

#Buttons

paymentButton=Button(bottomFrame,text="Payment",font=("arial",13,"bold"),bg="#ADD8E6",fg="black", bd=3,padx=5, command = payment)
paymentButton.grid(row=0,column=6,padx=(35, 5))

textPayment=Entry(bottomFrame,font=("arial",13,"bold"),bd=6,width=14, state = "disabled", textvariable = payCash)
textPayment.grid(row=0,column=7,padx=10)

buttonTotal=Button(bottomFrame,text="Total",font=("arial",14,"bold"),fg="black",bg="#ADD8E6",bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=8,padx=(20, 0))

buttonReceipt=Button(bottomFrame,text="Receipt",font=("arial",14,"bold"),fg="black",bg="#ADD8E6",bd=3,padx=5,command=receipt)
buttonReceipt.grid(row=0,column=9)

buttonSave=Button(bottomFrame,text="Save",font=("arial",14,"bold"),fg="black",bg="#ADD8E6",bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=10)

buttonReset=Button(bottomFrame,text="Reset",font=("arial",14,"bold"),fg="black",bg="#ADD8E6",bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=11,padx=(0, 5))


#TextArea

textReceipt=Text(recieptFrame,font=("arial",8,"bold"),bd=3,width=50,height=36, state = DISABLED)
textReceipt.grid(row=0,column=0)

root.mainloop()
