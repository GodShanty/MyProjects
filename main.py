import os
import subprocess
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttk

# Create the main window with fullscreen
main = ttk.Window(themename="superhero")
main.title("Billing System")
main.attributes('-fullscreen', True)
main.configure(background="#ffffff")

def Exit():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=main):
        main.destroy()

main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    emp_page = os.path.abspath("employee.py")
    print("Opening Employee:", emp_page)  # Debug print
    try:
        subprocess.Popen(["python", emp_page], creationflags=subprocess.CREATE_NO_WINDOW)
        main.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open employee.py:\n{e}")

def adm():
    admin_page = os.path.abspath("admin.py")
    print("Opening Admin:", admin_page)  # Debug print
    try:
        subprocess.Popen(["python", admin_page], creationflags=subprocess.CREATE_NO_WINDOW)
        main.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open admin.py:\n{e}")

# Get screen dimensions
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# Canvas for background
canvas = Canvas(main, width=screen_width, height=screen_height, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Load and display background image
bg_image = Image.open("images/background.png")
bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Load button images
emp_icon = PhotoImage(file="images/1.png")
adm_icon = PhotoImage(file="images/2.png")

# Button size and positions
button_width = 160
button_height = 160
button_x = screen_width - button_width - 60
emp_button_y = int(screen_height * 0.3)
adm_button_y = int(screen_height * 0.55)

# Custom style
style = ttk.Style()
style.configure("Custom.TButton", borderwidth=0)

# Employee Button
emp_button = ttk.Button(main, image=emp_icon, style="Custom.TButton", command=emp)
canvas.create_window(button_x, emp_button_y, anchor="nw", window=emp_button, width=button_width, height=button_height)

# Admin Button
adm_button = ttk.Button(main, image=adm_icon, style="Custom.TButton", command=adm)
canvas.create_window(button_x, adm_button_y, anchor="nw", window=adm_button, width=button_width, height=button_height)

main.mainloop()
