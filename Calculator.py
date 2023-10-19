import tkinter as tk

def button_click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

window = tk.Tk()
window.title("Calculator")
window.geometry("250x400")
window.configure(bg="gray")

entry = tk.Entry(window, font=("TkDefaultFont", 20))
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=10)

button_texts = (
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    ".", "0", "=", "/",
    "C"
)

row, col = 1, 0
for button_text in button_texts:
    button = tk.Button(window, text=button_text, font=("TkDefaultFont", 15), padx=10, pady=10, width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
    button.bind("<Button-1>", button_click)

for i in range(1, 6):
    window.grid_rowconfigure(i, weight=1)

for i in range(4):
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
