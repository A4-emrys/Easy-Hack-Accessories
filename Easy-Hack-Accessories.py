import tkinter as tk
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import time

window = tk.Tk()
window.title('+HiddenEYE')
window.geometry('560x550')
window.resizable(width=False, height=False)


bg = ImageTk.PhotoImage(file='background1.png')
bg2 = ImageTk.PhotoImage(file='background2.png')

canvas = tk.Canvas(window, highlightthickness=0)
canvas.create_image(0, 0, image=bg, anchor='nw')
canvas.create_text(274, 80, text="+HiddenEYE", font=('times', 25, 'bold'), fill='white', )
canvas.create_text(280, 180,text='Login', font=('times', 15, 'bold'), fill='white',)
canvas.pack(fill='both', expand=True)

email_entry = tk.Entry(font=('times', 12), width=19, fg='#5c8a8a')
email_entry.place(x=200, y=220)
email_entry.focus()

pass_entry = tk.Entry(font=('times', 12), width=19, fg='#5c8a8a')
pass_entry.place(x=200, y=270)
pass_entry.focus()

email_entry.insert(0, 'email:')
pass_entry.insert(0, 'pass:')


log_button = tk.Button(text='Login',bd=2, font=('times', 10, 'bold'), fg='white', bg='#006622', width=12, command=lambda:login())
log_button.place(x=230, y=333)


def login():
    time.sleep(0.1)
    if email_entry.get() == '':
        messagebox.showerror('Error', 'Please fill in the entries!')
        email_entry.focus()

    elif pass_entry.get() == '':
        messagebox.showerror('Error', 'Please fill in the entries!')
        pass_entry.focus()

    elif email_entry.get() != 'youremail@gmail.com':
        messagebox.showerror('Error', 'email is not correct!')
        email_entry.focus()

    elif pass_entry.get() != '12345':
        messagebox.showerror('Error', 'Password is incorrect')
        pass_entry.focus()

    elif email_entry.get() == 'youremail@gmail.com' and pass_entry.get() == '12345':
        canvas.destroy()
        email_entry.destroy()
        log_button.destroy()
        pass_entry.destroy()


        lg_canvas = tk.Canvas(window,width=560, height=550,highlightthickness=0)
        lg_canvas.create_image(0, 0, image=bg2, anchor='nw')
        lg_canvas.create_text(270, 60, text='Welcome back to the +HiddenEYE', font=('times', 23, 'bold'), fill='white')
        lg_canvas.create_text(90, 130, text='- Choose a Device', font=('times', 13, 'bold'), fill='white')
        lg_canvas.create_text(115, 225, text='- Choose a Device name', font=('times', 13, 'bold'), fill='white')
        lg_canvas.create_text(90, 318, text='- Model Number', font=('times', 13, 'bold'), fill='white')
        lg_canvas.create_text(90, 405, text='- Serial Number', font=('times', 13, 'bold'), fill='white')
        lg_canvas.pack()

        device_entry = ttk.Combobox(font=('times', 11, 'italic'), state= 'readonly')
        device_entry ['values'] = ('iOS', 'Android', 'Windows', 'Other')
        device_entry.place(x=34, y=155)

        name_entry = ttk.Combobox(font=('times', 11, 'italic'), state= 'readonly')
        name_entry ['values'] = ('iPhone 12Pro MAX', 'MACBOOK Pro', 'Samsung Galaxy S10', 'HP Pavilion')
        name_entry.place(x=34, y=248)

        modle_id = tk.Entry(font=('times new roman', 11, 'italic'), width=22)
        modle_id.place(x=34, y=342)
        modle_id.insert(0, 'ex: MHK53LL/A')

        serial = tk.Entry(font=('times', 11, 'italic'), width=22)
        serial.place(x=34, y=425)
        serial.insert(0, 'ex: XYRTDDJ2G50G63')

        hack_button = tk.Button(text='Hack', fg='white',bg='#006622', font=('times', 12, 'bold'), width=10, command=lambda:start())
        hack_button.place(x=370, y=248)


        logout = tk.Button(text='Logout', fg='white', bg='red', font=('times', 12, 'bold'), width=10,)
        logout.place(x=370, y=320)


        def start():
            lg_canvas.destroy()
            device_entry.destroy()
            name_entry.destroy()
            modle_id.destroy()
            serial.destroy()
            hack_button.destroy()
            logout.destroy()

            

            new_canvas = tk.Canvas(window, bg='#1f1f2e', width=560, height=550,highlightthickness=0)
            new_canvas.create_text(250, 138, text='Hacking.... %$^#^%$#&%$*&', font=('roboto', 12, 'bold'), fill='white')
            new_canvas.pack()


            bar = ttk.Progressbar(orient='horizontal', length=300)
            bar.place(x=135, y=160)
            task = 10
            x = 0

            while(x<task):
                time.sleep(1)
                bar ['value']+=10
                x+=1
                window.update_idletasks()
                time.sleep(1)
            new_canvas.destroy()
            window.update_idletasks()
            canvas1 = tk.Canvas(window, bg='#1f1f2e', width='560', height=550, highlightthickness=0)
            canvas1.create_text(280, 169, text='100% COMPLETED ✔', font=('times', 25, 'bold'), fill='green')
            canvas1.pack()

            data = tk.Button(text='Download data', fg='green', font=('roboto', 12, 'italic'), padx=6, command=lambda:start1())
            data.place(x=225, y=265)
            def start1():
                bar1 = ttk.Progressbar(orient='horizontal', length=300)
                bar1.place(x=133, y=330)
                task1 = 10
                x1 = 0

                while(x1<task1):
                    time.sleep(1)
                    bar1 ['value']+=10
                    x1+=1
                    window.update_idletasks()
                mark = tk.Label(text='Done ✔', fg='green', bg='#1f1f2e', font=('times',15, 'bold'))
                mark.place(x=245, y=370)

window.mainloop()
