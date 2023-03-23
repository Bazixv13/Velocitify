import os
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import importlib.util

# Load the firston.py file
spec = importlib.util.spec_from_file_location("firston", "firston.py")
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)

root = tk.Tk()
root.geometry("350x150")
root.resizable(False, False)
root.title("")
root.wm_iconbitmap("configs.ico")
root.iconbitmap("configs.ico")

on_var = tk.BooleanVar(value=config.on)

def save_values():
    config.on = on_var.get()
    with open("firston.py", "w") as f:
        f.write(f"on = {config.on}")
    messagebox.showinfo("Settings Saved", "Your settings have been saved successfully.")
    
def cancel():
    root.destroy()

def open_help():
    messagebox.showinfo("INFO", "If this box is not checked, the program will attempt to download libraries otherwise, it will skip that part. (by default its set to true)")
    
def show_tooltip():
    tooltip = tk.Toplevel(root)
    tooltip.wm_overrideredirect(True)
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    tooltip.geometry(f"+{x}+{y}")
    label = tk.Label(tooltip, text="If this box is not checked, the program will attempt to download\n libraries otherwise, it will skip that part. (by default its set to true)", bg="white", relief="solid", borderwidth=1)
    label.pack()
    label.after(2500, tooltip.destroy)

ttk.Label(root, text="       Script Settings", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=(20, 10))
ttk.Label(root, text="libraries downloaded:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=20, pady=5)
ttk.Checkbutton(root, variable=on_var, onvalue=True, offvalue=False, cursor="hand2").grid(row=1, column=1, sticky="e", pady=5)

question_button = ttk.Button(root, text='?', command=open_help, width=2, padding=2)
question_button.grid(row=1, column=2, pady=(0), padx=(10, 0))
question_button.bind("<Enter>", lambda e: show_tooltip())

ttk.Button(root, text="Cancel", command=cancel).grid(row=2, column=0, pady=(20, 10), padx=(20, 5), sticky="w")
ttk.Button(root, text="Save", command=save_values).grid(row=2, column=1, pady=(20, 10), padx=(5, 20), sticky="e")

root.update_idletasks()
root.geometry(f"+{(root.winfo_screenwidth() - root.winfo_width()) // 2}+{(root.winfo_screenheight() - root.winfo_height()) // 2}")
root.deiconify()

root.mainloop()
