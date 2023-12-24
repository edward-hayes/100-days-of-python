import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height= 300)
window.config(padx=20, pady=20)

#label
my_label = tk.Label(text="I am a Label", font = ("Arial,", 24, "bold"))
my_label.grid(column=0, row=0)

#button1
def button_clicked():
    my_label["text"] = input.get()
   

button1 = tk.Button(text="Click Me", command=button_clicked)
button1.grid(column=1,row=1)

#button2
button2 = tk.Button(text="new button")
button2.grid(column=2,row=0)

#entry
input = tk.Entry(width=10)
input.grid(column=3,row=2)

window.mainloop()
