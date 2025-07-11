import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Too Short", "Password length must be at least 4!")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")
        return

    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    all_chars = lower + upper + digits + symbols
    if not all_chars:
        messagebox.showerror("No Options Selected", "Please select at least one character type.")
        return

    # Ensure at least one character from each selected type
    password = [random.choice(lower), random.choice(upper)]
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    remaining = length - len(password)
    password += random.choices(all_chars, k=remaining)
    random.shuffle(password)
    result.set(''.join(password))

# ------------------ GUI Layout ------------------
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.resizable(False, False)
window.configure(bg="#9e3697")

# Widgets
tk.Label(window, text="Enter Password Length:", bg="#9e3697", fg="black", font=("Arial", 12)).pack(pady=10)
length_entry = tk.Entry(window, font=("Arial", 12), width=10)
length_entry.pack()

digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(window, text="Include Numbers (0-9)", variable=digits_var, bg="#9e3697", font=("Arial", 10)).pack()
tk.Checkbutton(window, text="Include Symbols (!@#$)", variable=symbols_var, bg="#9e3697", font=("Arial", 10)).pack()

tk.Button(window, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=20)

result = tk.StringVar()
tk.Entry(window, textvariable=result, font=("Arial", 12), justify='center', width=30).pack(pady=10)

window.mainloop()
