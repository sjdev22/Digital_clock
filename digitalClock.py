fro tkinter import Tk, Label

wondow = Tk()
window.title("Digital Clock")
winddow.geometry("600*300")
window.configure(bg="steelblue")

label = Label(window, font=("Arial Black",78,"bold"), bg="steelblue", fg="white")
label.pack(pady=100)

window.mainloop()