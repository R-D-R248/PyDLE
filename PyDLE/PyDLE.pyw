import os
import sys
import subprocess
import tkinter as tk
from tkinter import PhotoImage
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
try:
    from PIL import Image, ImageTk
except:
    os.system("pip install pillow")
    from PIL import Image, ImageTk

path = os.path.dirname(os.path.realpath(__file__))
tile_path = os.path.join(path, "tiles.png")
logo_path = os.path.join(path, "Logo.png")

dark_mode = 0

def run():
    file_path = filedialog.askopenfilename(
        filetypes=[("Python files", "*.py *.pyw *.pyi")],
        title="Open Python File"
    )

    
    if not file_path:
        return
    
    IDLE = messagebox.askyesno("Run File", "Do you want to run in IDLE?")
    
    file_dir = os.path.dirname(file_path)
    os.chdir(file_dir)

    if IDLE:
        python_exe = sys.executable
        subprocess.Popen([python_exe, "-m", "idlelib", "-r", file_path])
    else:
        GUI = messagebox.askyesno("Run File", "Is your program GUI-based?")
        if GUI:
            subprocess.Popen(["pythonw", file_path])
        else:
            subprocess.Popen(["cmd", "/k", "python", file_path])

def pipinstall(pack):
    os.system(f"pip install {pack} && pause")

def pip():
    pip_win = tk.Tk()
    pip_win.title("PyDLE Library")
    pip_win.geometry("800x600")
    entry = tk.Entry(pip_win, width=30)
    entry.pack(padx=20, pady=20)
    install_button = tk.Button(pip_win, text="Install", command=lambda: pipinstall(entry.get()))
    install_button.pack()
    pip_win.mainloop()

def save_text(text_content, coding_area, text_widget):
    file = filedialog.asksaveasfile(defaultextension=".py", filetypes=[("Python Files", "*.py;*.pyw;*.pyi")])
    
    if file:
        file.write(text_content)
        file.close()
        file_path = file.name
        file_name = os.path.basename(file_path)
        coding_area.title(file_name)
        return file_name

def create(content=None, file_name="Untitled"):
    coding_area = tk.Tk()
    coding_area.title(file_name)

    coding_area.state("zoomed")
    
    toolbar = tk.Frame(coding_area)
    toolbar.pack(side="top", anchor="nw", pady=10, padx=10)
    
    text_widget = tk.Text(coding_area, height=48, width=600)
    text_widget.pack()

    save_button = tk.Button(toolbar, text="Save", command=lambda: save_text(text_widget.get("1.0", "end-1c"), coding_area, text_widget))
    save_button.pack(side="left", padx=5)
    
    pip_button = tk.Button(toolbar, text="Install Package", command=pip)
    pip_button.pack(side="left", padx=5)
    
    if content:
        text_widget.insert("1.0", f"{content}")

    coding_area.bind('<Control-s>', lambda event: save_text(text_widget.get("1.0", "end-1c"), coding_area, text_widget))
    
    coding_area.mainloop()

def openf():
    file_path = filedialog.askopenfilename(
        filetypes=[("Python files", "*.py *.pyw *.pyi")],
        title="Open Python File"
    )
    
    if file_path:
        with open(file_path, "r") as f:
            content = f.read()
        file_name = os.path.basename(file_path)
        create(content, file_name)

root = tk.Tk()
root.title("PyDLE")
root.geometry("800x600")
root.resizable(False, False)

tile = PhotoImage(file=tile_path)
small_tile = tile.subsample(2, 2)

logo = PhotoImage(file=logo_path)

canvas = tk.Canvas(root, width=800, height=600)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

for x in range(0, 800, small_tile.width()):
    for y in range(0, 600, small_tile.height()):
        canvas.create_image(x, y, image=small_tile, anchor="nw")

canvas.create_image(0, 0, image=logo, anchor="nw")

ui = tk.Frame(root, bg="#ffffff", bd=2)
ui.place(x=120, y=20)

create_button = tk.Button(canvas, text="Create", command=create)
create_button.pack(anchor="center", pady=(180,10))

open_button = tk.Button(canvas, text="Open", command=openf)
open_button.pack(anchor="center", pady=10)

run_button = tk.Button(canvas, text="Run", command=run)
run_button.pack(anchor="center", pady=10)

root.bind('<Control-o>', lambda e: openf() or "break")
root.bind('<Control-r>', lambda e: run() or "break")
root.bind('<Control-n>', lambda e: create() or "break")

root.mainloop()
