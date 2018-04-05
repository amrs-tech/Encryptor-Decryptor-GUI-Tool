from time import sleep
from tkinter import *

def encrypt():
    global e1, e2
    word = e1.get()
    tempword = ''
    for i in word:
        t = ord(i)<<2
        tempword += chr(t)
    sleep(1)
    e2.delete(0,END)
    e2.insert(0,tempword)
       
def decrypt():
    global e1, e2
    word = e1.get()
    dec = ''
    for i in word:
        t = chr(ord(i)>>2)
        dec += t

    sleep(1)
    e2.delete(0,END)
    e2.insert(0,dec)



root = Tk()

root.title('CryptoGUI')

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
#e1.pack(side=RIGHT)
#e2.pack(side=RIGHT)
e1.focus_set()



l1 = Label(root, text="Input").grid(row=0, column=0)
l2 = Label(root, text="Answer").grid(row=1, column=0)
#l1.pack(fill=BOTH, side=LEFT, padx=5, pady=5)
#l2.pack(fill=BOTH, side=LEFT, padx=5, pady=5)


b1 = Button(root,text='Encrypt',command=encrypt).grid(row=3, column=0)
b2 = Button(root,text='Decrypt',command=decrypt).grid(row=3, column=1)

#b1.pack(fill=BOTH, side=BOTTOM, padx=5, pady=5)
#b2.pack(fill=BOTH, side=BOTTOM, padx=5, pady=5)

root.mainloop()

'''
word = input('Enter word to encrypt: ')
tempword = ''
for i in word:
    t = ord(i)<<2
    tempword += chr(t)

print('Encrypted word: '+tempword)

sleep(1)

dec = ''
for i in tempword:
    t = chr(ord(i)>>2)
    dec += t

print('Decrypted word: '+dec)'''
