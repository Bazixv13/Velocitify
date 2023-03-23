import os
import sys
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import time
import webbrowser

current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

# Construct the path to the config.py file
config_file = os.path.join(current_dir, "config.py")

# Import the config module
sys.path.insert(0, current_dir)

import config

# Determine the path to the executable (needed for PyInstaller)
if hasattr(sys, '_MEIPASS'):
    # Running as PyInstaller executable
    base_dir = sys._MEIPASS
else:
    # Running as normal Python script
    base_dir = os.path.abspath(os.path.dirname(__file__))

root = tk.Tk()
root.geometry("490x290")
root.resizable(False, False)
root.title("Script Settings")
root.iconbitmap(os.path.join(base_dir, "configs.ico"))
root.wm_iconbitmap(os.path.join(base_dir, "configs.ico"))

typing_animation = tk.BooleanVar(value=config.typing_animation)
loading_bars = tk.BooleanVar(value=config.loading_bars)
manual_typing_animation_speed = tk.BooleanVar(value=config.manual_typing_animation_speed)
typing_animation_speed = tk.DoubleVar(value=config.typing_animation_speed)
bot_token = tk.StringVar(value=config.bot_token)

def save_values():
    config.typing_animation = typing_animation.get()
    config.loading_bars = loading_bars.get()
    config.manual_typing_animation_speed = manual_typing_animation_speed.get()
    config.typing_animation_speed = typing_animation_speed.get()
    config.bot_token = bot_token.get()
    config.save_config()
    def fixcofig():
        time.sleep(0.1)
        ta = config.typing_animation
        lb = config.loading_bars
        mtas = config.manual_typing_animation_speed
        tas = config.typing_animation_speed
        bt = config.bot_token
        with open('config.py', 'w') as f:
            f.write(f"typing_animation = {ta}\n")
            f.write(f"loading_bars = {lb}\n")
            f.write(f"manual_typing_animation_speed = {mtas}\n")
            f.write(f"typing_animation_speed = {tas}\n")
            f.write(f"bot_token = '{bt}'\n")
            f.write("def save_config():\n")
            f.write("    import os\n")
            f.write("""    with open('config.py', 'w') as f:\n""")
            f.write("""        f.write(f"typing_animation = {typing_animation}\\n")\n""")
            f.write("""        f.write(f"loading_bars = {loading_bars}\\n")\n""")
            f.write("""        f.write(f"manual_typing_animation_speed = {manual_typing_animation_speed}\\n")\n""")
            f.write("""        f.write(f"typing_animation_speed = {typing_animation_speed}\\n")\n""")
            f.write("""        f.write(f"bot_token = '{bot_token}'\\n")\n""")
        
    fixcofig()
    dsf = messagebox.askyesno("Settings Saved", "Your settings have been saved successfully. Exit?")
    if dsf == True:
        root.destroy()
    else:
        pass

def open_bing():
    webbrowser.open("https://scribehow.com/embed-preview/Discord_Workflow__n3Jb3W73SVmpY49ZaBcxAA?size=small&skipIntro=true&removeLogo=true&as=default&preview=true")
def show_tooltip():
    tooltip = tk.Toplevel(root)
    tooltip.wm_overrideredirect(True)
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    tooltip.geometry(f"+{x}+{y}")
    label = tk.Label(tooltip, text="Click for help", bg="white", relief="solid", borderwidth=1)
    label.pack()
    label.after(1500, tooltip.destroy)
    
    
def show_tooltip2():
    tooltip2 = tk.Toplevel(root)
    tooltip2.wm_overrideredirect(True)
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    tooltip2.geometry(f"+{x}+{y}")
    label = tk.Label(tooltip2, text="The amount of time it takes to type one letter (will only take effect \nif you have enabled manual typing animation speed above).", bg="white", relief="solid", borderwidth=1)
    label.pack()
    label.after(1500, tooltip2.destroy)
    
def fsd():
    messagebox.showinfo("INFO","The amount of time it takes to type one letter (will only take effect if you have enabled manual typing animation speed above).")

def cancel():
    result = messagebox.askyesno("Warning", "If you haven't saved your changes, all of them will be lost.\nDo you want to Continue?")
    if result == True:
        root.destroy()
    else:
        pass
        
root.protocol("WM_DELETE_WINDOW", cancel)

ttk.Label(root, text="      Script Settings", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=(20, 10))
ttk.Label(root, text="Typing animation:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=20, pady=5)
ttk.Checkbutton(root, variable=typing_animation, onvalue=True, offvalue=False, cursor="hand2").grid(row=1, column=1, sticky="e", pady=5)
ttk.Label(root, text="Loading bars:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=20, pady=5)
ttk.Checkbutton(root, variable=loading_bars, onvalue=True, offvalue=False, cursor="hand2").grid(row=2, column=1, sticky="e", pady=5)
ttk.Label(root, text="Manual typing animation speed:", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", padx=20, pady=5)
ttk.Checkbutton(root, variable=manual_typing_animation_speed, onvalue=True, offvalue=False, cursor="hand2").grid(row=3, column=1, sticky="e", pady=5)
ttk.Label(root, text="Manual typing animation speed:", font=("Helvetica", 12)).grid(row=4, column=0, sticky="w", padx=20, pady=5)
ttk.Entry(root, textvariable=typing_animation_speed, font=("Helvetica", 12), width=10).grid(row=4, column=1, sticky="e", pady=5)
question2_button = ttk.Button(root, text='?', command=fsd, width=2, padding=2)
question2_button.grid(row=4,column=2,pady=(0), padx=(10, 0))
question2_button.bind("<Enter>", lambda e: show_tooltip2())
ttk.Label(root, text="Bot token:", font=("Helvetica", 12)).grid(row=5, column=0, sticky="w", padx=20, pady=5)
ttk.Entry(root, textvariable=bot_token, font=("Helvetica", 12)).grid(row=5,column=1,pady=5)
question_button = ttk.Button(root, text='?', command=open_bing, width=2, padding=2)
question_button.grid(row=5,column=2,pady=(0), padx=(10, 0))
question_button.bind("<Enter>", lambda e: show_tooltip())
ttk.Button(root, text="Cancel", command=cancel).grid(row=6, column=0, pady=(20, 10), padx=(20, 5), sticky="w")
ttk.Button(root, text="Save", command=save_values).grid(row=6, column=1, pady=(20, 10), padx=(5, 20), sticky="e")


root.update_idletasks()
root.geometry(f"+{(root.winfo_screenwidth() - root.winfo_width()) // 2}+{(root.winfo_screenheight() - root.winfo_height()) // 2}")
root.deiconify()

root.mainloop()
