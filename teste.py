import tkinter as tk 
from tkinter import *
import random 
from tkinter import messagebox


root = tk.Tk ()
root.title("Bô?")
root.geometry('600x600')
root.configure(background='#8494FF')


def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 50:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
    button_1.place(x=x, y=y)
        

def accepted():
            messagebox.showinfo( 
                   'Hehe', 'só marcar o dia 😮‍💨')



def denied():
        button_1.destory()


margin = Canvas(root, width=500, bg='#8494FF', height=100,
                bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#8494FF', text='Poderia deixar eu sentar?',
                fg='#000000', font=('Monntserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#ff0000', command=denied,
                     relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
root.bind('<Motion>', move_button_1)
button_2 = tk.Button(root, text='Sim', bg='#00ff00', relief=RIDGE, 
                     bd=3, command=accepted, font= ('Montserrat', 14, 'bold'))
button_2.pack()


root.mainloop()
