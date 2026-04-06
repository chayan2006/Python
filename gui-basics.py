# 🎨 GUI Basics with Tkinter (Built-in with Python)

import tkinter as tk
from tkinter import messagebox

# 1. Create the root (Main Window)
root = tk.Tk()
root.title("Python GUI App 1.0")
root.geometry("400x300") # Width x Height

# 2. Add a Title (Label)
label = tk.Label(root, text="Welcome back, Chayan!", font=("Arial", 16))
label.pack(pady=20) # 'pack' adds the element to the window

# 3. Add an Entry (Input Box)
entry = tk.Entry(root, width=30)
entry.pack()

# 4. Define a Function for Button Click
def on_btn_click():
    user_input = entry.get()
    messagebox.showinfo("Message", f"Hello, {user_input}!")

# 5. Add a Button
# (Note: Don't use () when passing the function to command=)
btn = tk.Button(root, text="Greet Me!", command=on_btn_click)
btn.pack(pady=10)

# 6. Add a Quit Button
quit_btn = tk.Button(root, text="Exit Application", command=root.quit)
quit_btn.pack(pady=10)

# 7. Start the Main Event Loop 
# (This keeps the window open and listening for clicks!)
# root.mainloop()

# Summary Table
"""
| Method         | Purpose                                     |
|----------------|---------------------------------------------|
| tk.Tk()        | Initialize main window                      |
| .title()       | Set the text at top of window               |
| tk.Label()     | Static text element                         |
| tk.Entry()     | Text input field                            |
| tk.Button()    | Clickable button                            |
| .pack()        | Basic layout (stacks elements)              |
| .grid()        | Grid layout (Excel-like columns/rows)       |
| .mainloop()    | Run the GUI until closed                    |
"""
