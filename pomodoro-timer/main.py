import math
from time import time
import tkinter as tk


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Ubuntu Mono"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    label_timer["text"] = "Timer"
    canvas.itemconfig(timer_text, text = "00:00")
    label_checkmark["text"] = ""
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def state_short_break():
    label_timer["text"] = "Break Time"
    break_sec = SHORT_BREAK_MIN*60
    count_down(break_sec)

def state_long_break():
    label_timer["text"] = "Break Time"
    break_sec = LONG_BREAK_MIN*60
    count_down(break_sec)

def state_work():
    label_timer["text"] = "Work Time"
    work_sec = WORK_MIN*60
    count_down(work_sec)


def start_timer():
    global reps
    reps += 1

    if reps == 7:
        state_long_break()
    elif reps % 2 == 0:
        state_short_break()
    elif reps % 2 != 0:
        state_work()



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(current_count):
    global reps

    count_min = math.floor(current_count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    
    count_sec = current_count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if current_count > 0:
        global timer
        timer = window.after(1000, count_down, current_count -1)
    else:
        print(reps)
        if reps % 2 == 0:
            checkmarkstring = ""
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                checkmarkstring += "✔" 
            label_checkmark["text"] = checkmarkstring
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

#tomato img
canvas = tk.Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font = (FONT_NAME, 35))
canvas.grid(row=1,column=1)

#labels
label_timer = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font= (FONT_NAME, 40, 'bold'))
label_timer.grid(row=0, column=1)

label_checkmark = tk.Label(fg=GREEN, bg=YELLOW, font= (FONT_NAME, 16))
label_checkmark.grid(row=3,column=1)

#buttons
button_start = tk.Button(text="Start", command=start_timer, font=(FONT_NAME,16), highlightthickness=0, highlightbackground=YELLOW)
button_start.grid(row=2,column=0)

button_reset = tk.Button(text="Reset", command=reset_timer, bg=YELLOW, font=(FONT_NAME,16), highlightthickness=0, highlightbackground=YELLOW)
button_reset.grid(row=2,column=2)

window.mainloop()
