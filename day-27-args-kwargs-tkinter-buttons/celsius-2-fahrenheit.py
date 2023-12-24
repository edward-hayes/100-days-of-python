import tkinter as tk

FONT = ('Ubuntu Mono',16)

window = tk.Tk()
window.title("Celsius To Fahrenheit")
window.minsize(width=300, height= 200)
window.config(padx=20, pady=20)

def to_fahrenheit(celsius):
    return (float(celsius)*(9/5) + 32)

#Entry Box

entry_celsius = tk.Entry(width=5)
entry_celsius.grid(row=0,column=1)

#Labels
label_degrees_c = tk.Label(text="°C", font = FONT)
label_degrees_c.grid(row=0, column=2)

label_is_equal = tk.Label(text="is equal to", font = FONT)
label_is_equal.grid(row=1,column=0)

label_result_f = tk.Label(text=0, font = FONT)
label_result_f.grid(row=1,column=1)

label_degrees_f = tk.Label(text="°F", font = FONT)
label_degrees_f.grid(row=1,column=2)

#Button
def calculate():
    result = to_fahrenheit(entry_celsius.get())
    label_result_f["text"] = result

button_calculate = tk.Button(text="Calculate", command=calculate)
button_calculate.grid(row=2,column=1)


window.mainloop()
