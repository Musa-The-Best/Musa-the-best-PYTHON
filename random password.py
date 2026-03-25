import tkinter as tk
import random
import string
def generate():
    length = int(entry.get())
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    result.config(text=password)
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")
tk.Label(root, text="Password Length:").pack(pady=10)
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Generate", command=generate).pack(pady=10)
result = tk.Label(root, text="", font=("Courier", 12, "bold"), fg="blue")
result.pack(pady=10)
root.mainloop()