import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = "0" + str(seconds)
    count_text = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
        print(count)
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Labels

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
timer.grid(row=0, column=1)

checkmark = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
checkmark.grid(row=3, column=1)

# Buttons

start = Button(text='Start', highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text='Reset', bg=YELLOW, highlightthickness=0)
reset.grid(row=2, column=2)

# colocar una imagen en la ventana
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)




window.mainloop()
