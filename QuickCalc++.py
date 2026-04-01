import tkinter as tk
import random

# The actual values we need for a calculator
REAL_VALUES = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# A list of confusing labels to put on the buttons
DECEPTIVE_LABELS = [
    "Error", "Wait", "Huh?", "X", "Z", 
    "No", "Help", "???", "Q", "404", 
    "Void", "!", "Alt", "Cmd", "End", "Ok"
]

def calculate():
    responses = [
        "uhh i don't know really",
        "no",
        "maybe later",
        "calculating... psyche!",
        "ask a friend",
        "error 418: i'm a teapot"
    ]
    result_var.set(random.choice(responses))

def add_to_expr(char):
    entry.insert(tk.END, char)

def clear():
    entry.delete(0, tk.END)
    result_var.set("")

root = tk.Tk()
root.title("QuickCalc++ by Vladimir43565")
root.geometry("400x500")

entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify="right")
entry.pack(fill="both", padx=10, pady=20)

result_var = tk.StringVar()
label = tk.Label(root, textvariable=result_var, font=("Arial", 14, "italic"), fg="red", wraplength=350)
label.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

# Shuffle the actual math values so they are in random positions
shuffled_values = REAL_VALUES.copy()
random.shuffle(shuffled_values)

# Shuffle the deceptive labels
random_labels = random.sample(DECEPTIVE_LABELS, len(DECEPTIVE_LABELS))

row = 0
col = 0

for i in range(len(shuffled_values)):
    actual_value = shuffled_values[i]
    display_text = random_labels[i]
    
    # Assign the command based on the HIDDEN actual value
    if actual_value == "=":
        cmd = calculate
    elif actual_value == "C":
        cmd = clear
    else:
        # We use a default argument to 'capture' the current actual_value in the loop
        cmd = lambda x=actual_value: add_to_expr(x)
        
    btn = tk.Button(buttons_frame, text=display_text, width=8, height=3, 
                    font=("Arial", 10, "bold"), command=cmd)
    btn.grid(row=row, column=col, padx=2, pady=2)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()