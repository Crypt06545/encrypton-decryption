

from tkinter import *
from tkinter import messagebox

import base64
import os



def decrypt():
    password=code.get()

    if password =="056464":
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message=text1.get(1.0,END)
        decode_messege=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_messege)
        decrypt=base64_bytes.decode("ascii")


        Label(screen2,text="Decrypt",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="Robote 10", bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)


        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("decryptio","Input password")

    elif password !="1234":
        messagebox.showerror("decryption","Invaild password")


def encrypt():
    password=code.get()

    if password =="1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message=text1.get(1.0,END)
        encode_messege=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_messege)
        encrypt=base64_bytes.decode("ascii")


        Label(screen1,text="Encrypt",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Robote 10", bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)


        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encryptio","input password")

    elif password !="1234":
        messagebox.showerror("encryption","Invaild password")


def main_screen():
    global screen
    global code
    global text1


    screen=Tk()
    screen.geometry("375x398")

    image_icon=PhotoImage(file="enp-dep\\keys.png")
    screen.iconphoto(False,image_icon)

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter Text For Encryption", fg="black",font=("calbri",13)).place(x=10,y=10)
    text1=Text(font="Robot 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
    
    Label(text="Enter Secret Key for encryption",fg="black",font=("calbri",13)).place(x=10,y=170)
    
    code=StringVar()
    Entry(textvariable=code,width=20,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)




    screen.title("pctApp")
    screen.mainloop()

main_screen()
