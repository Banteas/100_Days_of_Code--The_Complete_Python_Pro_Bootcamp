from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


equal_label = Label(window, text="is equal to")
equal_label.grid(column=0, row=1)

miles_label2 = Label(window, text="Miles")
miles_label2.grid(column=2, row=0)

km_label3 = Label(window, text="Km")
km_label3.grid(column=2, row=1)

conv_label4 = Label(window, text="-")
conv_label4.grid(column=1, row=1)

my_entry2 = Entry(window, width=10)
my_entry2.grid(column=1, row=0)

def convert_miles():
    km = round(float(my_entry2.get()) * 1.60934, 2)
    conv_label4.config(text=f"{km}")

my_button = Button(window, text="Convert", command= convert_miles)
my_button.grid(column=1, row=2)



window.mainloop()