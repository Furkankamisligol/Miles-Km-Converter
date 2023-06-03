from tkinter import *


def button_got_clicked():
    miles = float(input1.get())
    km = str(miles*1.609)
    km_label.config(text=km)


def copy_button_got_clicked():
    metin = km_label["text"]
    window.clipboard_clear()
    window.clipboard_append(metin)


window = Tk()
window.title("GUI Program")
window.minsize(width=200, height=300)
window.config(padx=20, pady=20)

info_label = Label(text="Miles to Kilometer Converter", font=("Ariel", 24,))
info_label.grid(row=0, column=3, padx=5, pady=5)

km_label = Label(text="", font=("Ariel", 24,))
km_label.grid(row=4, column=3, padx=5, pady=5)

km_label_1 = Label(text="KM", font=("Ariel", 24,))
km_label_1.grid(row=4, column=4, padx=5, pady=5)


button = Button(text="Convert", command=button_got_clicked, font=("Ariel", 24,))
button.grid(row=3, column=0, padx=5, pady=5)

input1 = Entry(width=10, font=("Ariel", 24,))
input1.grid(row=1, column=3, padx=5, pady=5)

mile_label = Label(text="Miles", font=("Ariel", 24,))
mile_label.grid(row=1, column=4, padx=5, pady=5)

copy_button = Button(text="Copy", command=copy_button_got_clicked, font=("Ariel", 16,))
copy_button.grid(row=5, column=4, padx=5, pady=5)

window.mainloop()
