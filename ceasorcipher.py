import tkinter as tk
from tkinter import ttk, messagebox

# Caesar cipher logic
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# Process input
def process_text():
    message = entry_message.get()
    shift_text = entry_shift.get()

    if not message.strip():
        messagebox.showwarning("Input Missing", "Please enter a message.")
        return

    if not shift_text.strip().isdigit():
        messagebox.showwarning("Invalid Input", "Shift must be a positive integer.")
        return

    shift = int(shift_text)
    mode = combo_mode.get()
    result = caesar_cipher(message, shift, 'encrypt' if mode == "Encrypt" else 'decrypt')
    result_var.set(result)

# Clear all fields
def clear_fields():
    entry_message.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    result_var.set("")
    combo_mode.current(0)

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("450x350")
root.configure(bg="#f0f4f7")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Caesar Cipher Encryption & Decryption", font=("Helvetica", 14, "bold"), bg="#f0f4f7", fg="#2c3e50").pack(pady=15)

# Message Input
tk.Label(root, text="Message:", bg="#f0f4f7").pack()
entry_message = tk.Entry(root, width=50, font=("Helvetica", 10))
entry_message.pack(pady=5)

# Shift Input
tk.Label(root, text="Shift Value:", bg="#f0f4f7").pack()
entry_shift = tk.Entry(root, width=20, font=("Helvetica", 10))
entry_shift.pack(pady=5)

# Mode Selection
tk.Label(root, text="Select Mode:", bg="#f0f4f7").pack()
combo_mode = ttk.Combobox(root, values=["Encrypt", "Decrypt"], state="readonly", width=20)
combo_mode.current(0)
combo_mode.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#f0f4f7")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Process", command=process_text, bg="#3498db", fg="white", padx=10).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Clear", command=clear_fields, bg="#e74c3c", fg="white", padx=10).grid(row=0, column=1, padx=10)

# Result Display
tk.Label(root, text="Result:", bg="#f0f4f7").pack(pady=5)
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, width=50, font=("Helvetica", 10), state='readonly')
result_entry.pack()

# Start GUI loop
root.mainloop()
